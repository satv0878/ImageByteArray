
from PIL import Image, ImageOps

import io


def processImage(path: str) -> None:
    image=readFile(path)
    resizedImage=resizeImage(image)
    byteArr=convertToBytArray(resizedImage)
    writeFileAsByteArray(byteArr)


def readFile(path: str)-> Image:
    image = Image.open(path, mode='r')
    return image

def convertToBytArray(image: Image)-> str:
    img_byte_arr = io.BytesIO()

    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def writeFileAsByteArray(input: str) -> None: 
    f = open("bytearray.txt", "w")
    f.write(input)
    f.close()


def resizeImage(image: Image)->Image: 
    size = (800, 600)
    fit_and_resized_image = ImageOps.fit(image, size, Image.ANTIALIAS)
    return fit_and_resized_image

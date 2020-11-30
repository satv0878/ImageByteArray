
from PIL import Image, ImageOps
import base64
import io


def processImage(path: str) -> None:
    image=readFile(path)
    resizedImage: Image = resizeImage(image)
    resizedImage.show()
    byteArr = convertToBytArray(resizedImage)
    writeFileAsByteArray(byteArr)


def readFile(path: str)-> Image:
    image = Image.open(path, mode='r').convert('LA')
    print(type(image))

    return image

def convertToBytArray(image: Image)-> str:
    img_byte_arr = io.BytesIO()
    print(type(image))

    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()  
    return img_byte_arr

def writeFileAsByteArray(input: str) -> None: 
    f = open("bytearray.txt", "w")
    byteString = bytearray(input)
    for i in input:
        f.write(hex(i)+',')
    
    
    f.close()
  


def resizeImage(image: Image)->Image: 
    size = (400, 300)
    fit_and_resized_image = ImageOps.fit(image, size, Image.BILINEAR)
    return fit_and_resized_image 

from PIL import Image, ImageOps
import base64
import io
from numpy import loadtxt


def readArrayFromFile() -> None:
    fileObj = open("bytearray.txt", "r") #opens the file in read mode
    words = fileObj.read().split(',') #puts the file into an array
    fileObj.close()
    print(len(words))
    print(words[0])
    print(max(words))
    im = Image.fromarray(words)
    im.show()

    





def processImage(path: str) -> None:
    image=readFile(path)
    resizedImage: Image = resizeImage(image)

    resizedImage.save('resized.png')
    pixels = list(resizedImage.getdata())
    
    #resizedImage.show()
    #byteArr = convertToBytArray(resizedImage)

    
    writeFileAsByteArray(pixels)


def readFile(path: str)-> Image:
    image = Image.open(path, mode='r').convert('L')
    return image

def convertToBytArray(image: Image) -> str:
    
    img_byte_arr = io.BytesIO()
    print(type(image))

    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()  
    return img_byte_arr

def writeFileAsByteArray(input: list) -> None: 
    f = open("bytearray2.txt", "w")
    #byteString = bytearray(input)
    print(len(input))
    for i in input:
        f.write(hex(i)+',')
    
    
    f.close()
  


def resizeImage(image: Image)->Image: 
    size = (400, 300)
    fit_and_resized_image = ImageOps.fit(image, size, Image.BILINEAR)
    return fit_and_resized_image 
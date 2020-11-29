
from PIL import Image

import io



def readFile(path: str)-> str:
    image = Image.open(path, mode='r')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()




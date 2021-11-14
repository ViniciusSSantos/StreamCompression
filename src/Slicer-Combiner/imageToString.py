import base64
from PIL import Image
import io

def imageToString(image):
    with open(image, "rb") as image:
        converted_string = base64.b64encode(image.read())
    return converted_string
    

def stringToImage(data):
    f = io.BytesIO(base64.b64decode(data))
    pilimage = Image.open(f)
    return pilimage
import base64
from PIL import Image
import io
from IPython.display import Video

def videoToString(image):
    with open(image, "rb") as image:
        converted_string = base64.b64encode(image.read())
    return converted_string

def stringToVideo(data , output):
    decodeit = open(output + ".mp4", 'wb')
    decodeit.write(base64.b64decode((data)))
    decodeit.close()
import openai
import config
import webbrowser
import os

from PIL import Image
from io import BytesIO

openai.api_key = config.API_KEY

# Read image file and resize to square 256x256
path = '../images/'
for image_file in os.listdir(path):
    if '.png' in image_file or '.jpg' in image_file:
        image = Image.open(path+image_file)
        width, height = 512, 512
        image = image.resize((width, height))

        # Convert to bytes-like object
        byte_stream = BytesIO()
        image.save(byte_stream, format='PNG')
        byte_array = byte_stream.getvalue()

        # Make API request to create a variation of the image
        response = openai.Image.create_variation(
        image=byte_array,
        n=1,
        size="512x512"
        )

        # Open URL
        for image in response['data']:
            webbrowser.open(image['url'])


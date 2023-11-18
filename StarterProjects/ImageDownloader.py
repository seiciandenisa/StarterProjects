import os
import requests
from urllib.parse import urlparse


def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']
    for ext in extensions:
        if ext in image_url:
            return ext


def generate_name_from_url(url: str) -> str:
    parsed_url = urlparse(url)
    path_components = parsed_url.path.split('/')  # using the last non-empty path component as the base name
    base_name = next((component for component in reversed(path_components) if component), 'image')
    return base_name[:20]  # truncate the name to a reasonable length


def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:  # checking if there is a folder
            image_name: str = f'{folder}/{name}{ext}'  # appending the extension to the name of the file
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be found..')

    if os.path.isfile(image_name):  # checking if the file already exists
        raise Exception('File name already exists!')

    # Downloading image
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: {image_name} successfully!')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    # This version will get th name of the image as an input
    '''input_url: str = input('Enter a url: ')
    input_name: str = input('Please choose a name: ')

    print('Downloading..')
    download_image(input_url, name=input_name, folder='images')'''

    # create a list or urls, loop through them and give them names automatically
    urls = [
        'https: // logos - world.net / wp - content / uploads / 2021 / 10 / Python - Symbol.png',
        'https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=2000',
        'https://images.hdqwalls.com/download/small-memory-evening-8k-5o-1280x1024.jpg',
    ]

    folder_name = 'images'
    # This version will automatically generate a name using image + the index number of the url
    '''for i, url in enumerate(urls, start=1):
        input_name = f'image_{i}'  # automatically generating a name for the image
        print('Downloading...')
        download_image(url, name=input_name, folder=folder_name)'''
    
    # This version will automatically generate a name with specific word from the url
    for url in urls:
        input_name = generate_name_from_url(url)
        print('Downloading..')
        download_image(url, name=input_name, folder=folder_name)

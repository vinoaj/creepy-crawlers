import pandas as pd
from io import BytesIO
from PIL import Image
from selenium import webdriver
from urllib.parse import urlparse

driver = get_driver()


def main(csv_path):
    process_csv(csv_path)
    driver.quit()


def get_driver():
    """Create a Selenium driver using headless Chrome"""
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    return driver


def process_csv(csv_path):
    df = pd.read_csv(csv_path)
    for index, row in df.iterrows():
        generate_screenshot(row['Article URL'])


def generate_screenshot(url):
    driver.get(url)
    png = driver.get_screenshot_as_png()

    image = Image.open(BytesIO(png))
    image = image.resize((200, 150), Image.LANCZOS)

    save_path = generate_filename(url)
    image.save(save_path)


def generate_filename(url):
    url_parsed = urlparse(url)
    url_path = url_parsed.path[1:].replace('/', '-')
    if url_path[-1] is '-':
        url_path = url_path[:-1]
    return url_path + '.png'


"""
def image_crop(img_path, width, height):
    image = Image.open(img_path)
    print('Cropping: %d x %d' % (width, height))
    image_cropped = image.crop((0, 0, width, height))
    return image_cropped
"""


def image_resize(img_path, width, height):
    image = Image.open(img_path)
    image_resized = image.resize((width, height), Image.LANCZOS)
    return image_resized


if __name__ == '__main__':
    # generate_filename('/portfolio/articles/')
    main('URLs.csv')

from PIL import Image
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)


def image_crop(img_path, width, height):
    image = Image.open(img_path)
    print('Cropping: %d x %d' % (width, height))
    image_cropped = image.crop((0, 0, width, height))
    image_cropped.save('test-2.png')


def image_resize(img_path, width, height):
    image = Image.open(img_path)
    image_resized = image.resize((width, height), Image.LANCZOS)
    image_resized.save('test-3.png')


def test():
    # driver.set_window_size(200,150)
    driver.get('https://www.clickz.com/3-measurement-resolutions-to-embrace-in-2013/37876/')
    driver.get_screenshot_as_file('test.png')
    image_crop('test.png', 200, 150)
    image_resize('test.png', 200, 150)
    driver.quit()


if __name__ == '__main__':
    test()

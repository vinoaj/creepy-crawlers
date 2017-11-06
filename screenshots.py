from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)


def test():
    driver.set_window_size(200,150)
    driver.get('https://www.clickz.com/3-measurement-resolutions-to-embrace-in-2013/37876/')
    driver.get_screenshot_as_file('test.png')


if __name__ == '__main__':
    test()

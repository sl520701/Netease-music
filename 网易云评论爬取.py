from selenium import webdriver
import time
from lxml import etree
def spider():
    url = 'https://music.163.com//song?id=1330346904'
    driver = webdriver.Chrome()
    driver.get(url)
    # html = etree.HTML(driver.page_source)
    iframe = driver.find_element_by_name("contentFrame")
    driver.switch_to.frame(iframe)
    html = etree.HTML(driver.page_source)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    print(1)
    parse_one_page(html)
    submitBtn = driver.find_element_by_xpath('//div[@class="m-cmmt"]/div[3]//a[last()]')
    for x in range(2,10):
        submitBtn.click()
        time.sleep(4)
        html = etree.HTML(driver.page_source)
        print(x)
        parse_one_page(html)
def parse_one_page(html):
    id = html.xpath('//div[@class="cmmts j-flag"]//div[@class="cnt f-brk"]/a/text()')
    previews = html.xpath('//div[@class="cmmts j-flag"]//div[@class="cnt f-brk"]/text()')
    Previews = []
    for each in zip(id, previews):
        Preview = {}
        id, preview = each
        Preview['id'] = id
        Preview['preview'] = preview
        Previews.append(Preview)
    for each in Previews:
        print(each)
if __name__ == '__main__':
    spider()
# iframe = driver.find_element_by_name("contentFrame")
# driver.switch_to.frame(iframe)
# html = etree.HTML(driver.page_source)
# id2 = html.xpath('//div[@class="cmmts j-flag"]//div[@class="cnt f-brk"]/a/text()')
# print(id2)



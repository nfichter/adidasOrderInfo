from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_order_info(driver,order_number,email):
    driver.get('https://www.adidas.com/us/order-tracker')
    one = driver.find_element_by_xpath('//*[@id="dwfrm_ordersignup_orderNo"]')
    one.clear()
    one.send_keys(order_number)
    two = driver.find_element_by_xpath('//*[@id="dwfrm_ordersignup_email"]')
    two.clear()
    two.send_keys(email)
    
    driver.find_element_by_xpath('//*[@id="dwfrm_ordersignup"]/fieldset/div[3]/button').click()

    while 'Payment total' not in driver.page_source:
        pass

    driver.save_screenshot('{}.png'.format(order_number))

def main():
    f = open('orders.csv').readlines()
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    for line in f:
        line = line.replace('\n','')
        line_ = line.split(',')
        get_order_info(driver,line_[0],line_[1])

if __name__ == '__main__':
    main()
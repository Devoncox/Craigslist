# import selenium and create chrome driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Lock
import time


#chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_driver = '/Users/dev/desktop/chromedriver'

mutex = Lock()

def PostToCraigs(city, region, medium, header, html, pay, med_value):

    if mutex.locked():
        return

    mutex.acquire()
    try:

        # give absolute path of chrome webdriver

        driver = webdriver.Chrome(chrome_driver)
        # script to import Emojis yes just for emojis
        JS_ADD_TEXT_TO_INPUT = """
                  var elm = arguments[0], txt = arguments[1];
                  elm.value += txt;
                  elm.dispatchEvent(new Event('change'));
                  """

        # Manipulate variables in order to execute properly
        emoji_header = '\U0001F4B8\U0001F4B8\U0001F4B8' + header
        postal_code = '85004'

        if region == 'Central':
            region = str(1)
        elif region == 'East':
            region = str(2)
        elif region == 'North':
            region = str(3)
        elif region == 'West':
            region = str(4)
        elif region == 'South' and city not in ['San Diego', 'Phoenix', 'New York']:
            region = str(5)
        elif region == 'South' and city in ['San Diego', 'Phoenix']:
            region = str(4)
        elif region == 'South' and city == 'New York':
            region = str(6)
        elif region == 'WestChester':
            region = str(8)


        postal_codes = {

            'Phoenix': '85004',
            'San Diego': '92054',
            'Dallas': '76034',
            'New York': '11101',
            'Houston':'77001',
            'North Jersey': '07306',
            'Atlanta': '30303',
            'Miami': '33309'



        }

        if region == 'South' and city == 'New York':
            postal_code = '07306'
        else:
            postal_code = postal_codes[city]


        # Open browser and go to craigslist
        driver.get("https://accounts.craigslist.org/login")

        # Log into Craigslist
        driver.find_element_by_xpath('//*[@id="inputEmailHandle"]').send_keys("marketing@qwick.com")
        driver.find_element_by_xpath('//*[@id="inputPassword"]').send_keys("R%8*Io5g")
        driver.find_element_by_xpath('//*[@id="login"]').click()

        # Click on drop down and choose city you're posting in
        if city == 'Miami':
            driver.find_element_by_xpath("/html/body/article/section/form[2]/select").send_keys("South Florida")
        else:
            driver.find_element_by_xpath("/html/body/article/section/form[2]/select").send_keys(city)

        # Dynamic Setting up post for location and medium (job or gig)
        driver.find_element_by_xpath('/html/body/article/section/form[2]/button').click()
        if city in ['Phoenix', 'San Diego', 'Dallas', 'New York', 'Atlanta', 'Miami']:
            driver.find_element_by_xpath('/html/body/article/section/form/ul/li['+ region +']/label/input').click()
            #driver.find_element_by_xpath('/html/body/article/section/form/button').click()

        if city == 'New York' and region == '1':
                driver.find_element_by_xpath('//*[@id="new-edit"]/div/label/label[1]/input').click()
        time.sleep(10)
        # Only need to choose cities for these and not Tucson
        driver.find_element_by_xpath(
            '/html/body/article/section/form/ul/li[' + med_value + ']/label/span[1]/input').click()
        # Setting up post of Gig specific actions
        if medium == 'Gig':
            driver.find_element_by_xpath('/html/body/article/section/form/label[1]/input').click()
            driver.find_element_by_xpath('//*[@id="new-edit"]/div/label/label[5]/input').click()
        # Setting up post of Job specific actions
        elif medium == 'Job':
            driver.find_element_by_xpath('//*[@id="new-edit"]/div/label/label[9]/input').click()
            driver.find_element_by_xpath('//*[@id="new-edit"]/div/div[3]/div/button').click()

        # Enter in details into the posting
        header_element = driver.find_element_by_xpath('//*[@id="PostingTitle"]')
        driver.execute_script(JS_ADD_TEXT_TO_INPUT, header_element, emoji_header)
        driver.find_element_by_xpath('//*[@id="postal_code"]').send_keys(postal_code)
        html_section = driver.find_element_by_xpath('//*[@id="PostingBody"]')
        driver.execute_script(JS_ADD_TEXT_TO_INPUT, html_section, html)


        # Enter in Posting details specific for a Job posting
        if medium == 'Job':
            driver.find_element_by_xpath('//*[@id="ui-id-1-button"]/span[1]').click()
            driver.find_element_by_xpath('//*[@id="ui-id-5"]').click()
            driver.find_element_by_name('remuneration').send_keys(pay)
            driver.find_element_by_xpath(
                '//*[@id="new-edit"]/div/fieldset[2]/div/div/div[2]/label/label[3]/input').click()
            driver.find_element_by_xpath('//*[@id="new-edit"]/div/div[4]/div/button').click()

        # Enter in Posting details specific for Gig posting
        elif medium == 'Gig':
            driver.find_element_by_xpath('//*[@id="new-edit"]/div/label[2]/label[2]/input').click()
            driver.find_element_by_xpath('//*[@id="new-edit"]/div/label[3]/label/input').send_keys(pay)
            driver.find_element_by_xpath(
                '//*[@id="new-edit"]/div/fieldset[2]/div/div/div[2]/label/label[3]/input').click()
            driver.find_element_by_xpath('//*[@id="new-edit"]/div/div[3]/div/button').click()

        # Click through and getting to payment method
        driver.find_element_by_xpath('//*[@id="leafletForm"]/button').click()
        driver.find_element_by_xpath('/html/body/article/section/form/button').click()
        driver.find_element_by_xpath('//*[@id="publish_top"]/button').click()
        driver.find_element_by_xpath('//*[@id="new-edit"]/div/div[3]/div/button').click()

        # Enter in payment information
        driver.find_element_by_xpath('//*[@id="cardNumber"]').send_keys('5115720004234872')
        driver.find_element_by_xpath('//*[@id="cvNumber"]').send_keys('544')
        driver.find_element_by_xpath('//*[@id="cardFirstName"]').send_keys('Devon')
        driver.find_element_by_xpath('//*[@id="cardLastName"]').send_keys('Cox')
        driver.find_element_by_xpath('//*[@id="ccinfo"]/input[2]').send_keys('6501 EAST GREENWAY PARKWAY #103-470')
        driver.find_element_by_xpath('//*[@id="cardCity"]').send_keys('Scottsdale')
        driver.find_element_by_xpath('//*[@id="cardState"]').send_keys('Arizona')
        driver.find_element_by_xpath('//*[@id="cardPostal"]').send_keys('85254')
        driver.find_element_by_xpath('//*[@id="expDate"]').send_keys('1022')
        driver.find_element_by_xpath('//*[@id="submitter"]').click()
        #driver.find_element_by_xpath('//*[@id="ccard-form"]/div/table[2]/tbody/tr[2]/td[2]/input').send_keys('Devon')
        #driver.find_element_by_xpath('//*[@id="ccard-form"]/div/table[2]/tbody/tr[3]/td[2]/input').send_keys('4803279963')
    finally:
        mutex.release()
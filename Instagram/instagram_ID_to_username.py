url = 'https://commentpicker.com/instagram-user-id.php'

from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import sys
try:
	sys.argv[1]
except IndexError:
	print("python3 INSTAGRAM_USER_by_id_firefox.py <ID>")
	exit(0)


firefox_bin = "/snap/firefox/current/usr/lib/firefox/firefox"
firefoxdriver_bin = "/snap/firefox/current/usr/lib/firefox/geckodriver"

opts = webdriver.FirefoxOptions()
opts.binary_location = firefox_bin
opts.set_preference("dom.popup_maximum", 300)
#opts.add_argument('--headless')
opts.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.2535.67")

service = webdriver.firefox.service.Service(executable_path=firefoxdriver_bin)
browser = webdriver.Firefox(service=service, options=opts)

browser.get(url)

accept_cookies_button = WebDriverWait(browser, 2).until(
EC.element_to_be_clickable((By.ID, "ez-accept-all"))
)
accept_cookies_button.click()

ins_element = WebDriverWait(browser, 10).until(
EC.presence_of_element_located((By.TAG_NAME, 'ins'))
)
browser.execute_script("arguments[0].remove();", ins_element)

eliminar_anuncis = WebDriverWait(browser, 10).until(
EC.presence_of_element_located((By.CLASS_NAME, "ezoic-ad"))
)
browser.execute_script("arguments[0].remove();", eliminar_anuncis)

browser.execute_script("""
var iframes = document.getElementsByTagName('iframe');
while (iframes.length > 0) {
iframes[0].parentNode.removeChild(iframes[0]);
}
""")

username = browser.find_element(By.ID, "instagram-username")
username.send_keys( sys.argv[1] )

captcha_label = WebDriverWait(browser, 3).until(
EC.presence_of_element_located((By.CSS_SELECTOR, 'label.search-form__label[for="captcha"]'))
)
strong_element = captcha_label.find_element(By.TAG_NAME, 'strong')
captcha = eval(strong_element.text.replace(' =',''))

CAPTXA = browser.find_element(By.ID, "captcha")
CAPTXA.send_keys( captcha )

cerca_usuari = WebDriverWait(browser, 10).until(
EC.element_to_be_clickable((By.ID, "js-start-button"))
)
browser.execute_script("arguments[0].scrollIntoView(true);", cerca_usuari)

cerca_usuari.click()

from time import sleep
sleep(5)

nomdeusuari = WebDriverWait(browser, 10).until(
EC.element_to_be_clickable((By.ID, "js-results-id"))
)

print("\nEl usuari és:\t{}\n\n".format(nomdeusuari.text))

browser.quit()

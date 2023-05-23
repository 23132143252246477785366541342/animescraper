from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from os import mkdir, path, listdir
import inquirer

print("Welcome to anime scraper!")
animeInput = input("Please search for anime: ")

questions = [
    inquirer.List(
        "size",
        message="What size do you need?",
        choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
    ),
]

answers = inquirer.prompt(questions)

anime = '86'
root = "https://www3.gogoanimes.fi"
url = f"https://www3.gogoanimes.fi/category/{anime}"

if path.exists("downloads\\{anime}"):
    mkdir(f"downloads\\{anime}")

chrome_options = Options()


chrome_options.add_argument("--user-data-dir=C:\\Users\\Tony Tran\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument('--profile-directory=Profile 1')

params = {
    "behavior": "allow",
    "downloadPath": f'C:\\Users\\Tony Tran\\Desktop\\a\\animeScraper\\downloads\\{anime}'
}

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

browser = uc.Chrome(desired_capabilities=caps, options=chrome_options)
browser.execute_cdp_cmd("Page.setDownloadBehavior", params)

print("hi")

browser.get(url)

browser.maximize_window()

req = browser.page_source
soup = BeautifulSoup(req, 'html.parser')
a = [i["href"][1:] for i in soup.find("ul", {"id": "episode_related"}).find_all("a")]
downloads = []

for i in a:
    browser.get(root + i)
    req = browser.page_source
    soup = BeautifulSoup(req, 'html.parser')

    downloads.append(soup.find("li", {"class": "dowloads"}).findChild("a")["href"])

gogoDownloads = []
for i in downloads:
    browser.get(i)
    sleep(3)
  
    
x1=0
while x1==0:
    count=0
    li = listdir(f"downloads\\{anime}")
    for x1 in li:
        if x1.endswith(".crdownload"):
            count = count+1
    if count==0:
        x1=1
    else:
        x1=0
    sleep(1)
sleep(2)
browser.quit()
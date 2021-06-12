from bs4 import BeautifulSoup
import mechanicalsoup
from urllib.request import Request, urlopen
import time

url = "https://realpython.com/python-web-scraping-practical-introduction/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


# ***** MechanicalSoup Stuff *****
# Browser objects represent the headless web browser. 
# You can use them to request a page from the Internet by passing a URL to their .get() method
browser = mechanicalsoup.Browser()
page = browser.get(url)

# page is a Response object that stores the response from requesting the URL from the browser
# print(page) 
# print(type(page.soup))

# You can view the HTML by inspecting the .soup attribute
# print(page.soup)
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profile_page = browser.submit(form, login_page.url)
# print(profile_page.url)

# Now that we have the profiles_page variable set, 
# let’s see how to programmatically obtain the URL for each link on the /profiles page
# To do this, you use .select() again, this time passing the string "a" 
# to select all the <a> anchor elements on the page
links = profile_page.soup.select("a")

base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    # print(f"{text}: {address}")


# Open your browser of choice and navigate to the URL http://olympus.realpython.org/dice. 
# This /dice page simulates a roll of a six-sided die, 
# updating the result each time you refresh the browser. 
# Below, you’ll write a program that repeatedly scrapes the page for a new result.
# The first thing you need to do is determine which element on the page contains the result of the die roll. Do this now by right-clicking anywhere on the page and selecting View page source.
# A little more than halfway down the HTML code is an <h2> tag :
# looks like this <h2 id="result">4</h2>

url = "http://olympus.realpython.org/dice"
for i in range(4):
    page = browser.get(url)
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(4)
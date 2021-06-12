from urllib.request import Request, urlopen
import re

url = "https://realpython.com/python-web-scraping-practical-introduction/"

def find_information_with_string_method(tag, html):
    open_tag = "<" + tag + ">"
    close_tag = "</" + tag + ">"
    start_tag_index = html.find(open_tag)
    start_index = start_tag_index + len(open_tag)
    end_index = html.find(close_tag)
    title = html[start_index:end_index]
    return title


def find_information_with_regex(tag, html):
    pattern = "<" + tag + ".*?>.*?</" + tag + ".*?>"
    information = re.search(pattern, html, re.IGNORECASE)
    title = information.group()
    title = re.sub("<.*?>", "", title)
    return title

def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)    
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html


def get_result(url, tag):
    html = get_html(url)
    information = find_information_with_string_method(tag, html)
    information_using_regex = find_information_with_regex(tag, html)
    return information_using_regex

print(get_result(url, 'title'))

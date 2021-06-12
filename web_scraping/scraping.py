from urllib.request import Request, urlopen

url = "https://realpython.com/python-web-scraping-practical-introduction/"

def find_information(tag, html):
    open_tag = "<" + tag + ">"
    close_tag = "</" + tag + ">"
    start_tag_index = html.find(open_tag)
    start_index = start_tag_index + len(open_tag)
    end_index = html.find(close_tag)
    title = html[start_index:end_index]
    return title


def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)    
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html


def get_result(url, tag):
    html = get_html(url)
    information = find_information(tag, html)
    return information


print(get_result(url, 'title'))

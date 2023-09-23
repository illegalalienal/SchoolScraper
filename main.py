import pandas as pd #allows 2d array to be printed properly
import ssl  #internet stuff, verification
ssl._create_default_https_context = ssl._create_unverified_context #allows scraper to connect with unverified connection
import requests
from lxml import html   #web scraper

def get_html(url):
    response = requests.get(url, verify=False)
    source_code = response.content
    return source_code
def get_data_table(source_code):
    data_table = []
    html_elem = html.document_fromstring(source_code)
    tables = html_elem.cssselect("table")

    return tables[0]


def scrape_data(url):
    return get_data_table(get_html(url))

#The 3 methods above comprise the entire function of the data scraper.

if __name__ == '__main__':
    print("Beginning Now: \n")

    class_info = [] #2 Dimensional array of strings that will contain all class information.

    url_iterator = 1
    url = "https://apps.fit.edu/schedule/main-campus/fall?query=&page=" + str(url_iterator) #URL is structured a bit weird, but thats because there are 50 pages of class information
                                                                                            #and I fully intend on scraping it all at some point.

    data_table = scrape_data(url)

    trs = data_table.cssselect('tr')    #table rows

    #nested for loop handles reading data and assigning to variables
    row = -1
    for tr in trs:
        if row == -1:
            row += 1
            continue

        col = 0
        output_table_row = []
        tds = tr.cssselect('td')
        curr_class = [""] * 11

        for td in tds:
            cell_text = td.text_content().strip()
            curr_class[col] = cell_text
            col += 1

        class_info.append(curr_class)
        row += 1

    print(pd.DataFrame(class_info))
    print(len(class_info))

import pandas as pd #allows 2d array to be printed properly
import ssl  #internet stuff, verification
import course
import requests
import urllib3
from lxml import html   #web scraper

ssl._create_default_https_context = ssl._create_unverified_context #allows scraper to connect with unverified connection
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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

def populate_with_results(class_info, url):
    data_table = scrape_data(url)

    trs = data_table.cssselect('tr')  # table rows

    # nested for loop handles reading data and assigning to variables
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

        curr_course = course.Course(curr_class[0], curr_class[1], curr_class[2], curr_class[3], curr_class[4], curr_class[5],
                                curr_class[6], curr_class[7], curr_class[8], curr_class[9], curr_class[10])
        class_info.append(curr_course)
        row += 1


#The 3 methods above comprise the entire function of the data scraper.

if __name__ == '__main__':
    print("Beginning Now: \n")

    class_info = [] #2 Dimensional array of strings that will contain all class information.

    url_iterator = 1
    url = "https://apps.fit.edu/schedule/main-campus/fall?query=&page=" + str(url_iterator) #URL is modular so that several pages can be scanned

    while True: #loops through pages until one is found that doesn't contain a table, the first incorreect result
        try:
            print("Currently checking URL " + url)
            populate_with_results(class_info, url)
            url_iterator += 1
            url = "https://apps.fit.edu/schedule/main-campus/fall?query=&page=" + str(url_iterator)
        except IndexError:
            break

    #print(pd.DataFrame(class_info))
    for course in class_info:
        print(course)
    print(len(class_info))

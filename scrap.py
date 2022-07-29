# import requests
# import pdb
# from bs4 import BeautifulSoup
# '''
# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id = "ResultsContainer")
# job_elements = results.find_all("div", class_ = "card-content")
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_ = "title")
#     company_element = job_element.find("h3", class_ = "company")
#     location_element = job_element.find("p", class_ = "location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
# '''
# # print(job_element, end = "\n\n")
# # print(results.prettify())
# # print(page.text)
# # print(soup.prettify())
# # a = input("End")
#
# pdb.set_trace()
# file = open("out.csv", "a")
# headers = ({"User agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari"
#                           "/537.36","Accept-language" : "en-US,en;q=0.5"})
# '''
# url = "https://www.amazon.com/Data-Mining-Concepts-Techniques-Management/dp/" \
#       "0123814790/ref=sr_1_1?crid=1IH6TACDFSIEJ&keywords=han+and+kamber+data+" \
#       "science&qid=1643831716&s=books&sprefix=han+and+kamber+data+" \
#       "sci%2Cstripbooks-intl-ship%2C546&sr=1-1"
# '''
# url = "https://www.flipkart.com/data-mining-concepts-techniques-3rd/"\
#       "product-reviews/itmdfjfz25wfbhxy?pid=9789380931913&lid=""" \
#       "LSTBOK97893809319130SWFNL&marketplace=FLIPKART"
# page = requests.get(url, headers = headers)
# soup = BeautifulSoup(page.content, "lxml")
# print(soup)
# print("Searching for title:")
# try:
#     title = soup.find("div", class_ = "_2s4DIt _1CDdy2")
#     title_string =  title.string.strip().replace(',','')
# except AttributeError:
#     print("Attribute error")
#     title_string = "NA"
# print("Title string: ", title_string)
# '''
# try:
#     subtitle = soup.find("span", attr = {"id": "productSubtitle"})
#     subtitle_string = subtitle.string.strip().replace(',', '')
# except AttributeError:
#     print("Attribute error")
#     subtitle_string = "NA"
# print("Product subtitle = ", subtitle_string)
# '''
# # file.write("Title, ", "Subtitle, ")
# # file.write(f"{title_string}, {subtitle_string}, ")
# file.write("Title, ")
# file.write(f"{title_string}")
# file.close()
# import module
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import pdb
import csv
import pandas as pd

pdb.set_trace()
HEADERS = ({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/90.0.4430.212 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5"})


# user define function
# Scrape the data
def get_text_from_page(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


def html_code(url):
    # pass the url
    # into getdata function
    htmldata = get_text_from_page(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    # display html code
    return soup


# customer review
def get_review_text_list(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""

    # for item in soup.find_all("div",
    #                           class_="a-expander-content reviewText "
    #                                  "review-text-content "
    #                                  "a-expander-partial-collapse-content"):
    #     data_str = data_str + item.get_text()

    for item in soup.find_all("span", class_ = "review-text"):
        data_str = data_str + item.get_text()


    result = data_str.split("\n")
    return result
# The lines in this function containing count_span need to be commented out
# and the indentation fixed accordingly in case there is no section for the
# top positive review and the top critical review on the web page
def get_review_title_list(soup):
    title_str = ""
    count_span = 0
    for item in soup.find_all("a", class_ = "review-title"):
        title_str = title_str + item.get_text()
    for item in soup.find_all("span", class_ = "review-title"):
        if count_span >= 2:
            title_str = title_str + item.get_text()
        count_span += 1

    result = title_str.split("\n")
    return result

def get_next_page_url(soup):
    page = soup.find('ul', class_ = 'a-pagination')
    if not page:
        return
    if not page.find('li', class_ = 'a-disabled a-last'):
        url = "https://www.amazon.in" + \
              str(page.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return

# url = "https://www.amazon.in/Columbia-Mens-wind-\
# resistant-Glove/dp/B0772WVHPS/?_encoding=UTF8&pd_rd\
# _w=d9RS9&pf_rd_p=3d2ae0df-d986-4d1d-8c95-aa25d2ade606&pf\
# _rd_r=7MP3ZDYBBV88PYJ7KEMJ&pd_rd_r=550bec4d-5268-41d5-\
# 87cb-8af40554a01e&pd_rd_wg=oy8v8&ref_=pd_gw_cr_cartx&th=1"

# url = "https://www.amazon.in/Columbia-Mens-wind-resistant-Glove/"\
#       "product-reviews/B085YJH4RL/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&"\
#       "reviewerType=all_reviews"

# url = "https://www.amazon.in/Columbia-Mens-wind-resistant-Glove/"\
#       "product-reviews/B085YJH4RL/ref=cm_cr_dp_d_show_all_btm?ie=UTF8"\
#       "&reviewerType=all_reviews"
'''
url = "https://www.amazon.in/Data-Mining-Concepts-Techniques-Management/"\
      "product-reviews/0123814790/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&"\
      "reviewerType=all_reviews"
'''
# url = "https://www.amazon.in/Programming-Language-PROGRAMMING-LANG-_p2-ebook/"\
#       "product-reviews/B009ZUZ9FW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&"\
#       "reviewerType=all_reviews"
# url  = "https://www.amazon.in/OnePlus-Bullets-Wireless-Bass-Black/"\
#        "product-reviews/B092ZJVB6Z/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&"\
#        "reviewerType=all_reviews"
# url = "https://www.amazon.in/HIT-Anti-Mosquito-Racquet-Rechargeable/"\
#       "product-reviews/B07S5FBY3J/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&"\
#       "reviewerType=all_reviews"
# url = "https://www.amazon.in/Harry-Potter-Philosophers-Stone-Rowling/"\
#       "product-reviews/1408855658/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&"\
#       "reviewerType=all_reviews"
url = "https://www.amazon.in/American-Tourister-AMT-SCH-03/product-reviews/"\
      "B07CGSJNML/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
soup = html_code(url)
print(soup)

soup_list = [soup]
urls = [url]
next_url = None
next_soup = None
# Approximate maximum number of reviews to be collected
max_reviews = 14000
while True:
    if next_url:
        url = next_url
    if next_soup:
        soup = next_soup
    if len(soup_list) >= max_reviews/10:
        break
    next_url = get_next_page_url(soup)

    if next_url:
        urls.append(next_url)
        next_soup = html_code(next_url)
        soup_list.append(next_soup)
    else:
        break
    # print("About to sleep")
    print("Current URL:", url)
    # sleep(randint(3, 10))
    # print("Woke up")

print(urls)
rev_text_for_write = []
rev_titles_for_write = []
'''
for soup in soup_list:
    rev_data = get_review_text_list(soup)
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_text_for_write.append(i)

    rev_titles = get_review_title_list(soup)
    for i in rev_titles:
        if i == "":
            pass
        else:
            rev_titles_for_write.append(i)
'''
def return_list_removed_values(l, value):
    return[x for x in l if x != value]

for soup in soup_list:
    rev_text = get_review_text_list(soup)
    rev_titles = get_review_title_list(soup)
    rev_text = return_list_removed_values(rev_text, "")
    rev_titles = return_list_removed_values(rev_titles, "")
    if len(rev_text) != len(rev_titles):
        continue
    for i in rev_text:
        rev_text_for_write.append(i)
    for i in rev_titles:
        rev_titles_for_write.append(i)
'''
with open("review_debug.txt", "w", encoding = "utf-8") as f:
    i = 0
    while i < len(rev_titles_for_write):
        f.write(rev_titles_for_write[i] + "\n" + rev_text_for_write[i] +
                "\n______\n")
        i += 1
    f.write("TEXT WITHOUT TITLES?\n")
    while i < len(rev_text_for_write):
        f.write(rev_text_for_write[i] + "\n")
        i += 1
'''
# initialise data of lists.
data = {"Review title": rev_titles_for_write, 'Review': rev_text_for_write}
# Create DataFrame
df = pd.DataFrame(data)
# Save the output.
df.to_csv('amazon_review_american_tourister_bag.csv')
# df.to_csv('amazon_reviews_k_and_r_c.csv')

#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json

#adres URL strony z opiniami
url_prefix = "https://www.ceneo.pl"
product_id = input("Podaj kod produktu: ")
url_postfix = "#tab=reviews"
url = url_prefix+"/"+product_id+url_postfix

#wybranie z kodu strony fragmenów odpowiadających poszczególnym opiniom
#opinions = page_tree.select("li.review-box")


#pusta lista na opinie
opinions_list = []

while url is not None:
    #pobranie kodu HTML strony z adresu URL 
    page_response =  requests.get(url)
    page_tree = BeautifulSoup(page_response.text, 'html.parser')
    opinions = page_tree.select("li.js_product-review")
    #ekstrakcja składowych dla pierwszej opinii z listy
    for opinion in opinions:
        #opinion = opinions.pop()
        opinion_id = opinion["data-entry-id"]
        #opinion_id = opinion["js_product-review"]47281024
        author = opinion.select('div.reviewer-name-line').pop().string.strip()
        try:
            recomendation = opinion.select('div.product-review-summary > em').pop().string
        except IndexError:
            recomendation = None
        stars = opinion.select('span.review-score-count').pop().string
        try:
            purchased = opinion.select('div.product-review-pz').pop().string
        except IndexError:
            purchased = None
        useful = opinion.select('button.vote-yes').pop()["data-total-vote"]
        useless = opinion.select('button.vote-no').pop()["data-total-vote"]
        content = opinion.select('p.product-review-body').pop().get_text()
        try:
            cons = opinion.select('div.cons-cell > ul').pop().get_text()
        except IndexError:
            cons = None
        try:
            pros = opinion.select('div.pros-cell > ul').pop().get_text()
        except IndexError:
            pros = None    
        date = opinion.select('span.review-time > time')
        review_date = date.pop(0)["datetime"]
        try:
            purchase_date = date.pop(0)["datetime"]
        except IndexError:
            purchase_date = None

        opinion_dict = {
            "opinion_id":opinion_id,
            "author":author,
            "recomendation":recomendation,
            "stars":stars,
            "content":content,
            "pros":pros,
            "cons":cons,
            "useful":useful,
            "useless":useless,
            "purchased":purchased,
            "purchase_date":purchase_date,
            "review_date":review_date     
        }
        opinions_list.append(opinion_dict)
    try:
        url = url_prefix+page_tree.select("a.pagination__next").pop()["href"]
    except IndexError:
        url = None
    print("url to",url)
    print("liczba opinii to:",len(opinions_list))

        #print(opinion_id,author,recomendation,stars,content,pros,cons,useful,useless,purchased,purchase_date,review_date)
filename = product_id+".json"
with open(filename, 'w', encoding="utf-8") as fp:
    json.dump(opinions_list,fp, ensure_ascii=False)






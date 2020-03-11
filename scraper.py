#import bibliotek
import requests
from bs4 import BeautifulSoup
#adres URL strony z opiniami
url = "https://www.ceneo.pl/47281024#tab=reviews"
#rl = "https://www.ceneo.pl/76891706#tab=reviews"
#pobranie kodu HTML strony z adresu URL 
page_response =  requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')

# - opinia li.review box
# - identyfikator li.review box[data-entry-id]
# - autor div.reviewer-name-line
# - rekomendacja div.product-review-summary > em 
# - liczba gwiazdek span.review-score-count
# - czy potwierdzona zakupem  div.product-review-pz
# - data wystawienia span.review-time > time
# ["datetime"] - pierwsze wystapienie 
# - data zakupu span.review-time > time
# ["datetime"] - drugie wystapienie
# - przydatna: button.vote-yes["data-total-vote"]
# - nieprzydatna button.vote-no["data-total-vote"]
# - treść p.product-review-body
# - wady div.cons-cell > ul
# - zalety div.pros-cell > ul

#wybranie z kodu strony fragmenów odpowiadających poszczególnym opiniom
opinions = page_tree.select("li.review-box")

opinion = opinions.pop()
opinion_id = opinion.select('li.review box["data-entry-id"]').pop().string
author = opinion.select('div.reviewer-name-line').pop().string
recomendation = opinion.select('div.product-review-summary > em').pop().string
stars = opinion.select('span.review-score-count').pop().string
purchased = opinion.select('div.product-review-pz').pop().string
useful = opinion.select('button.vote-yes').pop()["data-total-vote"]
useless = opinion.select('button.vote-no').pop()["data-total-vote"]
content = opinion.select('p.product-review-body').pop().get_text()

#ekstrakcja składowych dla pierwszej opinii z listy





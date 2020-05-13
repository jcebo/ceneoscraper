class Product:
    def __init__(self, product_id=None, name=None, opinions=[]):
        self.product_id = product.id
        self.name = name 
        self.opinions = opinions
    def extract_product(self):
        page_response =  requests.get("https://www.ceneo.pl"+request.form['product_code'])
        page_tree = BeautifulSoup(page_response.text, 'html.parser')
        self.name = int(page_tree.select("h1.product_name").pop().get_text().strip())
        
        try:
            opinions_count = page_tree.select("a.product-reviews-link > span").pop().get_text().strip()
        except IndexError:
            opinions_count = 0
        if opinions_count > 0:
            url_prefix = "https://www.ceneo.pl"
            url_postfix = "#tab=reviews"
            url = url_prefix+"/"+self.product_id+url_postfix
            while url:
                #pobranie kodu HTML strony z adresu URL 
                page_response =  requests.get(url)
                page_tree = BeautifulSoup(page_response.text, 'html.parser')
                opinions = page_tree.select("li.js_product-review")
                #ekstrakcja składowych dla pierwszej opinii z listy
                for opinion in opinions:     
                    op = Opinion()
                    op.extract_opinion(opinion)
                    self.opinion.append(op)

                   
                    
        
                    opinions_list.append(features)            
class Selectors(Enum):
    AUTHOR = ['div.reviewer-name-line']        

class Opinion:
    #lista składowych opinii wraz z selektorami i atrybutami
    selectors = {            
            "author": ['div.reviewer-name-line'],
            "recommendation": ['div.product-review-summary > em'],
            "stars":['span.review-score-count'],
            "content":['p.product-review-body'],
            "pros":['div.pros-cell > ul'],
            "cons":['div.cons-cell > ul'],
            "useful":['button.vote-yes', "data-total-vote"],
            "useless":['button.vote-no', "data-total-vote"],
            "purchased":['div.product-review-pz'],
            "purchase_date":['span.review-time > time:nth-of-type(1)',"datetime"],
            "review_date":['span.review-time > time:nth-of-type(2)',"datetime"]    
                }
    #konstruktor (inicjalizator) obiektu klasy            
    def __init__(self, opinion_id=None, author=None, recommendation=None, stars=None, content=None, 
                pros=None, cons=None, useful=None, useless=None, purchased=None, purchase_date=None, review_date=None):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.useful = useful
        self.uselss = useless
        self.purchased = purchased
        self.purchase_date = purchase_date
        self.reiew_date = review_date
    # reprezentacja tekstowa obiektu klasy
    def __str__(self):
        return f'opinion id: {opinion_id}\n author: {author}\n' 
    #reprezetnacja słownikowa obiektu   
    def __repr__(self):
        pass

    def extract_opinion(self):
        features = {key:extract_feature(opinion, *args)
                    for key,args in selectors.items()}
        self.opinion_id = int(opinion["data-entry-id"])
        pass
    def transform_opinion(self):
            features["purchased"] = True if features["purchased"] == "Opinia potwierdzona zakupem" else False
                    features["useful"] = int(features["useful"])
                    features["useless"] = int(features["useless"])
                    features["content"] = features["content"].replace("\n", ". ").replace("\r",". ")
                    features["pros"] = remove_whitespaces(features["pros"])
                    features["cons"] = remove_whitespaces(features["cons"])
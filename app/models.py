class Product:
    def __init__(self, product_id=None, name=None, opinions=[]):
        self.product_id = product.id
        self.name = name 
        self.opinions = opinions

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
    def extract_opinion(self):

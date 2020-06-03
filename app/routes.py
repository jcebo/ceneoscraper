from app import app
from flask import render_template, request, redirect, 
from flaskext.markdown import Mardown
from app.forms import ProductForm
from app.models import Product, Opinion
import requests
import pandas as pd
app.config['SECRET_KEY'] = "Tajemniczy_mysi_sprzęt"
Markdown(app)
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/extraction.html', methods = ['POST', 'GET'])
def extraction():
    form = ProductForm()
    if form.validate_on_submit():
        page_response =  requests.get("https://www.ceneo.pl"+request.form['product_code'])
        if page_response.status_code == 200:
            product = Product(request.form['product_code'])
            product.extract_product()
            product.save_product()
            return redirect(url_for(product, product_id=product.product_id))
        else:
            form.product_code.errors.append("Dla podanego kodu nie ma produktu")
            return render_template("extraction.html", form=form)             
    return render_template("extraction.html", form=form)
    

@app.route('/list.html')
def list():
    pass
@app.route('/author.html')
def author():
    content = ""
    with open("README.md", "r", endcoding="UTF-8") as f:
            content = f.read()
    return render_template("author.html", text=content)

@app.route('/product/<product_id>')
def product(product_id):
    product = Product()
    product.read_product(product_id)
    opinions = pd.DataFrame.from_records([opinion.__dict__() for opinion in product.opinions])
    opinions["stars"] = opinions["stars"].map(lambda x: float(x.split("/")[0].replace(",",".")))
    return render_template("product.html", tables=[
        opinions.to_html(
            classes='table table-bordered table-sm table-responsive',
            table_id="opinions"
        )
    ])
    

@app.route('/analyzer/<product_id>')
def analyzer():
    return "POdaj kod produktu do analizy"
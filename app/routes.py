from app import app
from flask import render_template
from flaskext.markdown import Mardown
from app.forms import ProductForm
app.config['SECRET_KEY'] = "Tajemniczy_mysi_sprzęt"
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!" 

@app.route('/extraction.html', methods = ['POST', 'GET'])
def extraction():
    form = ProductForm()
    if form.validate_on_submit():
        return "Przesłano formularz"
    
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
def product():
    

@app.route('/analyzer/<product_id>')
def analyzer():
    return "POdaj kod produktu do analizy"
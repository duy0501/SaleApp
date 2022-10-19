from flask import render_template

from saleapp import app,dao


@app.route("/")

def index():
    cate=dao.load_categories()
    pro=dao.load_products()
    return render_template('index.html',categories=cate,products=pro)
if __name__=='__main__':
    app.run(debug=True)


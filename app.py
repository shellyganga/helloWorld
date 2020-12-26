from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/templates/about.html')
def about_html():
    return render_template('about.html')

@app.route('/article')
def article():
    return render_template('article.html')

@app.route('/templates/article.html')
def article_html():
    return render_template('article.html')

@app.route('/claims')
def claims():
    return render_template('claims.html')

@app.route('/templates/claims.html')
def claims_html():
    return render_template('claims.html')

@app.route('/sentence')
def sentence():
    return render_template('sentence.html')

@app.route('/templates/sentence.html')
def sentence_html():
    return render_template('sentence.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/templates/summary.html')
def summary_html():
    return render_template('summary.html')


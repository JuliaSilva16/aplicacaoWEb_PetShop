from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/index')
def index():
    return redirect('index')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
@app.route('/acompanhamento')
def acompanhamento():
    return render_template('acompanhamento.html')

@app.route('/gestao')
def gestao():
    return render_template('gestao.html')

@app.route('/relatorio')
def relatorio():
    return render_template('relatorio.html')

@app.route('/controle')
def controle():
    return render_template('controle.html')

if __name__ == '__main__':
    app.run(debug=True)
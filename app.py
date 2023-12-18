from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)


@app.route('/')
def inicio():
        return render_template('Inicio.html')


@app.route('/servicos')
def servicos():
        return render_template('Servicos.html')


@app.route('/orcamentos')
def orcamentos():
        return render_template('Orcamento.html')


if __name__ == '__main__':
    app.run()
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/pag-inicial.html')

@app.route('/about')
def about():
    return render_template('pages/sobre-nos.html')

@app.route('/form')
def contact():
    return render_template('pages/formulario.html')

if __name__ == '__main__':
    app.run(debug=True)

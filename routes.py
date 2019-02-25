from flask import Flask,redirect, render_template,url_for
app = Flask(__name__, template_folder='static/templates')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/template')
def template():
    return render_template("template.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host="0.0.0.0")
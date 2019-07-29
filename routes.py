from flask import Flask,redirect, render_template,url_for
import os
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

@app.route('/sitemap.xml')
def sitemap():
    return render_template("sitemap.xml")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__ == '__main__':
    app.static_folder = 'static'
    env_port = int(os.environ.get('PORT', 5000)) # Grabs port from environment variables, else sets to 5000
    app.run(host="0.0.0.0", port=env_port)

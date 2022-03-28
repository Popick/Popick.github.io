from flask import Flask, request, render_template, session
from datetime import datetime
import codecs

app = Flask(__name__)
app.secret_key = "o03af53aUrJHZAjD0eKWgWVTqS7XL7FU"


def open_html_file(file_name):
    f = codecs.open(file_name, "r", 'utf-8')
    txt = f.read()
    f.close()
    return txt


def open_image(img):
    with open(img, "rb") as image_file:
        return image_file.read()


@app.route('/<js_file>.js')
def open_js(js_file):
    return open_html_file("assets/" + js_file + ".js")


@app.route('/<css_file>.css')
def open_css(css_file):
    return open_html_file("assets/" + css_file + ".css")


@app.route('/imgs/<image>')
def back_png(image):
    return open_image('imgs/' + image)


@app.route('/<html_file>')
def open_html(html_file):
    if 'username' in session:
        try:
            return render_template(html_file + ".html")
        except:
            return "404 Not found!"
    else:
        return render_template("login.html")


@app.route('/')
def index():
    return("bonkers")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

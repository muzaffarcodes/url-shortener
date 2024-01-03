from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'  # Change to your domain

# In-memory database to store original and shortened URLs
urls = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    short_url = generate_short_url()
    urls[short_url] = long_url
    return render_template('shorten.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if short_url in urls:
        long_url = urls[short_url]
        return redirect(long_url)
    else:
        return render_template('not_found.html')

if __name__ == '__main__':
    app.run()

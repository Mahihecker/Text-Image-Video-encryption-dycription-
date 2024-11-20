from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    """
    Landing page with options for text, image, and video cryptography.
    """
    return render_template('index.html')

@app.route('/text')
def text_cryptography():
    """
    Page for text cryptography.
    """
    return render_template('text_cryptography.html')

@app.route('/image')
def image_cryptography():
    """
    Page for image cryptography.
    """
    return render_template('image_cryptography.html')

@app.route('/video')
def video_cryptography():
    """
    Page for video cryptography.
    """
    return render_template('video_cryptography.html')

if __name__ == '__main__':
    app.run(debug=True)

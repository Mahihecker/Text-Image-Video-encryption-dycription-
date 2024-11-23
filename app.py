from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename
from encrypt_image import encrypt_image
from decrypt_image import decrypt_image
from encrypt_video import encrypt_video
from decrypt_video import decrypt_video

app = Flask(__name__)

# Configure upload and processed folders for images and videos
UPLOAD_FOLDER_IMAGES = 'static/uploads/images'
PROCESSED_FOLDER_IMAGES = 'static/processed_images'
UPLOAD_FOLDER_VIDEOS = 'static/uploads/videos'
PROCESSED_FOLDER_VIDEOS = 'static/processed_videos'
os.makedirs(UPLOAD_FOLDER_IMAGES, exist_ok=True)
os.makedirs(PROCESSED_FOLDER_IMAGES, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_VIDEOS, exist_ok=True)
os.makedirs(PROCESSED_FOLDER_VIDEOS, exist_ok=True)

app.config['UPLOAD_FOLDER_IMAGES'] = UPLOAD_FOLDER_IMAGES
app.config['PROCESSED_FOLDER_IMAGES'] = PROCESSED_FOLDER_IMAGES
app.config['UPLOAD_FOLDER_VIDEOS'] = UPLOAD_FOLDER_VIDEOS
app.config['PROCESSED_FOLDER_VIDEOS'] = PROCESSED_FOLDER_VIDEOS

# Initialize variables to store processed paths or results
current_encrypted_text = None
current_decrypted_text = None
current_encrypted_image = None
current_decrypted_image = None
current_encrypted_video = None
current_decrypted_video = None


@app.route('/')
def index():
    """
    Home page with links to Text, Image, and Video Cryptography.
    """
    return render_template('index.html')


@app.route('/text', methods=['GET', 'POST'])
def text_cryptography():
    """
    Page for text cryptography.
    """
    global current_encrypted_text, current_decrypted_text

    if request.method == 'POST':
        if 'encrypt' in request.form:
            # Handle text encryption
            text = request.form['text']
            encryption_key = request.form['encryption_key']
            if text and encryption_key:
                # Simulate encryption (replace with actual logic)
                current_encrypted_text = ''.join(
                    chr(ord(char) + len(encryption_key)) for char in text
                )
        elif 'decrypt' in request.form:
            # Handle text decryption
            encrypted_text = request.form['encrypted_text']
            decryption_key = request.form['decryption_key']
            if encrypted_text and decryption_key:
                # Simulate decryption (replace with actual logic)
                current_decrypted_text = ''.join(
                    chr(ord(char) - len(decryption_key)) for char in encrypted_text
                )

    return render_template(
        'text_cryptography.html',
        encrypted_text=current_encrypted_text,
        decrypted_text=current_decrypted_text
    )


@app.route('/image', methods=['GET', 'POST'])
def image_cryptography():
    """
    Page for image cryptography.
    """
    global current_encrypted_image, current_decrypted_image

    if request.method == 'POST':
        if 'encrypt' in request.form:
            # Handle image encryption
            image = request.files['image']
            encryption_key = request.form['encryption_key']
            if image and encryption_key:
                filename = secure_filename(image.filename)
                upload_path = os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename)
                image.save(upload_path)

                encrypted_filename = f"encrypted_{filename}"
                encrypted_path = os.path.join(app.config['PROCESSED_FOLDER_IMAGES'], encrypted_filename)

                # Encrypt the image
                encrypt_image(upload_path, encryption_key.encode(), encrypted_path)

                # Update the encrypted image path
                current_encrypted_image = encrypted_filename

        elif 'decrypt' in request.form:
            # Handle image decryption
            image = request.files['image']
            decryption_key = request.form['decryption_key']
            if image and decryption_key:
                filename = secure_filename(image.filename)
                upload_path = os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename)
                image.save(upload_path)

                decrypted_filename = f"decrypted_{filename}"
                decrypted_path = os.path.join(app.config['PROCESSED_FOLDER_IMAGES'], decrypted_filename)

                # Decrypt the image
                decrypt_image(upload_path, decryption_key.encode(), decrypted_path)

                # Update the decrypted image path
                current_decrypted_image = decrypted_filename

    return render_template(
        'image_cryptography.html',
        encrypted_image=current_encrypted_image,
        decrypted_image=current_decrypted_image
    )


@app.route('/video', methods=['GET', 'POST'])
def video_cryptography():
    """
    Page for video cryptography.
    """
    global current_encrypted_video, current_decrypted_video

    if request.method == 'POST':
        if 'encrypt' in request.form:
            # Handle video encryption
            video = request.files['video']
            encryption_key = request.form['encryption_key']
            if video and encryption_key:
                filename = secure_filename(video.filename)
                upload_path = os.path.join(app.config['UPLOAD_FOLDER_VIDEOS'], filename)
                video.save(upload_path)

                encrypted_filename = f"encrypted_{filename}"
                encrypted_path = os.path.join(app.config['PROCESSED_FOLDER_VIDEOS'], encrypted_filename)

                # Encrypt the video
                encrypt_video(upload_path, encryption_key.encode(), encrypted_path)

                # Update the encrypted video path
                current_encrypted_video = encrypted_filename

        elif 'decrypt' in request.form:
            # Handle video decryption
            video = request.files['video']
            decryption_key = request.form['decryption_key']
            if video and decryption_key:
                filename = secure_filename(video.filename)
                upload_path = os.path.join(app.config['UPLOAD_FOLDER_VIDEOS'], filename)
                video.save(upload_path)

                decrypted_filename = f"decrypted_{filename}"
                decrypted_path = os.path.join(app.config['PROCESSED_FOLDER_VIDEOS'], decrypted_filename)

                # Decrypt the video
                decrypt_video(upload_path, decryption_key.encode(), decrypted_path)

                # Update the decrypted video path
                current_decrypted_video = decrypted_filename

    return render_template(
        'video_cryptography.html',
        encrypted_video=current_encrypted_video,
        decrypted_video=current_decrypted_video
    )


if __name__ == '__main__':
    app.run(debug=True)

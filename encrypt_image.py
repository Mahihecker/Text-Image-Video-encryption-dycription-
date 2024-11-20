import numpy as np
from PIL import Image
from Crypto.Cipher import ARC4

def encrypt_image(image_path, key, output_path):
    """
    Encrypt an image using RC4.
    :param image_path: Path to the input image
    :param key: Encryption key
    :param output_path: Path to save the encrypted image
    """
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Flatten the image array into bytes
    img_bytes = img_array.tobytes()

    # Encrypt the bytes using RC4
    cipher = ARC4.new(key)
    encrypted_bytes = cipher.encrypt(img_bytes)

    # Convert encrypted bytes back to array
    encrypted_array = np.frombuffer(encrypted_bytes, dtype=img_array.dtype).reshape(img_array.shape)

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

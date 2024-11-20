import numpy as np
from PIL import Image
from Crypto.Cipher import ARC4

def decrypt_image(encrypted_image_path, key, output_path):
    """
    Decrypt an RC4-encrypted image.
    :param encrypted_image_path: Path to the encrypted image
    :param key: Decryption key (same as encryption key)
    :param output_path: Path to save the decrypted image
    """
    # Load the encrypted image
    img = Image.open(encrypted_image_path)
    img_array = np.array(img)

    # Flatten the image array into bytes
    encrypted_bytes = img_array.tobytes()

    # Decrypt the bytes using RC4
    cipher = ARC4.new(key)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # Convert decrypted bytes back to array
    decrypted_array = np.frombuffer(decrypted_bytes, dtype=img_array.dtype).reshape(img_array.shape)

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

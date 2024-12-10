import numpy as np
from PIL import Image

class RC4:
    def __init__(self, key):
        if not key:
            raise ValueError("Key cannot be empty")

        # Ensure the key is a string, and encode it to bytes if necessary
        if isinstance(key, bytes):
            key = key.decode()  # Convert bytes to string
        self.keygenerator = self.PRGA_YIELD(self.KSA(list(key.encode())))

    def KSA(self, key):
        """
        Key Scheduling Algorithm (KSA).
        :param key: Key as a list of bytes.
        :return: Scrambled state array S.
        """
        s = list(range(256))  # Initialize state array S with 0 to 255
        j = 0
        for i in range(256):
            j = (j + s[i] + key[i % len(key)]) % 256
            s[i], s[j] = s[j], s[i]  # Swap values in S
        return s

    def PRGA_YIELD(self, S):
        """
        Pseudo-Random Generation Algorithm (PRGA).
        :param S: Scrambled state array S from KSA.
        :yield: Next byte of the keystream.
        """
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # Swap values in S
            yield S[(S[i] + S[j]) % 256]

import numpy as np
from PIL import Image

def encrypt_image(image_path, key, output_path):
    """
    Encrypt an image using RC4.
    :param image_path: Path to the input image
    :param key: Encryption key (string or bytes)
    :param output_path: Path to save the encrypted image
    """
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Flatten the image array into bytes
    img_bytes = img_array.tobytes()

    # Encrypt the bytes using the RC4 class
    rc4_cipher = RC4(key)
    keystream = (next(rc4_cipher.keygenerator) for _ in range(len(img_bytes)))#for total bytes in flattened image array,create that much number of keystreams but one by one in a loop
    encrypted_bytes = bytes([b ^ k for b, k in zip(img_bytes, keystream)])#xor

    # Convert encrypted bytes back to array
    encrypted_array = np.frombuffer(encrypted_bytes, dtype=img_array.dtype).reshape(img_array.shape)

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

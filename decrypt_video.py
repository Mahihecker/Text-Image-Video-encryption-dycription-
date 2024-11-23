def decrypt_video(encrypted_video_path, key, output_path):
    """
    Decrypt a video file using a simple logic (e.g., XOR or RC4).
    Replace this with real decryption logic.
    """
    with open(encrypted_video_path, 'rb') as f:
        encrypted_data = f.read()

    # Dummy decryption (XOR with key)
    decrypted_data = bytearray([b ^ key[0] for b in encrypted_data])

    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"Decrypted video saved to {output_path}")

def encrypt_video(input_path, key, output_path):
    """
    Encrypt a video file using a simple logic (e.g., XOR or RC4).
    Replace this with real encryption logic.
    """
    with open(input_path, 'rb') as f:
        video_data = f.read()

    # Dummy encryption (e.g., XOR with the first byte of the key)
    encrypted_data = bytearray([b ^ key[0] for b in video_data])

    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

    print(f"Encrypted video saved to {output_path}")

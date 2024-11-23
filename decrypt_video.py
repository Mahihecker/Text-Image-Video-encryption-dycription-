import cv2
import numpy as np

class RC4:
    def __init__(self, key):
        if not key:
            raise ValueError("Key cannot be empty")
        if isinstance(key, bytes):
            key = key.decode()  # Convert bytes to string if needed
        self.keygenerator = self.PRGA_YIELD(self.KSA(list(key.encode())))

    def KSA(self, key):
        s = list(range(256))
        j = 0
        for i in range(256):
            j = (j + s[i] + key[i % len(key)]) % 256
            s[i], s[j] = s[j], s[i]
        return s

    def PRGA_YIELD(self, S):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            yield S[(S[i] + S[j]) % 256]

def decrypt_video(encrypted_video_path, key, output_video_path):
    """
    Decrypt a video encrypted frame-by-frame.
    """
    video = cv2.VideoCapture(encrypted_video_path)

    # Get video properties
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 output

    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    rc4_cipher = RC4(key)  # Initialize RC4 with the provided key

    while video.isOpened():
        ret, frame = video.read()  # Read the next frame
        if not ret:
            break

        # Flatten the frame into bytes
        frame_bytes = frame.tobytes()

        # Decrypt the pixel data
        keystream = (next(rc4_cipher.keygenerator) for _ in range(len(frame_bytes)))
        decrypted_bytes = bytes([b ^ k for b, k in zip(frame_bytes, keystream)])

        # Convert decrypted bytes back to a frame
        decrypted_frame = np.frombuffer(decrypted_bytes, dtype=frame.dtype).reshape(frame.shape)

        # Write the decrypted frame back to the video
        out.write(decrypted_frame)

    # Release resources
    video.release()
    out.release()
    print(f"Decrypted video saved to {output_video_path}")

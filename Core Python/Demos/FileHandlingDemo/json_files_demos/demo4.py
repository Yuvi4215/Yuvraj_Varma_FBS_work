from Crypto.Cipher import AES
import base64

class SimpleEncryptor:
    def __init__(self, key: bytes):
        # AES key must be 16, 24, or 32 bytes long
        self.key = key.ljust(32, b'\0')[:32]  # pad/truncate key

    def encrypt(self, text: str) -> str:
        cipher = AES.new(self.key, AES.MODE_ECB)
        # pad text to multiple of 16 bytes
        pad = 16 - len(text) % 16
        text += chr(pad) * pad
        encrypted = cipher.encrypt(text.encode())
        return base64.urlsafe_b64encode(encrypted).decode()

    def decrypt(self, token: str) -> str:
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted = cipher.decrypt(base64.urlsafe_b64decode(token))
        pad = decrypted[-1]
        return decrypted[:-pad].decode()
    
if __name__ == "__main__":
    e = SimpleEncryptor(b"mysecretkey12345")  # must be bytes!
    print(e.encrypt("Sample text for text"))

    print(e.decrypt("kmjvPZBB-ivAjnXX3k41M0Zztlt9keEBHFu1D8OSL1g="))


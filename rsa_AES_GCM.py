import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from generar_claves import generar_par_claves


def encrypt_document(document: bytes, recipient_public_key_pem: bytes) -> bytes:
    aes_key = os.urandom(32)
    cipher_aes = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher_aes.encrypt_and_digest(document)
    
    recipient_key = RSA.import_key(recipient_public_key_pem)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_aes_key = cipher_rsa.encrypt(aes_key)
    
    return enc_aes_key + cipher_aes.nonce + tag + ciphertext

def decrypt_document(pkg: bytes, recipient_private_key_pem: bytes) -> bytes:
    private_key = RSA.import_key(recipient_private_key_pem, passphrase="lab04uvg")
    
    enc_aes_key = pkg[:private_key.size_in_bytes()]
    nonce = pkg[private_key.size_in_bytes():private_key.size_in_bytes()+16]
    tag = pkg[private_key.size_in_bytes()+16:private_key.size_in_bytes()+32]
    ciphertext = pkg[private_key.size_in_bytes()+32:]
    
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(enc_aes_key)
    
    cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    return cipher_aes.decrypt_and_verify(ciphertext, tag)

if __name__ == '__main__':
    generar_par_claves(2048)

    with open("public_key.pem", "rb") as f: pub = f.read()
    with open("private_key.pem", "rb") as f: priv = f.read()

    # Generen un cifrado de un texto
    doc = b"Contrato de confidencialidad No. 2025-GT-001"
    pkg = encrypt_document(doc, pub)
    resultado = decrypt_document(pkg, priv)
    print(f"Descifrado texto corto: {resultado.decode()}")

    # Prueba con archivo de 1 MB (simula un contrato real)
    doc_grande = os.urandom(1024 * 1024)
    pkg2 = encrypt_document(doc_grande, pub)
    assert decrypt_document(pkg2, priv) == doc_grande
    print("Archivo 1 MB: OK")

from Crypto.PublicKey import RSA

def generar_par_claves(bits: int = 3072):
    # Generar el par de claves RSA
    print(f"Generando par de claves RSA de {bits} bits (esto puede tomar unos segundos)...")
    key = RSA.generate(bits)
    
    # Exportar clave privada protegida con passphrase
    private_key = key.export_key(passphrase="lab04uvg", pkcs=8, protection="scryptAndAES128-CBC")
    with open("private_key.pem", "wb") as f:
        f.write(private_key)
        
    # Exportar clave pública sin protección
    public_key = key.publickey().export_key()
    with open("public_key.pem", "wb") as f:
        f.write(public_key)

if __name__ == '__main__':
    generar_par_claves(3072)
    print("Claves generadas: private_key.pem y public_key.pem")
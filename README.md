# Plataforma de Transferencia de Documentos Legales (RSA y Cifrado Híbrido)

## Descripción del Proyecto
Este proyecto implementa un sistema seguro de transferencia de documentos confidenciales (contratos, acuerdos, datos personales) entre oficinas (Guatemala City, Miami y Madrid) para una firma de abogados. 

El sistema utiliza **criptografía híbrida**, combinando la seguridad asimétrica de RSA (con padding OAEP) para la transferencia segura de claves y la eficiencia simétrica de AES (con modo GCM) para cifrar los documentos largos. El proyecto forma parte del Laboratorio de Cifrado y permite demostrar el funcionamiento de estas tecnologías y el impacto del padding correcto.

## Requisitos e Instalación
El proyecto está implementado en **Python 3**.
Para ejecutar los scripts, asegúrate de tener instalada la librería criptográfica `pycryptodome`:

```sh
pip install pycryptodome
```

## Ejemplos de Ejecución y Uso

### 1. Generación de Claves (Paso Actual)
Ejecuta el script de generación de claves para crear un par RSA de 3072 bits. Esto creará los archivos correspondientes a las llaves criptográficas:

```sh
python3 generar_claves.py
```
> **Nota:** La clave privada generada (`private_key.pem`) está protegida mediante una frase de contraseña ("lab04uvg") como requerimiento de seguridad.

---

## Respuestas a las Preguntas de Análisis (En progreso)

### 1. ¿Por qué no cifrar el documento directamente con RSA?
RSA es un algoritmo asimétrico y realizar operaciones matemáticas con llaves grandes es computacionalmente lento comparado con algoritmos simétricos (como AES). Además, RSA tiene un límite estricto sobre la cantidad de datos que puede cifrar, que es proporcional al tamaño de su llave. Por eso, el enfoque correcto (el cifrado híbrido) consiste en usar el rápido AES para cifrar el documento largo y usar el costoso RSA únicamente para cifrar y compartir la llave de AES.

### 2. ¿Qué información contiene un archivo .pem y cómo es la estructura de `public_key.pem`?
El formato `.pem` (Privacy-Enhanced Mail) es una forma estándar codificada en Base64 para almacenar certificados digitales o claves criptográficas, lo que facilita copiarlas, pegarlas y transmitirlas en texto plano. 
Si abres `public_key.pem`, la estructura es así:
1. Inicia con un encabezado exacto: `-----BEGIN PUBLIC KEY-----`
2. Luego tiene texto codificado en Base64 que contiene la información esencial para la clave pública (modulus y public exponent).
3. Termina con: `-----END PUBLIC KEY-----`

---
*(Instrucciones de los pasos 2, 3 y 4 se agregarán conforme se avance en el proyecto)*

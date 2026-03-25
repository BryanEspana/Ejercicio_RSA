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

### 1. Generación de Claves

Ejecuta el script de generación de claves para crear un par RSA de 3072 bits:

```sh
python3 generar_claves.py
```

### 2. Cifrado Directo con RSA-OAEP

Prueba el cifrado asimétrico directo y la demostración de padding:

```sh
python3 rsa_OAEP.py
```

### 3. Cifrado Híbrido (RSA + AES-GCM)

Ejecuta la implementación principal para documentos de gran tamaño:

```sh
python3 rsa_AES_GCM.py
```

---

## Respuestas a las Preguntas de Análisis

### 1. ¿Por qué no cifrar el documento directamente con RSA?

RSA es un algoritmo asimétrico y realizar operaciones matemáticas con llaves grandes es computacionalmente lento comparado con algoritmos simétricos (como AES). Además, RSA tiene un límite estricto sobre la cantidad de datos que puede cifrar, que es proporcional al tamaño de su llave. Por eso, el enfoque correcto (el cifrado híbrido) consiste en usar el rápido AES para cifrar el documento largo y usar el costoso RSA únicamente para cifrar y compartir la llave de AES.

### 2. ¿Qué información contiene un archivo .pem y cómo es la estructura de `public_key.pem`?

El formato `.pem` (Privacy-Enhanced Mail) es una forma estándar codificada en Base64 para almacenar certificados digitales o claves criptográficas.

Estructura de `public_key.pem`:

1. Encabezado: `-----BEGIN PUBLIC KEY-----`
2. Datos Base64: Información de la clave (modulus y public exponent).
3. Pie: `-----END PUBLIC KEY-----`

### 3. ¿Por qué cifrar el mismo mensaje dos veces produce resultados distintos?

Esto ocurre debido a que RSA-OAEP es un esquema de cifrado **probabilístico**. OAEP (Optimal Asymmetric Encryption Padding) introduce aleatoriedad (un "seed" aleatorio) antes de realizar la operación de RSA.

**Propiedad de OAEP:** El padding transforma el mensaje determinista en uno aleatorio antes de cifrar, lo que evita que un atacante pueda adivinar el contenido mediante ataques de texto claro escogido (indistinguibilidad).

### 4. Identificación de vulnerabilidades: PKCS#1 v1.5 vs OAEP

OAEP es superior a PKCS#1 v1.5 porque incluye pruebas de seguridad contra ataques de texto cifrado escogido (Padding Oracle Attacks). Mientras que v1.5 es determinista en ciertos aspectos y vulnerable si el receptor revela errores de padding, OAEP utiliza funciones de hash para asegurar la integridad de la estructura del relleno.

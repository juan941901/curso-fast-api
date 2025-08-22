# Curso FastApi

## Clase 1 - Configuración de entorno de trabajo

Para instalar fastapi usamos el comando 

```python

pip3 install fastapi[standard]

```

Ya con fastapi instalado, y creado nuestro archivo `main.py` ejecutamos el comando

```python

fastapidev

```

esto ejecutara el proyecto

---

## Clase 2 - Creaciónde de Endpoints GET

para crear endpoint en fastapi declaramos una función asincrona y le agregamos el decorador `@app.get`, con esto estamos creando un endpoint de tipo get para que reciba nuestras solicitudes.

Para definir el nombre del endpoint lo escribimos dentro de los paretencis de nuestro decorador, así indicamos la ruta para acceder a ese segmento de código.

Ahora para poder recibir valores en nuestro endpoint de tipo get, lo que hacemos es colocar un `/` luego del nombre del endpoint y entre llaves `{}` con el nombre de la variable y luego esta misma la pasamos como variable de entrada en nuestra función.

dependiendo el tipo de dato que estemos pasando a nuestra función es recomendable definirle su tipo de dato esto con el fin de poder aplicar funciones internas de python

---

## Clase 2 - Creaciónde de Endpoints POST y validacion de errores

Para crear el end de tipo `POST` agregamos en nuestrp decorador la palabra `post`, y haciendo uso de `pydantic` podemos crear modelos(json) que recibira el endpoint.

adicionalmente al tipar nuestro tipo de datos en nuestro basemodel, nos permite que si viene un valor errado al indicado este genere la excepción

---


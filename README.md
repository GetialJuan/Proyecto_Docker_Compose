# Proyecto Docker Compose

En el archivo [app/app.py](app/app.py) se encuentra una simple aplicación con 4 endpoints para realizar operaciones básicas sobre un contador: obtenerlo, asignarle un valor específico (por JSON o por URL), y eliminarlo.

### Acceso a los servicios ofrecidos por el "API" desde el CLI

- Validar si el servicio está arriba:

```
curl -i http://localhost:8000
```

- Consultar el valor del contador:

```
curl http://localhost:8000
```

- Asignar el contador a un valor particular por medio de la URL:

```
curl -X PUT http://localhost:8000/value
```

Donde value es el valor a asignar al contador. (Ej: curl -X POST http://localhost:8000/4)

- Asignar el contador a un valor particular con un JSON:

```
curl -H "Content-Type: application/json" -X POST -d '{"counter": value}' http://localhost:8000/
```

Donde value es el valor a asignar al contador. (Ej: ... -d '{"counter": 5}' ...)

- Eliminar el valor del contador (retornarlo a 0):

```
curl -X DELETE http://localhost:8000
```

### Gestión de contenedores

- Para detener la ejecución de los contenedores con borrado de los mismos

```
docker-compose down --rmi all
```

- Para forzar la construcción de la imagen que se usa en la aplicación sin considerar lo que está en *cache*

```
docker-compose build --no-cache --no-rm
```

README.md basado en el del profesor John Sanabria en https://github.com/johnsanabria/gtd-flask

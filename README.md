# Blaise REST Api python client

This library facilitates calling the Blaise REST Api in python services. To use
the library you need to do the following:

### Creating new endpoints

Add new endpoints and tests as required.

Run tests:
```
poetry run python -m pytest
```

Git add, commit and push ensuring you've added the build files.

### Consuming

Add a dependency to poetry:
```
blaise-restapi = {git = "https://github.com/ONSdigital/blaise-api-python-client.git", rev = "main"}
```

Add an import statement where you wish to consume the client:
```
import blaise_restapi
```

Declare and consume the client by passing the URL of the rest api:
```
restapi_client = blaise_restapi.Client(f"http://{url}")
```
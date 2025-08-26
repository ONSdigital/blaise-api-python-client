# Blaise REST API Python Client

A Python client for interacting with our Blaise REST API. It provides a convenient wrapper for making requests to Blaise from Python applications.

## Usage

Add the dependency to your project using Poetry, for stability, install from a published GitHub release tag:

```
poetry add git+https://github.com/ONSdigital/blaise-api-python-client.git@v1.0.2
```

Import the client and create an instance by passing in the REST API URL:

```
import blaise_restapi

restapi_client = blaise_restapi.Client("http://restapi-url")

# Example usage
cases = restapi_client.get_cases("server_park", "questionnaire_name")
```

## Running Development Tasks

This project includes a `Makefile` with common development commands.

-   **Format:**
    Formats the code.
    ```bash
    make format
    ```

-   **Lint:**
    Checks code quality.
    ```bash
    make lint
    ```

-   **Test:**
    Executes test suite.
    ```bash
    make test
    ```
# Blaise REST API Python Client

A Python client for interacting with our Blaise REST API. It provides a convenient wrapper for making requests to Blaise from Python applications. This repository provides the client library; it does not run or deploy the REST API.

## Repository Layout

- `blaise_restapi/client.py` contains the REST API client.
- `blaise_restapi/functions/` contains questionnaire helpers.
- `tests/` contains tests using mocked HTTP responses.

## Usage

1. Add the package to your project using Poetry, using a published GitHub release tag for stability:

   ```bash
   poetry add git+https://github.com/ONSdigital/blaise-api-python-client.git@v1.0.3
   ```

2. Import the client and create an instance by passing in the REST API URL:

   ```python
    import blaise_restapi

    restapi_client = blaise_restapi.Client("http://restapi-url")

    # Example usage
    cases = restapi_client.get_cases("server_park", "questionnaire_name")
   ```

## Development Setup

1. Install Python 3.13 and Poetry.
1. Run `poetry install` to install the project and development dependencies.

## Linting

- Run `make lint` to check linting and formatting.
- Run `make lint-fix` to apply auto-fixes and formatting.

## Type Checking

- Run `make typecheck` to run Pyright in strict mode.

## Dependency and Dead-Code Checks

- Run `make deptry` to check dependencies.
- Run `make vulture` to check for unused code.

## Testing

- Run `make test` to run tests and report coverage.

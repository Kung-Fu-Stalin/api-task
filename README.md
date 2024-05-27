# API tests

## Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Kung-Fu-Stalin/api-task.git
    cd api-task
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Set the `PYTHONPATH` from the local directory:

    - On Windows:

        ```sh
        set PYTHONPATH=%PYTHONPATH%;%cd%
        ```

    - On macOS and Linux:

        ```sh
        export PYTHONPATH="${PYTHONPATH}:$(pwd)"
        ```

## Usage

Now you can run tests. For example:

```sh
pytest -s tests/test_facts_endpoint.py
```
All tests configuration is avaiable in `config/config.yaml`. Reports after tests execution are available in `reports/report.html` (Generated automatically after test execution). 

## Overview

This repository contains a suite of tests for validating the `/facts` endpoint of an API. The tests are written by `pytest` and cover various scenarios to ensure the reliability and correctness of the API responses. The tests validate fetching random cat facts, retrieving a specific fact by ID, handling different animal types, and checking correct and incorrect amounts of facts.

## Test Cases

There is a table summarizing the test cases included in the suite:

| Test Case Name | Description | Validation Used | Reason for Validation |
| -------------- | ----------- | ----------------| --------------------- |
| `test_fetch_random_cat_fact` | Sends a request to get a random cat fact | - Check if status code is 200 <br> - Check 'text' in response <br> - Check 'text' is a non-empty string | Ensure the endpoint returns a successful response with a valid fact |
| `test_get_fact_by_id` | Retrieves a specific fact by ID | - Check if status code is 200 <br> - Check `_id` matches the expected ID <br> - Check `text` matches the expected content | Validate the endpoint correctly fetches the fact by ID and returns the correct content |
| `test_animal_type` | Sends a request to get a fact for a specific animal type | - Check if status code is 200 <br> - Check 'type' in response <br> - Check 'type' matches the requested animal type | Ensure the endpoint returns the correct type of fact for different animals |
| `test_correct_amount` | Sends a request to get a specific number of facts | - Check if status code is 200 <br> - Check response length matches the requested amount | Verify the endpoint returns the correct number of facts |
| `test_incorrect_amount` | Tests various invalid amounts to check error handling | - Check if status code matches the expected code <br> - Check response payload matches the expected payload | Ensure the endpoint handles invalid amounts gracefully and returns appropriate error messages |

## Validation Details

### `test_fetch_random_cat_fact`
- **Validation**: Status code 200, 'text' in response, 'text' is a non-empty string.
- **Reason**: Ensures the endpoint is functional and returns a valid cat fact.

### `test_get_fact_by_id`
- **Validation**: Status code 200, `_id` matches expected ID, `text` matches expected content.
- **Reason**: Confirms that fetching a fact by ID returns the correct data.

### `test_animal_type`
- **Validation**: Status code 200, 'type' in response, 'type' matches requested animal type.
- **Reason**: Validates the endpoint's ability to return facts for different animal types.

### `test_correct_amount`
- **Validation**: Status code 200, response length matches requested amount.
- **Reason**: Ensures the endpoint can handle requests for multiple facts and returns the correct number of items.

### `test_incorrect_amount`
- **Validation**: Status code matches expected code, response payload matches expected payload.
- **Reason**: Checks that the endpoint correctly handles and returns errors for invalid request parameters.

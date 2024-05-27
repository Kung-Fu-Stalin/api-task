import pytest

from utils import get_logger


logger = get_logger(__name__)


class TestSuiteFactsEndpoint:

    ENDPOINT = "/facts"

    def test_fetch_random_cat_fact(self, api_session):
        method = "GET"

        logger.info("Send request to get random cat fact")
        response = api_session.request(
            method=method,
            endpoint=f"{self.ENDPOINT}/random"
        )
        assert response.status_code == 200, "Expected status code 200"

        response_json = response.json()

        assert 'text' in response_json, \
            "Expected 'text' in response"
        assert isinstance(response_json['text'], str), \
            "Expected 'fact' to be a string"
        assert len(response_json['text']) > 0, \
            "Expected 'fact' to be non-empty"

    def test_get_fact_by_id(self, api_session):
        method = "GET"
        fact_id = "591f98803b90f7150a19c229"
        ex_text = ("In an average year, cat owners in the "
                   "United States spend over $2 billion on cat food.")

        logger.info(f"Get fact by id: {fact_id}")
        response = api_session.request(
            method=method,
            endpoint=f"{self.ENDPOINT}/{fact_id}"
        )
        assert response.status_code == 200, \
            "Unexpected status code"

        response_json = response.json()

        assert response_json.get("_id") == fact_id, \
            f"Incorrect fact id. Expected: {fact_id}"
        assert response_json.get("text") == ex_text, \
            "Incorrect fact content"

    @pytest.mark.parametrize("animal_type", ["cat", "dog", "horse"])
    def test_animal_type(self, api_session, animal_type):
        method = "GET"
        params = {
            "animal_type": animal_type
        }

        logger.info(f"Send request to get data for: {animal_type} animal_type")
        response = api_session.request(
            method=method,
            endpoint=f"{self.ENDPOINT}/random",
            params=params
        )

        assert response.status_code == 200, \
            "Unexpected status code"

        response_json = response.json()

        assert response_json.get("type"), \
            "Key 'Type' is not found in response"
        assert response_json["type"] == animal_type, \
            f"Incorrect animal type, expected: {animal_type}"
        
    @pytest.mark.parametrize("amount", [2, 4, 54, 100, 200, 500])
    def test_correct_amount(self, api_session, amount):
        method = "GET"
        params = {
            "amount": amount
        }

        logger.info(f"Send request to get {amount} fact about cats")
        response = api_session.request(
            method=method,
            endpoint=f"{self.ENDPOINT}/random",
            params=params
        )
        assert response.status_code == 200, \
            "Unexpected status code"

        response_json = response.json()

        assert len(response_json) == amount, \
            f"Incorrect facts amount. Expected: {amount}"

    @pytest.mark.parametrize("test_params",
        [
            (-1, 200, []),
            (1200, 405, {"message": "Limited to 500 facts at a time"}),
            (501, 405, {"message": "Limited to 500 facts at a time"}),
            ("NaN", 200, []),
            (-3000, 200, []),
            (0, 200, [])
        ]
    )
    def test_incorrect_amount(self, api_session, test_params):
        incorrect_amount, ex_code, ex_payload = test_params
        method = "GET"
        params = {
            "amount": incorrect_amount
        }

        logger.info(
            f"Send request to get fact with incorrect amount value: {incorrect_amount}"
        )
        response = api_session.request(
            method=method,
            endpoint=f"{self.ENDPOINT}/random",
            params=params
        )

        assert response.status_code == ex_code, \
            f"Unexpected status code. Expected: {ex_code}"
        assert response.json() == ex_payload, \
            f"Incorrect response payload. Expected: {ex_payload}"

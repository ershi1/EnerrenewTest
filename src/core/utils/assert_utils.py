# utils/assert_utils.py
def validate_response(response, expected_status=200, schema=None):
    assert response.status_code == expected_status, \
        f"Expected status {expected_status}, got {response.status_code}"

    if schema:
        validate(instance=response.json(), schema=load_schema(schema))

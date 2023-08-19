import pytest

from tests.conftest import client

from fastapi import status


def test_random_passwords():
    response = client.get(
        "pass/random_passwords",
        params={
            "length": 10,
            "uppercase_chars": True,
            "digits": True,
            "special_chars": True,
            "hard_mode": True
        }
    )
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 5

# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401


def test_fake_query_param_default(client: TestClient):
    """Test case for fake_query_param_default

    test query parameter default value
    """
    params = [("has_default", 'Hello World'),     ("no_default", 'no_default_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/fake/query_param_default",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


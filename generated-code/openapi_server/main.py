# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from service.fake_api import router as FakeApiRouter
from service.pet_api import router as PetApiRouter
from service.store_api import router as StoreApiRouter
from service.user_api import router as UserApiRouter

app = FastAPI(
    title="OpenAPI Petstore",
    description="This is a sample server Petstore server. For this sample, you can use the api key &#x60;special-key&#x60; to test the authorization filters.",
    version="1.0.0",
)

app.include_router(FakeApiRouter)
app.include_router(PetApiRouter)
app.include_router(StoreApiRouter)
app.include_router(UserApiRouter)

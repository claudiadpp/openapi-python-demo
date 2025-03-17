# openapi_client.FakeApi

All URIs are relative to *http://petstore.swagger.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fake_query_param_default**](FakeApi.md#fake_query_param_default) | **GET** /fake/query_param_default | test query parameter default value


# **fake_query_param_default**
> fake_query_param_default(has_default=has_default, no_default=no_default)

test query parameter default value



### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://petstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://petstore.swagger.io/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FakeApi(api_client)
    has_default = 'Hello World' # str | has default value (optional) (default to 'Hello World')
    no_default = 'no_default_example' # str | no default value (optional)

    try:
        # test query parameter default value
        api_instance.fake_query_param_default(has_default=has_default, no_default=no_default)
    except Exception as e:
        print("Exception when calling FakeApi->fake_query_param_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **has_default** | **str**| has default value | [optional] [default to &#39;Hello World&#39;]
 **no_default** | **str**| no default value | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid username supplied |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


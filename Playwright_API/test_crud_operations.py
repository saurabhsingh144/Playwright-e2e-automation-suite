import json
from http import cookies

import playwright
import pytest
from pip._internal.network import auth
from playwright.sync_api import Playwright



base_url="https://restful-booker.herokuapp.com"


token=""
booking_id=""
# utility to read data
def read_json(filepath):
    with open(filepath,"r") as json_file:
        data = json.load(json_file)
        return data

# Fixture to create playwright request
@pytest.fixture(scope="session")
def request_context(playwright: Playwright):
    context=playwright.request.new_context()
    yield context
    context.dispose()

@pytest.fixture(scope="function")
def test_create_booking(request_context):
     data=read_json("testdata/post_request.json")
     response=request_context.post(f"{base_url}/booking",data=data)
     response_body=response.json()
     assert response.ok ,"POST request failed"
     assert response.status == 200
     assert "bookingid" in response_body
     assert "booking" in response_body
     assert response_body["booking"]["firstname"] == data["firstname"]
     assert response_body["booking"]["lastname"] == data["lastname"]
     # global booking_id
     # booking_id=response_body["bookingid"]
     return response.json()["bookingid"]



def test_get_booking_details(request_context):
     # data=read_json("testdata/post_request.json")
      response=request_context.get(f"{base_url}/booking/{booking_id}")
      response_body=response.json()
      print(response_body)
      assert response.ok ,"GET request failed"
      assert response.status == 200


def test_get_booking_by_name(request_context):
    name_params={"firstname":"Jim","lastname":"Brown"}
    response=request_context.get(f"{base_url}/booking",params=name_params)
    response_body=response.json()
    print(f"Booking IDs fetched by names{name_params}",response_body)
    assert len(response_body)>0

def test_get_by_dates(request_context):
    data_params={"checkin":"2026-05-12","checkout":"2026-05-14"}
    response=request_context.get(f"{base_url}/booking",params=data_params)
    response_body=response.json()
    print(f"Booking IDs fetched by dates{data_params}",response_body)

@pytest.fixture(scope="session")
def test_create_token(request_context):
    data=read_json("testdata/get_token.json")
    print(data)
    response=request_context.post(f"{base_url}/auth",data=data)
    response_body=response.json()
    assert response.ok ,"GET request failed"
    assert "token" in response_body
    # global token
    return response_body["token"]
    assert len(token)>5
def test_partial_update_token(request_context,test_create_token,test_create_booking):
    data=read_json("testdata/partial_update_token.json")
    response=request_context.patch(f"{base_url}/booking/{test_create_booking}",
                                   data=data,
                                   headers={"Cookie":f"token={test_create_token}"})
    response_body=response.json()
    print(response_body)
    assert response.ok ,"PATCH request failed"
    assert response.status==200












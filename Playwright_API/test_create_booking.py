
from playwright.sync_api import  Playwright ,expect


def test_create_booking(playwright: Playwright):
    base_url="https://restful-booker.herokuapp.com"
    request_context=playwright.request.new_context()
    request_body={
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates":
            {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"

    }
    response=request_context.post(f"{base_url}/booking",data=request_body)
    response_body=response.json()
    print(response_body)

    assert  response.ok
    assert  response.status == 200
    assert "bookingid" in response_body
    assert "booking" in response_body
    assert response_body["booking"]["firstname"] == "Jim"
    assert response_body["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert response_body["booking"]["bookingdates"]["checkout"] == "2019-01-01"


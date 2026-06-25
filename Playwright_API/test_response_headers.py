from playwright.sync_api import Playwright
from Playwright_API.test_crud_operations import request_context
def test_header_response(request_context):
   response= request_context.get("https://www.google.com/")
   assert response.ok
   assert response.status_text=="OK"

#    Extract Headers
   headers=response.headers
   for key ,value in headers.items():
    print(key,value)

    assert "text/html" in headers.get("content-type")
    assert "gzip" in headers.get("content-encoding")
    assert "gzip" == headers.get("content-encoding")


#     Validate specific header presence
    assert "Server" in headers
    assert "set-cookie" in headers

def test_cookies(request_context):
    response= request_context.get("https://www.google.com/")
    # Extract cookies from the response
    cookies=request_context.storage_state()["cookies"]
    aec_cookies=None
    for c in cookies:
        if c['name']=="AEC":
            aec_cookies=c
    assert aec_cookies is not None

    # assert "AEC" in cookies











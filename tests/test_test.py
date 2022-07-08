from framework.api.api_requests import MyRequests


def test_api_requests():
    response = MyRequests.get(url="hello")
    print(response.json())
    print("Message for test merge conflict")

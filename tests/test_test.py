from framework.api.api_requests import MyRequests


def test_api_requests():
    response = MyRequests.get(url="hello")
    print(response.json())
    print("actual message: this is true!!!!")

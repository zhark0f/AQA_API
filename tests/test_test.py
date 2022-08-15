import allure

from framework.api.api_requests import MyRequests


@allure.description("Test_test")
def test_api_requests():
    response = MyRequests.get(url="hello")
    print(response.json())
    print("actual message: this is true!!!!")

@allure.description("Test_test_2")
def test_2():
    assert True

@allure.description("Test_test_3")
def test_3():
    assert False
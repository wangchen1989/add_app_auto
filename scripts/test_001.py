import allure, pytest

class Test:
    @allure.step(title="这是第一条测试用例")
    def test_001(self):
        with open("./添加图片到测试报告.png", "rb") as f:
            allure.attach("图片", f.read(), allure.attach_type.PNG)
        print("Niha")

# @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
# @allure.step(title="这是第二条测试用例")
# def test_002():
#     allure.attach("登录", "不输的账户")
#     print("大风a")
#
# @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @allure.step(title="这是第一条测试用例")
# def test_003():
#     allure.attach("登录", "错的账户")
#     print("心情不美丽")

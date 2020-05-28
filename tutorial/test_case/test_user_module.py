from api.UserModule import UserModule
import uuid
import allure


class TestUserModule(object):

    @classmethod
    def setup_class(cls):
        cls.username = str(uuid.uuid1())
        cls.password = str(uuid.uuid1())
        cls.modify_password = str(uuid.uuid1())
        cls.user_module = UserModule()

    def test_register(self):
        response = self.user_module.register(self.username, self.password)

        print(response)
        assert response.status_code == 200
        assert 'id' in response.json().keys()

    def test_login(self):
        self.user_module.register(self.username, self.password)

        response = self.user_module.login(self.username, self.password)

        assert response.status_code == 200
        assert 'access_token' in response.json().keys()

    def test_modify_password(self):
        # 先注册
        self.user_module.register(self.username, self.password)

        # 完成登录
        self.user_module.login(self.username, self.password)

        # 再修改密码
        self.user_module.modify_password(self.username, self.modify_password)

        # 修改后的密码实现登录
        response = self.user_module.login(self.username, self.modify_password)

        # 断言部分
        assert response.status_code == 200
        assert 'access_token' in response.json().keys()

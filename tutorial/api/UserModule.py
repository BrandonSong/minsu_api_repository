import requests
import uuid


class UserModule(object):

    Headers = {
        "Authorization": "Basic cm9vdDpsbmhoM3k5N2t4YXo5ejl1eGFtODV2bDM2YjFuMTJldg=="
    }

    def register(self, username, password):
        """ 封装登录接口 """
        response = requests.post("http://pmtest.wul.ai/pm/admin/register",
                                 json={
                                    "username": username,
                                    "password": password,
                                    "roles": ["homestay-user"]
                                 },
                                 headers=self.Headers
                                )

        return response

    def login(self, username, password):
        response = requests.post("http://pmtest.wul.ai/pm/admin/login",
                                 json={
                                     "username": username,
                                     "password": password
                                 },
                                 headers=self.Headers)
        return response

    def modify_password(self, username, password):
        response = requests.post("http://pmtest.wul.ai/pm/admin/password",
                                 json={
                                     "username": username,
                                     "password": password
                                 },
                                 headers=self.Headers)
        return response


if __name__ == '__main__':
    login_module = UserModule()

    username = str(uuid.uuid1())
    password = str(uuid.uuid1())
    modify_password = str(uuid.uuid1())

    resp1 = login_module.register(username, password)
    print(resp1.content)

    resp2 = login_module.modify_password(username, modify_password)
    print(resp2.content)

    resp3 = login_module.login(username, modify_password)
    print(resp3.content.decode('utf-8'))


import request


# http://85.143.79.6:5001

class Api:

    def __init__(self, url, port, ssh=False):

        if port:
            self.url = f"{'https://' if enable_SSL else 'http://'}{api_url}"
            if port:
                self.url += f":{port}"

        self.url = url


    def _req(self, sub_url: str, data: typing.Dict = {}) -> requests.Response:
        json_data = self._get_json_data(data)

        resp = requests.post(
            f'{self.url}/{sub_url}',
            json=json_data,
            headers={'Content-Type': 'application/json'}
        )
        return resp

    def connect(self, login, password, token, mode):
        self._req(
            'Auth/Connected',
            data={
                'login': login,
                'password': password,
                'token': token,
                'mode': mode,
            }
        )
        self.token = token


if __name__ == '__main__':
    api = Api(url="fdfdfd", port=5000)
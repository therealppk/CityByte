class URL:
    def __init__(
        self,
        protocol: str,
        host: str,
        port: int,
        path: str = "/",
        params: dict = None,
        headers: dict = None,
    ):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.path = path

        self.params = params if params is not None else {}
        self.headers = headers if headers is not None else {}

    def _base_url(self):
        return f"{self.protocol}://{self.host}:{self.port}"

    def __str__(self):
        return f"{self._base_url()}{self.path}"

    def get_url(self, path):
        return f"{self._base_url()}{path}"

    def with_default_params(self, params=None):
        if params is None:
            params = {}

        param_dict = {}

        param_dict.update(self.params)
        param_dict.update(params)

        return param_dict

    def with_default_headers(self, headers=None):
        if headers is None:
            headers = {}

        header_dict = {}

        header_dict.update(self.headers)
        header_dict.update(headers)

        return header_dict

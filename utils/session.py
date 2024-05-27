from requests import Session


class CatSession(Session):

    def __init__(self, origin: str):
        super().__init__()
        self.origin = origin

    def request(self, method: str, endpoint: str, **kwargs):
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        url = f"{self.origin}{endpoint}"
        return super().request(
            method=method,
            url=url,
            **kwargs
        )

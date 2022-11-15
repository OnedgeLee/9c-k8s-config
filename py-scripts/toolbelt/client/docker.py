from toolbelt.client import BaseUrlSession

DOCKER_HUB_URL = "https://hub.docker.com"


class DockerClient:
    def __init__(self, namespace: str) -> None:
        self._namespace = namespace
        self._session = BaseUrlSession(DOCKER_HUB_URL)

    def check_image_exists(self, repo: str, tag: str) -> bool:
        resp = self._session.get(
            f"{DOCKER_HUB_URL}/v2/namespaces/{self._namespace}/repositories/{repo}/tags/{tag}"
        )
        return resp.status_code == 200

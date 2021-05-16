import os


class Config:
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1", 1]
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
    _ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")

    JUDGE0_URL = os.environ.get("JUDGE0_URL")

    @property
    def ALLOWED_HOSTS(self):
        if not self._ALLOWED_HOSTS:
            return []

        return self._ALLOWED_HOSTS.split(",")

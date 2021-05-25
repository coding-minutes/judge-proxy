import os


class Config:
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1", 1]
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

    JUDGE0_URL = os.environ.get("JUDGE0_URL")

    # Find better config
    LANGUAGES = [
        {"id": 49, "name": "C (GCC 8.3.0)", "editor_code": "cpp"},
        {"id": 53, "name": "C++ (GCC 8.3.0)", "editor_code": "cpp"},
        {"id": 60, "name": "Go (1.13.5)", "editor_code": "go"},
        {"id": 62, "name": "Java (OpenJDK 13.0.1)", "editor_code": "java"},
        {"id": 63, "name": "JavaScript (Node.js 12.14.0)", "editor_code": "javascript"},
        {"id": 70, "name": "Python (2.7.17)", "editor_code": "python"},
        {"id": 71, "name": "Python (3.8.1)", "editor_code": "python"},
    ]

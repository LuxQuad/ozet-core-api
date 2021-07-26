from fastapi.middleware.cors import CORSMiddleware

origins: list = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5000",

    "https://esume.me",
]


config: dict = {
    'allow_origins': origins,
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}

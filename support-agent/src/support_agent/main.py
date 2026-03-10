import fastapi


class AppFactory:
    @staticmethod
    def create_app() -> fastapi.FastAPI:
        return fastapi.FastAPI()

import os


class Config:
    def __init__(self):
        with open(".env") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                key, value = line.strip().split("=")
                os.environ[key] = value
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

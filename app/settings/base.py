from decouple import config


SERVICE_NAME = config("SERVICE_NAME")

DEBUG = config("DEBUG", default=False, cast=bool)


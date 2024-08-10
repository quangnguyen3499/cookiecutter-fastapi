from pydantic_settings import BaseSettings


class AWSConfig(BaseSettings):
    # Parameter Store
    AWS_REGION: str = ""
    AWS_SSM_ENDPOINT_URL: str = ""
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_SSM_PREFIX: str = ""

    class Config:
        env_file = "./.env"
        extra = "allow"


aws_settings = AWSConfig()

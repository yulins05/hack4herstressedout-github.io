import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    HOST: str = os.environ.get("DATABRICKS_HOST", "https://dbc-05b809de-a07b.cloud.databricks.com")
    TOKEN: str = os.environ.get("DATABRICKS_TOKEN", "dapi814cda0173629149dba4867c3d77f48b")
    WAREHOUSE_ID: str = os.environ.get("DATABRICKS_WAREHOUSE_ID", "7474654412539911")
    PORT: int = int(os.environ.get("PORT", 8050))
    DEBUG: bool = os.environ.get("FLASK_DEBUG", "False").lower() in ("true", "1")

    def validate(self):
        missing = [k for k, v in self.__dict__.items() if not v and k != "DEBUG"]
        if missing:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")

settings = Config()
settings.validate()
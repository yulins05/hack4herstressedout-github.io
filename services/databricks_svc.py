import pandas as pd
from databricks.sdk import WorkspaceClient
from config.settings import settings

class DatabricksService:
    def __init__(self):
        # Explicitly passing credentials loaded from our config object
        self.client = WorkspaceClient(
            host=settings.HOST,
            token=settings.TOKEN
        )

    def fetch_unity_catalog_table(self, table_fullname: str, limit: int = 500) -> pd.DataFrame:
        """Executes optimized statement queries against Unity Catalog via SQL Warehouse."""
        query = f"SELECT * FROM {table_fullname} LIMIT {limit}"
        
        response = self.client.statement_execution.execute_statement(
            warehouse_id=settings.WAREHOUSE_ID,
            statement=query
        )
        
        columns = [col.name for col in response.manifest.schema.columns]
        data = response.result.data_array if response.result.data_array else []
        
        return pd.DataFrame(data, columns=columns)

# Singleton instance for application-wide use
db_service = DatabricksService()
from typing import Any, Dict

FUGUE_BQ_CONF_TEMP_DATASET = "fugue.bq.temp_dataset"
FUGUE_BQ_CONF_TEMP_DATASET_DEFAULT_NAME = "FUGUE_TEMP_DATASET"
FUGUE_BQ_CONF_PROJECT = "fugue.bq.project"
FUGUE_BQ_CONF_CREDENTIALS_ENV = "fugue.bq.credentials.env"

FUGUE_BQ_DEFAULT_CONF: Dict[str, Any] = {
    FUGUE_BQ_CONF_TEMP_DATASET: FUGUE_BQ_CONF_TEMP_DATASET_DEFAULT_NAME,
}

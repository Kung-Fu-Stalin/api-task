from typing import Union
from pathlib import Path

import yaml


class Config:

    PROJECT_PATH = Path(__file__).resolve().parent.parent
    CONFIG_PATH = Path(PROJECT_PATH, "config", "config.yaml")
    REPORTS_PATH = Path(PROJECT_PATH, "reports")
    REPORTS_PATH.mkdir(parents=True, exist_ok=True)

    def __init__(self):
        self.data = self._read_data(self.CONFIG_PATH)
        self._set_attributes()

    @staticmethod
    def _read_data(config_path: Union[str, Path]) -> dict:
        with open(config_path, "r") as file:
            return yaml.safe_load(file)

    def _set_attributes(self):
        for key, value in self.data.items():
            setattr(self, key.upper(), value)


Config = Config()

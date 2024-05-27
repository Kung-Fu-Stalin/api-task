from pathlib import Path

import pytest 

from utils import Config
from utils import CatSession 
from utils import get_logger


logger = get_logger(__name__)


def pytest_configure(config):
    logger.info(f"Generating report file: {Config.REPORT_FILE}")
    html_report = Path(Config.REPORTS_PATH, Config.REPORT_FILE)
    config.option.htmlpath = html_report
    config.option.self_contained_html = True


@pytest.fixture(scope="session")
def api_session():
    logger.info(f"Create session for: {Config.URL}")
    with CatSession(Config.URL) as session:
        yield session

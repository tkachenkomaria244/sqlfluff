
from sqlfluff.core.templaters import DbtTemplateInterface
from sqlfluff.core import FluffConfig
import pytest
import os


@pytest.fixture()
def dbt_templater():
    """Returns an instance of the DbtTemplater."""
    return DbtTemplateInterface()


@pytest.fixture()
def in_dbt_project_dir():
    """A wrapper to chdir into the dbt_project fixture and back to cwd at the end of the test."""
    try:
        pre_test_dir = os.getcwd()
        os.chdir("test/fixtures/dbt_project")
        yield  # test runs here
    finally:
        os.chdir(pre_test_dir)


@pytest.fixture()
def fluff_config():
    """Returns a default FluffConfig for dbt tests."""
    return FluffConfig(
        configs={"templater": {"dbt": {"profiles_dir": "../dbt"}}}
    )

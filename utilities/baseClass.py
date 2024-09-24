import pytest
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def assert_current_url(self, string):
        assert string in self.driver.current_url


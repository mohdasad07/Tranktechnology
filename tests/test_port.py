import pytest

from pages.tport import tport

@pytest.mark.smoke
def test_port(page):
    port_obj = tport(page)
    port_obj.port_clicking()
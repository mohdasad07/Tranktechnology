

import pytest

from pages.verticals import vertical

@pytest.mark.smoke
def test_trading(page):
    trading_obj = vertical(page)
    trading_obj.trading_options_clicking()

@pytest.mark.smoke
def test_retail_ecommerce(page):
    retailcom_obj= vertical(page)
    retailcom_obj.retail_ecom_clicking()

@pytest.mark.smoke
def test_health(page):
    health_obj= vertical(page)
    health_obj.health_options_clicking()

@pytest.mark.smoke
def test_fintech(page):
    fintech_obj= vertical(page)
    fintech_obj.fintech_options_selction()



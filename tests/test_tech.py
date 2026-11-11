

import pytest

from pages.technologies import technology

@pytest.mark.smoke
def test_technology(page):
    ecomm_obj = technology(page)
    ecomm_obj.ecomm_options_clicking()

@pytest.mark.smoke
def test_mobapp(page):
    mobapp_obj= technology(page)
    mobapp_obj.mobapp_options_clicking()


@pytest.mark.smoke
def test_ai(page):
    tech = technology(page)
    tech.ai_options_clicking()
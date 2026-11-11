import pytest

from pages.tcontact import contact

@pytest.mark.smoke
def test_contact_(page):
    contact_obj = contact(page)
    contact_obj.contact_clicking()
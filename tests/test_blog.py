import pytest

from pages.tblogs import blog

@pytest.mark.smoke
def test_blog(page):
    blog_obj = blog(page)
    blog_obj.blogs_elements_clicking()

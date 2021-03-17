import re

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from web.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def remove_csrf_tag(self, text):
        """Remove csrf tag from text"""
        return re.sub(r"<[^>]*csrfmiddlewaretoken[^>]*>", "", text)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string("web/home.html", request=request)
        self.assertEqual(
            self.remove_csrf_tag(response.content.decode()),
            self.remove_csrf_tag(expected_html),
        )

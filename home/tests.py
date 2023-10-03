from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        reponse = self.client.get("/")
        self.assertEquals(reponse.status_code, 200)
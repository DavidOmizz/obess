from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginFunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()  # Use Firefox driver; you can configure Chrome or others
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_can_login(self):
        self.selenium.get(f'{self.live_server_url}/login/')
        username_input = self.selenium.find_element_by_name('username')
        password_input = self.selenium.find_element_by_name('password')
        username_input.send_keys('testuser')
        password_input.send_keys('testpass')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        # Check if login was successful by looking for a logout link or dashboard
        body_text = self.selenium.find_element_by_tag_name('body').text
        self.assertIn('Logout', body_text)

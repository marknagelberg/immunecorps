from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'volunteers/home.html')


class JoinPageTest(TestCase):

    def test_uses_join_immunecorps_template(self):
        response = self.client.get('/join-immunecorps')
        self.assertTemplateUsed(response, 'volunteers/join-immunecorps.html')


class CheckEmailPageTest(TestCase):

    def test_uses_check_emailtemplate(self):
        response = self.client.get('/check-email')
        self.assertTemplateUsed(response, 'volunteers/check-email.html')

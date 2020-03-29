from django.test import TestCase
from volunteers.models import Volunteer


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'volunteers/home.html')


class JoinPageTest(TestCase):

    def test_uses_join_immunecorps_template(self):
        response = self.client.get('/join-immunecorps')
        self.assertTemplateUsed(response, 'volunteers/join-immunecorps.html')


class NewVolunteerTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/volunteers/new',
                data={'email':'emailtest@example.com'})
        self.assertEqual(Volunteer.objects.count(), 1)
        new_volunteer = Volunteer.objects.first()
        self.assertEqual(new_volunteer.email, 'emailtest@example.com')

    def test_redirects_after_POST(self):
        response = self.client.post('/volunteers/new',
                data={'email':'emailtest@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
            '/volunteers/the-only-volunteer-in-the-world/')

    def test_cannot_POST_duplicate_email(self):
        pass
        #TODO
        #Volunteer.objects.create(email='emailtest@example.com')
        #response = self.client.post('/join-immunecorps',
                #data={'email':'emailtest@example.com'})


class VolunteerLoginPageTest(TestCase):

    def test_uses_login_template(self):
        response = self.client.get('/volunteer-login')
        self.assertTemplateUsed(response, 'volunteers/login.html')

    def test_redirects_after_POST(self):
        response = self.client.post('/volunteer-login',
                data={'email':'emailtest@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
            '/volunteers/the-only-volunteer-in-the-world/')


class VolunteerDashboardTest(TestCase):

    def test_uses_volunteer_dashboard_page_template(self):
        response = self.client.get('/volunteers/the-only-volunteer-in-the-world/')
        self.assertTemplateUsed(response, 'volunteers/dashboard.html')


class CheckEmailPageTest(TestCase):

    def test_uses_check_emailtemplate(self):
        response = self.client.get('/check-email')
        self.assertTemplateUsed(response, 'volunteers/check-email.html')


class VolunteerModelTest(TestCase):

    def test_saving_and_retrieving_volunteers(self):
        first_volunteer = Volunteer()
        first_volunteer.email = 'volunteeremail1@example.com'
        first_volunteer.save()

        second_volunteer = Volunteer()
        second_volunteer.email = 'volunteeremail2@example.com'
        second_volunteer.save()

        saved_volunteers = Volunteer.objects.all()
        self.assertEqual(saved_volunteers.count(), 2)

        first_saved_volunteer = saved_volunteers[0]
        second_saved_volunteer = saved_volunteers[1]
        self.assertEqual(first_saved_volunteer.email, 'volunteeremail1@example.com')
        self.assertEqual(second_saved_volunteer.email, 'volunteeremail2@example.com')




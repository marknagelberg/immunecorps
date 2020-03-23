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

    def test_can_save_a_POST_request(self):
        response = self.client.post('/join-immunecorps',
                data={'email':'emailtest@example.com'})
        new_volunteer = Volunteer.objects.first()
        self.assertEqual(new_volunteer.email, 'emailtest@example.com')

    def test_redirects_after_POST(self):
        response = self.client.post('/join-immunecorps',
                data={'email':'emailtest@example.com'})
        self.assertRedirects(response, '/check-email')

    def test_only_save_email_when_necessary(self):
        self.client.get('/join-immunecorps')
        self.assertEqual(Volunteer.objects.count(), 0)

    def test_cannot_POST_duplicate_email(self):
        pass
        #TODO
        #Volunteer.objects.create(email='emailtest@example.com')
        #response = self.client.post('/join-immunecorps',
                #data={'email':'emailtest@example.com'})



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




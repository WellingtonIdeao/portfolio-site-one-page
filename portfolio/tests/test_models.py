from django.test import TestCase
from ..models import Contact


class ModelContactTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(name='name', email='name@example.com', subject='subject', message='message')

    def test_contact_model_name_field_max_length(self):
        contact = Contact.objects.get(pk=1)
        max_length = contact._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_contact_model_email_field_max_length(self):
        contact = Contact.objects.get(pk=1)
        max_length = contact._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)

    def test_contact_model_subject_field_max_length(self):
        contact = Contact.objects.get(pk=1)
        max_length = contact._meta.get_field('subject').max_length
        self.assertEqual(max_length, 50)

    def test_contact_model_subject_field_is_blank(self):
        contact = Contact.objects.get(pk=1)
        is_blank = contact._meta.get_field('subject').blank
        self.assertEqual(is_blank, True)

    def test_contact_model_name_field_label(self):
        contact = Contact.objects.get(pk=1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_contact_model_email_field_label(self):
        contact = Contact.objects.get(pk=1)
        field_label = contact._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_contact_model_subject_field_label(self):
        contact = Contact.objects.get(pk=1)
        field_label = contact._meta.get_field('subject').verbose_name
        self.assertEqual(field_label, 'subject')

    def test_contact_model_message_field_label(self):
        contact = Contact.objects.get(pk=1)
        field_label = contact._meta.get_field('message').verbose_name
        self.assertEqual(field_label, 'message')






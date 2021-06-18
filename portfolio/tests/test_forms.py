from django.test import SimpleTestCase
from ..forms import ContactForm


class ContactFormTests(SimpleTestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()
        # Set up data for the whole TestCase
        cls.contactForm = ContactForm()

    def test_contact_form_name_field_label(self):
        self.assertTrue(self.contactForm.fields['name'].label == 'Nome')

    def test_contact_form_email_field_label(self):
        self.assertTrue(self.contactForm.fields['email'].label == 'Email')

    def test_contact_form_subject_field_label(self):
        self.assertTrue(self.contactForm.fields['subject'].label == 'Assunto')

    def test_contact_form_message_field_label(self):
        self.assertTrue(self.contactForm.fields['message'].label == 'Mensagem')

    def test_contact_form_label_suffix(self):
        self.assertTrue(self.contactForm.label_suffix == '')

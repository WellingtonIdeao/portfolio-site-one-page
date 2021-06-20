from django.test import SimpleTestCase
from ..forms import ContactForm
from django.forms.fields import EmailField
# py -Wa manage.py test
# coverage run --source='.' manage.py test myapp
# coverage report


class ContactFormTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        # Set up data for the whole TestCase
        super().setUpClass()
        cls.contactForm = ContactForm()

    def test_contact_form_field_name_required(self):
        self.assertEqual(self.contactForm.fields['name'].required, True)

    def test_contact_form_field_email_required(self):
        self.assertEqual(self.contactForm.fields['email'].required, True)

    def test_contact_form_field_subject_not_required(self):
        self.assertEqual(self.contactForm.fields['subject'].required, False)

    def test_contact_form_field_message_required(self):
        self.assertEqual(self.contactForm.fields['message'].required, True)

    def test_contact_form_field_name_label(self):
        self.assertEqual(self.contactForm.fields['name'].label, 'Nome')

    def test_contact_form_field_email__label(self):
        self.assertEqual(self.contactForm.fields['email'].label, 'Email')

    def test_contact_form_field_subject_label(self):
        self.assertEqual(self.contactForm.fields['subject'].label, 'Assunto')

    def test_contact_form_message_field_label(self):
        self.assertEqual(self.contactForm.fields['message'].label, 'Mensagem')

    def test_contact_form_label_suffix(self):
        self.assertEqual(self.contactForm.label_suffix, '')

    def test_contact_form_field_name_correct_widget(self):
        self.assertEqual(
            self.contactForm.fields['name'].widget.attrs,
            {'maxlength': '50', 'class': 'form-control', 'placeholder': 'Enter your name'}
        )

    def test_contact_form_field_email_correct_widget(self):
        self.assertEqual(
            self.contactForm.fields['email'].widget.attrs,
            {'maxlength': '50', 'class': 'form-control', 'placeholder': 'name@example.com'}
        )

    def test_contact_form_field_subject_correct_widget(self):
        self.assertEqual(
            self.contactForm.fields['subject'].widget.attrs,
            {'maxlength': '50', 'class': 'form-control', 'placeholder': 'Enter your subject'}
        )

    def test_contact_form_field_message_correct_widget(self):
        self.assertEqual(
            self.contactForm.fields['message'].widget.attrs,
            {
                'cols': '40', 'rows': '10', 'class': 'form-control',
                'placeholder': 'Enter your message', 'style': 'height: 10rem'
            }
        )
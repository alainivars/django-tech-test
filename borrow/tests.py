from __future__ import unicode_literals

"""
Contact Form tests
"""
from django import test
from django.forms import ModelForm

from form import ContactForm


class ContactFormTests(test.TestCase):
    """
    simple functional tests:
    - url
    - form validation
    """

    def test_is_subclass_of(self):
        self.assertTrue(issubclass(ContactForm, ModelForm))

    def test_sends_mail_with_headers(self):
        reply_to_email = u'user@example.com'  # the user's email
        data = {
            'name': b'Test',
            'phone': b'0123456789',
            'email': reply_to_email,
            'companyName': b'Test',
            'companyAddress': b'Test address',
            'companyNumber': b'01234567',
            'companySector': 1,
            'amount': b'10000',
            'duration': b'365',
            'description': b'Test message'
        }
        form = ContactForm(data=data)
        assert form.is_valid()


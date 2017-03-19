#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm

from models import Contact

# just the minimum, it's a challenge

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        # but here, never forget : Explicit is better than implicit
        fields = [
            'name', 'email', 'phone',
            'companyName', 'companyAddress', 'companyNumber', 'companySector',
            'amount', 'duration', 'description'
        ]

#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


BUSINESS_SECTOR = (
    ('1', _('Retail')),
    ('2', _('Professional Services')),
    ('3', _('Food & Drink')),
    ('4', _('Entertainment')),
)


class Contact(models.Model):
    """
    Contact form:
    We could of course manage users and add register before they can borrow
    money but it's not a complete app and the user management must be place
    in an other app.
    We could also validate email (format, send email register verification),
    same for the look with bootstrap.
    I just chosen to follow the spec. ie. "The Task"
    """

    class Meta:
        app_label = 'borrow'

    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=200)
    phone = models.CharField(_('Phone Number'), max_length=25)
    companyName = models.CharField(_('Company Name'), max_length=100)
    # address is simplified (no multi-fields)
    companyAddress = models.CharField(_('Company Address'), max_length=100)
    companyNumber = models.CharField(_('Company Number'), max_length=8)
    companySector = models.CharField(_('Company Sector'), max_length=1, choices=BUSINESS_SECTOR)
    amountValidators = [MinValueValidator(10000), MaxValueValidator(100000)]
    amount = models.PositiveIntegerField(_('Amount'), validators=amountValidators)
    duration = models.PositiveIntegerField(_('Days'))
    description = models.TextField(_('Description'), )

    def __str__(self):
        return self.name

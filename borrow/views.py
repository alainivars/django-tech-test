#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from form import ContactForm
from django.views.generic import FormView


def success(request):
    return HttpResponse('Success!')


class ContactFormView(FormView):
    """
    I could choice to do on so many way to manage with this challenge.
    But because I use Django to resolve it and him philosophy is KISSS,
    same as Python, let Django work:

    1/ in the model: Django manage very well data and single validation
    2/ in the form: Django made oll the work, could be it more simple
    3/ in the view: I just overload form_valid to save valid form in database

    Finally: Django is one of the better and faster Framework ever created,
             when you understand it.
    """
    template_name = "contact.html"
    form_class = ContactForm
    success_url = '/borrow/success/'

    def form_valid(self, form):
        form.save()
        return super(ContactFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['url'] = 'contact'
        return context


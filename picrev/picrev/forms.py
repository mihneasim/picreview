from django.forms import ModelForm

from picrev.models import Request


class RequestForm(ModelForm):

    class Meta(object):

        model = Request
        fields = ['name', 'email', ]

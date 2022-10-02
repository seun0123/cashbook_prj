from socket import fromshare
from django import forms
from .models import Cashbook

class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title', 'feeling','content', 'image']

    def __init__(self, *args, **kwargs):
        super(CashbookForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False

    def __init__(self, *args, **kwargs):
        super(CashbookForm, self).__init__(*args, **kwargs)
        self.fields['feeling'].required = False       
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['feeling'].widget.attrs['readonly'] = True
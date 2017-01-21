from django import forms
from employees.models import employees
'''
class ContactForm(forms.Form):
    CHOICES = (('dcare', 'Direct Care'),('admin', 'Admin'),('recreation', 'Recreation'),)
    togroup = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=CHOICES, label="Choose Group:")
    yourname = forms.CharField(required=False, label='Your Name\n(optional)')
    message = forms.CharField(required=False, label='Message')'''

class ContactForm(forms.Form):
    CHOICES = (('dcare', 'Direct Care - (MN Work)'),('admin', 'Admin - (DN)'),('recreation', 'Recreation - (MN Personal)'),)
    togroup = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=CHOICES, label="Choose Group:", error_messages={'required': 'Please choose a group!'})
    yourname = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 24, 'rows': 4}))
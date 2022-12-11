from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Submit
from django import forms
from django.urls import reverse_lazy

from .models import Contact


class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('contact:contact')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.layout = Layout(
            FloatingField('email'),
            FloatingField('message'),
            FloatingField('subject'),
        )

    subject = forms.CharField()
    email = forms.CharField()
    message = forms.Textarea()

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = '__all__'

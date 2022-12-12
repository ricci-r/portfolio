from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import ButtonHolder, Column, Row, Submit
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
        self.helper.disable_csrf = False
        self.helper.layout = Layout(
            FloatingField('subject'),
            FloatingField('email'),
            Row(
                Column(FloatingField('name', css_class='form-group col-md-6 mb-0')),
                Column(FloatingField('last_name', css_class='form-group col-md-6 mb-0')),
                css_class='form-row'
            ),
            FloatingField('message'),
            ButtonHolder(
                Submit('submit', 'Enviar', css_class='btn btn-dark')
            )
        )

    name = forms.CharField(
        label="Nome"
    )
    last_name = forms.CharField(
        label="Sobrenome"
    )
    subject = forms.CharField(
        label="Assunto"
    )
    email = forms.CharField(
        label="E-mail"
    )
    message = forms.Textarea()

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = '__all__'
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = '__all__'

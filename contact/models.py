from django.db import models


class Contact(models.Model):
    """Model definition for Contact."""

    name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return str(self.email)

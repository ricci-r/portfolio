from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Website"
            body = {
                'emal': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, settings.CONTACT_EMAIL , [settings.CONTACT_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Mensagem enviada com sucesso')
            return redirect("contact:contact")
        messages.error(request, 'Error: Mensagem não enviada.')

    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/index.html', context)

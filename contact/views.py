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
            subject = 'Gostaria de falar sobre'
            body = {
                'name':form.cleaned_data['name'],
                'last_name':form.cleaned_data['last_name'],
                'emal': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER , [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Mensagem enviada com sucesso')
            return redirect("contact:contact")
            
        messages.error(request, 'Error: Mensagem não enviada.')

    form = ContactForm()

    context = {
        'form': ContactForm()
    }

    return render(request, 'contact/index.html', context)

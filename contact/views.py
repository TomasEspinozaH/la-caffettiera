from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def contact(request):
  contact_form = ContactForm()
  if request.method == "POST":
    contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
      name = request.POST.get('name', '')
      email = request.POST.get('email', '')
      content = request.POST.get('content', '')
      # Enviamos correo y redireccionamos
      email = EmailMessage(
        "La Caffettiera: Nuevo mensaje de contacto",
        "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
        "no-contestar@inbox.mailtrap.io", 
        ["tomasceatoleii1998@gmail.com"],
        reply_to=[email]
      )
      try:
        email.send()
        return redirect(reverse('contact') + "?ok")  
      except:
        #algo fallo, redireccionamos a FAIL
        return redirect(reverse('contact') + "?fail")

      return redirect(reverse('contact') + "?ok")

  return render(request, 'contact/contact.html', {'form':contact_form})
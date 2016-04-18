# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import PonosenEmail, RecoverPassword
from .forms import PasswordRecoverForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from lunaApi.settings import SEND_MAIL_PONOSEN
from django.utils.crypto import get_random_string

# Create your views here.
def saveEmail(request, email):
	try:
		if PonosenEmail.objects.filter(email=email):
			return JsonResponse({"saved": False, "alert": "Uporabnik že obstaja"})
		else:
			PonosenEmail(email=email).save()
			return JsonResponse({"saved":True})
	except:
		return JsonResponse({"saved": False})


def reqRecoverPassword(request, email):
	user = PonosenEmail.objects.filter(email=email)
	if user:
		unique_id = get_random_string(length=32)
		RecoverPassword(user=user[0], code=unique_id).save()
		#send mail
		data = {"code":unique_id}
		msg_plain = render_to_string('ponosen/email.html', data)
		msg_html = render_to_string('ponosen/email.html', data)
		send_mail("Ponosna obnovitev gesla",
			msg_plain,
			SEND_MAIL_PONOSEN,
			[email],
			html_message=msg_html,
			)
		return JsonResponse({"alert": "Preveri nabiralnik"})
	else:
		return JsonResponse({"alert": "Uporabnik s tem e-mailom ne obstaja"})


def recoverPassword(request, code):
	recovery = RecoverPassword.objects.filter(code=code)
	if recovery:
		if request.POST:
			form = PasswordRecoverForm(request.POST)
			if form.is_valid():
				return render(request, 'ponosen/passwordRecovery.html', {"passwd":form.cleaned_data['password'], "email": recovery[0].user.email})
			else:
				context = {"forma":form, "code":code}
				return render(request, 'ponosen/passwordRecovery.html', context)
		else:
			return render(request, 'ponosen/passwordRecovery.html', {"forma":PasswordRecoverForm(), "code":code})

	else:
		return render(request, 'ponosen/passwordRecovery.html', {"alert":"zahtevek ne obstaja"})

def ping(request):
	return JsonResponse({"response": "Smo tu"})
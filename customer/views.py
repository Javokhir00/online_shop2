from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .send_email_form import EmailForm
# Create your views here.


def customer_list(request):
    return render(request, 'customer/customer_list.html' )




def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            recipient_list = form.cleaned_data['recipient_list']  # Already a validated list
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                return HttpResponse("✅ Email sent successfully.")
            except Exception as e:
                return HttpResponse(f"❌ Failed to send email: {str(e)}", status=500)
        else:
            return render(request, 'customer/send_email.html', {'form': form})
    else:
        form = EmailForm()
    return render(request, 'customer/send_email.html', {'form': form})

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@csrf_exempt
@require_POST
def send_contact_email(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        print(name)
        # Replace the following values with your email settings
        subject = 'Contact Form Submission'
        message_body = f'Name: {name}\n\nMessage:\n{message}'
        from_email = email
        recipient_list = ["shivrajkolwankar0124@gmail.com"]

        send_mail(subject, message_body, from_email, recipient_list, fail_silently=False)

        return JsonResponse({'success': True, 'message': 'Email sent successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


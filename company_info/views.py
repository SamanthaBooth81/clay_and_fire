"""Company Info Views"""
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


def faq_page(request):
    """View to return FAQ's page"""
    return render(request, 'help/faqs.html')


def shipping_returns(request):
    """View to return shipping and returns info page"""
    return render(request, 'help/shipping-returns.html')


def about_us(request):
    """View to return shipping and returns info page"""
    return render(request, 'company/about-us.html')


def privacy_policy(request):
    """View to return shipping and returns info page"""
    return render(request, 'company/privacy-policy.html')


def contact(request):
    """View to return contact us page"""
    # Help from Scottish Coder YouTube Tutorial - link in README
    if request.method == 'POST':
        # Send contact form to Gmail Account
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        From: {}
        New message: {}
        '''.format(message_data['email'], message_data['message'])

        send_mail(
            message_data['subject'], message, '', ['sambooth018@gmail.com'])

        messages.info(request, (
            f'Your message has been sent, we will contact you \
                via { email } as soon as possible.'))
        return render(request, 'home/index.html')

    return render(request, 'contact/contact-us.html')

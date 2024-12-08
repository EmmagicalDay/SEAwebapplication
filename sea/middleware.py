# sea/middleware.py

from django.utils.timezone import now
from django.contrib import messages
from django.shortcuts import redirect
from .models import FailedLoginAttempt

class AccountLockoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            failed_attempt = FailedLoginAttempt.objects.filter(user=request.user).first()
            if failed_attempt and failed_attempt.attempts >= 3:
                from django.contrib.auth import logout
                logout(request)
                messages.error(request, 'Your account is locked. Please contact administrators.')
                return redirect('user-login')
        response = self.get_response(request)
        return response

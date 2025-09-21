from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import RSVP

def invitation(request):
    return render(request, 'invite/invitation.html')

@require_POST
def rsvp(request):
    name = request.POST.get('guestName', '').strip()
    attendance = request.POST.get('attendance')
    RSVP.objects.create(name=name, attendance=attendance)
    return JsonResponse({'ok': True})

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Meet

# Create your views here.
def home(request):
    meets = Meet.objects
    return render(request, 'home.html', {'meets': meets})

def new(request):
    return render(request, 'new.html')

def create(request):
    meet = Meet()
    meet.title = request.GET['title']
    meet.body = request.GET['body']
    meet.pub_date = timezone.datetime.now()
    meet.save()
    return redirect("/meeting/"+str(meet.id))

def detail(request, meet_id):
    meet_detail = get_object_or_404(Meet, pk = meet_id)
    return render(request, 'detail.html', {'meet':meet_detail})
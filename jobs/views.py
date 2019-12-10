from django.shortcuts import render

from .models import Job,ViewsCount

def home(request):
    jobs = Job.objects
    views_count = ViewsCount.objects.get(id=1)
    views_count.count += 1
    views_count.save()
    return render(request, 'jobs/home.html', {'jobs':jobs,'count':views_count.count})

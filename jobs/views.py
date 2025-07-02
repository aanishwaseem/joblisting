from django.shortcuts import render, get_object_or_404
from .models import Jobs
# Create your views here.
def all_jobs(request):
    jobs = Jobs.objects.all()
    return render(request, 'jobs/find-jobs.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

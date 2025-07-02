from django.urls import path,include
from jobs import views
urlpatterns = [
    path('', views.all_jobs, name='find-jobs'),
    path('<int:job_id>', views.job_detail, name='job_detail'),

]

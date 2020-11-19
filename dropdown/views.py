from django.shortcuts import render
from .models import Programming, Course

# Create your views here.
def index(request):
    program = Programming.objects.all()
    d = {'program': program}
    return render(request, 'index.html', d)

def load_course(request):
    programming_id = request.GET.get('programming')
    print(programming_id)
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    data = {'courses': courses}
    return render(request, 'course_dropdown_list_options.html', context=data)
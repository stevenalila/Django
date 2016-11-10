from django.shortcuts import render
#controller
# Create your views here.
def index(request):
    return render(request, "time_display_assignment/index.html")
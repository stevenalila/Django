from django.shortcuts import render, HttpResponse
import datetime
#controller
# Create your views here.
def index(request):
	day_format = "%b %d, %Y"
	time_format = "%I:%M %p"
	today = datetime.datetime.today()
	day = today.strftime(day_format)
	time = today.strftime(time_format)
	return render(request, 'time_display_assignment/index.html', {'day':day, 'time':time})
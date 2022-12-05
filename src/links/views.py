from django.shortcuts import render
from django.http import HttpResponse

from links.models import Links
# Create your views here.



def home_page(request):
    links = Links.objects.all()
    context = {"links": links}
    return render(request, template_name="home.html", context=context)
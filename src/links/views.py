from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from links.models import Links
# Create your views here.



def links_list(request):
    links = Links.objects.all()
    context = {"links": links}
    return render(request, template_name="home.html", context=context)


def links_detail(request, pk):
    link = Links.objects.get(pk=pk)
    context = {"object": link}
    return render(request, template_name="detail.html", context=context)

def links_delete(request, pk):
    link = Links.objects.get(pk=pk)
    message = f'Videos {link.name} has just deleted!!!'
    link.delete()
    context = {"message": message}
    return render(request, template_name="delete.html", context=context)

def links_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        links = request.POST.get('links')
        link = Links.objects.create(name=name, links=links)
        return HttpResponseRedirect(reverse('videos-detail', kwargs={'pk': link.pk}))
    context = {}
    return render(request, template_name="create.html", context=context)


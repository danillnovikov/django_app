from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, DeleteView, CreateView

from . import forms
from links.models import Links
# Create your views here.



def links_list(request):
    links = Links.objects.all()
    context = {"links": links}
    return render(request, template_name="home.html", context=context)

class LinksList(ListView):
    model = Links


def links_detail(request, pk):
    link = Links.objects.get(pk=pk)
    context = {"object": link}
    return render(request, template_name="detail.html", context=context)

class LinksDetail(DetailView):
    model= Links

def links_delete(request, pk):
    link = Links.objects.get(pk=pk)
    message = f'Videos {link.name} has just deleted!!!'
    link.delete()
    context = {"message": message}
    return render(request, template_name="delete.html", context=context)

class LinksDelete(DeleteView):
    success_url = reverse_lazy('links-list-cbv')
    model = Links

def links_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        links = request.POST.get('links')
        link = Links.objects.create(name=name, links=links)
        return HttpResponseRedirect(reverse('videos-detail', kwargs={'pk': link.pk}))
    context = {'form': forms.LinksForm()}
    return render(request, template_name="create.html", context=context)

class LinksCreate(CreateView):
    model = Links
    #fields=('name', 'links')
    success_url=reverse_lazy('links-list-cbv')
    form_class = forms.LinksForm

def links_update(request, pk):
    #http://127.0.0.1:8000/links-update/1/
    if request.method == "GET":
        link = Links.objects.get(pk=pk)
        context = {'link': link}
    elif request.method == "POST":
        name = request.POST.get('name')
        links = request.POST.get('links')
        #link = Links.objects.create(name=name, links=links)
        link = Links.objects.get(pk=pk)
        link.name = name
        link.links = links
        link.save()
        return HttpResponseRedirect(reverse('videos-detail', kwargs={'pk': link.pk}))
    return render(request, template_name="update.html", context=context)

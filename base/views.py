from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView



from .models import Item
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('items')

class ItemList(ListView):
    model = Item
    context_object_name = 'items'

class ItemDetail(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'base/item.html'

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('items')

class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('items')

class ItemDelete(DeleteView):
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('items')

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Item
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('items')

class CustomRegisterView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        '''
            form_valid is an inbuilt function.
            Simply making sure, user is logged in after registration.
        '''
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('items')
        return super(CustomRegisterView, self).get(*args, **kwargs)




class ItemList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        '''
            This built-in function is modified to assure that respective users can login
            and edit into their account and their account only,
            They cannot get access of data/shopping_list items that doesn't belong
            to them.

            context['items'] = context['items'].filter(user=self.request.user)
            filters data to give access to respective currently logged in user's data only
        '''
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user) #give access to personal data only
        context['count'] = context['items'].filter(purchased = False).count() #provides count of unpurchased items.

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['items'] = context['items'].filter(
                item_name__icontains = search_input
            )
        context['search_input'] = search_input

        return context


class ItemDetail(LoginRequiredMixin,DetailView):
    '''
        LoginRequiredMixin restricts users without account to access any data.
        ItemDetail is the R of CRUD i.e. Read.
    '''
    model = Item
    context_object_name = 'item'
    template_name = 'base/item.html'

class ItemCreate(LoginRequiredMixin, CreateView):
    '''
        LoginRequiredMixin restricts users without account to access any data.
        ItemDetail is the C of CRUD i.e. Create.
    '''
    model = Item
    fields = ['item_name', 'description', 'purchased']
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        '''
            form_valid is an inbuilt function.
            Simply making sure, that an account only has access to edit its own data only.
        '''
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
    '''
        LoginRequiredMixin restricts users without account to access any data.
        ItemUpdate is the U of CRUD i.e. Update.

    '''
    model = Item
    fields = ['item_name', 'description', 'purchased']
    success_url = reverse_lazy('items')

class ItemDelete(LoginRequiredMixin, DeleteView):
    '''
        LoginRequiredMixin restricts users without account to access any data.
        ItemDetail is the D of CRUD i.e. Delete.
    '''
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('items')

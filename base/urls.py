from django.urls import path
from .views import ItemList, ItemDetail, ItemCreate, ItemUpdate, ItemDelete, CustomLoginView, CustomRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('register/',CustomRegisterView.as_view(), name = 'register'),

    path('', ItemList.as_view(), name = 'items'),
    path('item/<int:pk>', ItemDetail.as_view(), name='item'),
    path('create-item/', ItemCreate.as_view(), name = 'item-create'),
    path('item-update/<int:pk>', ItemUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>', ItemDelete.as_view(), name='item-delete'),

]

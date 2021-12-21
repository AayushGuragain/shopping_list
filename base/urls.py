from django.urls import path
from .views import ItemList, ItemDetail, ItemCreate, ItemUpdate, ItemDelete

urlpatterns = [
    path('', ItemList.as_view(), name = 'items'),
    path('item/<int:pk>', ItemDetail.as_view(), name='item'),
    path('create-item/', ItemCreate.as_view(), name = 'item-create'),
    path('item-update/<int:pk>', ItemUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>', ItemDelete.as_view(), name='item-delete'),


]

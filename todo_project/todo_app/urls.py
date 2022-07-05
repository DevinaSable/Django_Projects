from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("list/<int:id>/", views.ItemListView.as_view(), name="list"),
    #CRUD Patern for TodoList
    path("list/add", views.ListCreate.as_view(), name='list-add'),
    path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    #CRUD pattern for TodoItems
    path("list/<int:list_id/item/add/", views.ItemCreate.as_view(), name='item-add'),
    path("list/<int:id>/item/<int:pk>/", views.ItemUpdate.as_view(), name='item-update'),
    path("list/<int:id>/delete/", views.ItemDelete.as_view(), name="item-delete"),

]
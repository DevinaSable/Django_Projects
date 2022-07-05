from django.urls import path
from . import views

urlpatterns = [
    path("",
         views.DiaryEntryListView.as_view(),
         name='diaryentry-list'
         ),


    path("diaryentry/<int:pk>",
         views.DiaryEntryDetailView.as_view(),
         name='diaryentry-detail'
         ),


    path("create",
        views.DiaryEntryCreateView.as_view(),
         name="diaryentry-create"
        ),


    path("diaryentry/<int:pk>/update",
         views.DiaryEntryUpdateView.as_view(),
         name='diaryentry-update'
        ),


    path("diaryentry/<int:pk>/delete",
         views.DiaryEntryDeleteView.as_view(),
         name='diaryentry-delete'
        ),
]

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView,
)

from .models import DiaryEntry
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class DiaryEntryListView(ListView):
    model = DiaryEntry
    queryset = DiaryEntry.objects.all().order_by("-date_created")


class DiaryEntryDetailView(DetailView):
    model = DiaryEntry


class DiaryEntryCreateView(SuccessMessageMixin, CreateView):
    model = DiaryEntry
    fields = ['title', 'content']
    success_url = reverse_lazy('diaryentry-list')
    success_message = "Your new entry was created!"



class DiaryEntryUpdateView(SuccessMessageMixin, UpdateView):
    model = DiaryEntry
    fields = ['title', 'content']
    success_message = "Your entry was updated!"


    def get_success_url(self):
        return reverse_lazy("diaryentry-detail",
                            kwargs={"pk": self.object.pk})


class DiaryEntryDeleteView(DeleteView):
    model = DiaryEntry
    success_url = reverse_lazy('diaryentry-list')
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)



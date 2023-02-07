from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
# message
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Login Logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Diary


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class DiaryListView(LockedView, ListView):
    model = Diary
    queryset = Diary.objects.all().order_by("create_date")


class DiaryDetailView(LockedView, DetailView):
    model = Diary


class DiaryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Diary
    fields = ["title", "content"]
    success_url = reverse_lazy("diary-list")
    success_message = "Your new diary was created!"


class DiaryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Diary
    fields = ["title", "content"]
    success_message = "Your diary was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "diary-detail",
            kwargs={"pk": self.diary.id}
        )


class DiaryDeleteView(LockedView, DeleteView):
    model = Diary
    success_url = reverse_lazy("diary-list")
    success_message = "Your diary was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


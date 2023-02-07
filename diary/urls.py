from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        # as_view() 클래스로 진입하기 위한 진입 메소드(클래스형 뷰 사용)
        views.DiaryListView.as_view(),
        name="diary-list"
    ),
    path(
        "<int:pk>",
        views.DiaryDetailView.as_view(),
        name="diary-detail"
    ),
    path(
        "create",
        views.DiaryCreateView.as_view(),
        name="diary-create"
    ),
    path(
        "<int:pk>/update",
        views.DiaryUpdateView.as_view(),
        name="diary-update"
    ),
    path(
        "<int:pk>/delete",
        views.DiaryDetailView.as_view(),
        name="diary-delete"
    ),
]

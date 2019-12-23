from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.board_list),
    path("write/", views.board_write),
    path("detail/<int:pk>", views.board_detail)  # 정수형 pk번째 글 검색
]

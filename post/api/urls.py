from . import views
from django.urls import path

urlpatterns = [
    path('', views.apiOverView, name="api-over-view"),
    path('post-list/', views.PostList.as_view(), name="post-list-api"),
    path('post-detail/<slug:slug>/', views.PostDetail.as_view(), name="post-detail-api"),
]

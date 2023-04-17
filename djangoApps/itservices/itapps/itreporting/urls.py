from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', views.home, name = 'itreporting-home'),
    path('about/', views.about, name = 'itreporting-about'),
    path('products/', PostListView.as_view(), name = 'itreporting-report'),
    path('issue/<int:pk>', PostDetailView.as_view(), name = 'issue-detail'),
    path('review/new/', PostCreateView.as_view(), name = 'issue-create'),
    path('review/<int:pk>/update/', PostUpdateView.as_view(), name = 'review-update'),
    path('review/<int:pk>/delete/', PostDeleteView.as_view(), name = 'review-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-review'),
    path('contact/', views.contact, name = 'itreporting-contact'),



]

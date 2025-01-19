from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostsListView.as_view(), name='blog'),
    path('<slug:category_slug>/', views.PostsListView.as_view(), name='category'),
    path('<slug:category_slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='category_post'),
]
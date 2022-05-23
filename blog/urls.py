from django.urls import path
from .views import PostListView, PostDetailView #post_list, post_detail

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>-<int:month>-<int:day>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
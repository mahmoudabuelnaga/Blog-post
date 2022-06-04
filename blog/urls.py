from django.urls import path
from .views import PostListView, PostDetailView, EmailPostView #post_list, post_detail

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>-<int:month>-<int:day>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('share/<int:post_id>/', EmailPostView, name='post_share'),
]
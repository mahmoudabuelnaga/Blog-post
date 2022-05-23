from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic
# Create your views here.
class PostListView(generic.ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = "blog/post/list.html"

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 1)
#     page = request.GET.get('page')
    
#     try:
#         posts = paginator.page(page)
#         print(posts)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)

#     context = {
#         'posts':posts,
#     }
#     return render(request, 'blog/post/list.html', context)


class PostDetailView(generic.DeleteView):
    queryset = Post.objects.all()
    context_object_name = 'post'
    template_name = 'blog/post/detail.html'

# def post_detail(request, year, month, day, slug):
#     post = get_object_or_404(
#         Post, slug=slug, status='published', 
#         publish__year=year, publish__month=month, publish__day=day
#     )

#     context = {
#         'post':post,
#     }

#     return render(request, 'blog/post/detail.html', context)
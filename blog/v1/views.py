from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Blog
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect


class BlogListView(ListView):

    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog_detail'


class BlogCreateView(CreateView):

    model = Blog
    fields = ('content',)
    template_name = 'blog/blog_form.html'


class BlogUpdateView(UpdateView):

    model = Blog
    fields = ('content',)


class BlogDeleteView(DeleteView):

    model = Blog
    success_url = reverse_lazy('list-blogs')


@csrf_exempt
def post_upvote(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.post_upvote()
    return JsonResponse({'success': True})


@csrf_exempt
def post_downvote(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.post_downvote()
    return JsonResponse({'success': True})

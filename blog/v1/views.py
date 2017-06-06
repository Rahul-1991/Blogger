from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Blog
from django.core.urlresolvers import reverse_lazy


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


class BlogUpdateView(UpdateView):

    model = Blog
    fields = ('content',)


class BlogDeleteView(DeleteView):

    model = Blog
    success_url = reverse_lazy('list-blogs')

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, DeleteView
from django.shortcuts import render
from .models import BlogDataStructure
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
# from .forms import BlogForm


class BlogListView(View):

    context = BlogDataStructure().get_list()
    template_name = 'blog/blog_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'context': self.context})


class BlogCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'blog/blog_form.html', {'context': {'create': True}})

    def post(self, request, *args, **kwargs):
        response = dict(request.POST)
        response.pop('csrfmiddlewaretoken')
        BlogDataStructure().create(response)
        return HttpResponseRedirect(reverse('list-blogs'))


class BlogDetailView(View):

    template_name = 'blog/blog_detail.html'

    def get(self, request, *args, **kwargs):
        pk = int(self.kwargs.get('pk'))      # check for non integer pk
        data = BlogDataStructure().read(pk)
        return render(request, self.template_name, {'context': data})


class BlogUpdateView(View):

    template_name = 'blog/blog_form.html'

    def get(self, request, *args, **kwargs):
        pk = int(self.kwargs.get('pk'))
        data = BlogDataStructure().read(pk)
        data.update({'create': False})
        return render(request, 'blog/blog_form.html', {'context': data})

    def post(self, request, *args, **kwargs):
        pk = int(self.kwargs.get('pk'))
        response = dict(request.POST)
        response.pop('csrfmiddlewaretoken')
        BlogDataStructure().update(pk, response)
        return HttpResponseRedirect(reverse('list-blogs'))


class BlogDeleteView(View):

    def get(self, request, *args, **kwargs):
        pk = int(self.kwargs.get('pk'))
        response = BlogDataStructure().read(pk)
        return render(request, 'blog/blog_confirm_delete.html', {'context': response})

    def post(self, request, *args, **kwargs):
        pk = int(self.kwargs.get('pk'))
        BlogDataStructure().delete(pk)
        context = BlogDataStructure().get_list()
        return render(request, 'blog/blog_list.html', {'context': context})


# class BlogListView(ListView):
#
#     model = Blog
#     template_name = 'blog/blog_list.html'
#
#     def get_queryset(self):
#         return Blog.objects.all().order_by('-upvote_count')


# class BlogDetailView(DetailView):
#
#     model = Blog
#     template_name = 'blog/blog_detail.html'
#     context_object_name = 'blog_detail'
#
#
# class BlogCreateView(CreateView):
#
#     model = Blog
#     form_class = BlogForm
#     template_name = 'blog/blog_form.html'
#
#
# class BlogUpdateView(UpdateView):
#
#     model = Blog
#     form_class = BlogForm
#
#
# class BlogDeleteView(DeleteView):
#
#     model = Blog
#     success_url = reverse_lazy('list-blogs')
#
#
# @csrf_exempt
# def post_upvote(request, pk):
#     post = get_object_or_404(Blog, pk=pk)
#     post.post_upvote()
#     return JsonResponse({'success': True})
#
#
# @csrf_exempt
# def post_downvote(request, pk):
#     post = get_object_or_404(Blog, pk=pk)
#     post.post_downvote()
#     return JsonResponse({'success': True})

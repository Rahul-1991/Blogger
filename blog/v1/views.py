from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.shortcuts import render
from .models import BlogDataStructure
from blog.decorators import process_params
from blog.utils import get_published_time_diff


class BlogListView(View):

    template_name = 'blog/blog_list.html'

    def get(self, request, *args, **kwargs):
        context = BlogDataStructure().get_list()
        for key, value in context.iteritems():
            published_time_diff = get_published_time_diff(value.get('updated_at'))
            value.update({'published_time_diff': published_time_diff})
        return render(request, self.template_name, {'context': context})


class BlogCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'blog/blog_form.html', {'context': {'create': True}})

    @process_params()
    def post(self, request, *args, **kwargs):
        response = kwargs.get('params')
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
        pk = int(kwargs.get('pk'))
        data = BlogDataStructure().read(pk)
        data.update({'create': False})
        return render(request, 'blog/blog_form.html', {'context': data})

    @process_params()
    def post(self, request, *args, **kwargs):
        pk = int(self.kwargs.get('pk'))
        response = kwargs.get('params')
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


@csrf_exempt
def post_upvote(request, pk):
    data = BlogDataStructure().read(int(pk))
    data.update({
        'upvote_count': data.get('upvote_count', 0) + 1
    })
    BlogDataStructure().update(int(pk), data)
    return JsonResponse({'success': True})


@csrf_exempt
def post_downvote(request, pk):
    data = BlogDataStructure().read(int(pk))
    data.update({
        'downvote_count': data.get('downvote_count', 0) + 1
    })
    BlogDataStructure().update(int(pk), data)
    return JsonResponse({'success': True})

from django.conf.urls import url
import views

urlpatterns = [
    url(r'list/$', views.BlogListView.as_view(), name='list-blogs'),
    url(r'detail/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='detail-blog'),
    url(r'create/$', views.BlogCreateView.as_view(), name='create-blog'),
    url(r'update/(?P<pk>\d+)/$', views.BlogUpdateView.as_view(), name='update-blog'),
    url(r'delete/(?P<pk>\d+)/$', views.BlogDeleteView.as_view(), name='delete-blog'),
]

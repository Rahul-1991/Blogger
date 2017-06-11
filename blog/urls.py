from django.conf.urls import url, include


# can be used for versioning by adding a v2/ url
urlpatterns = [
    url(r'v1/', include('blog.v1.urls'))
]

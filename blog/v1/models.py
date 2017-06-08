from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime
from blog.utils import get_time_difference


class TrackingField(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Blog(TrackingField):

    content = models.TextField(max_length=255)
    upvote_count = models.IntegerField(null=True, blank=True, default=0)
    downvote_count = models.IntegerField(null=True, blank=True, default=0)

    def get_absolute_url(self):
        return reverse('list-blogs')

    def get_time_difference(self):
        current_time = datetime.now()
        published_time = self.updated_at.replace(tzinfo=None)
        delta = current_time - published_time
        time_diff = get_time_difference(delta)
        if time_diff.get('days', 0):
            return 'published {} days ago'.format(time_diff.get('days'))
        elif time_diff.get('hours', 0):
            return 'published {} hours ago'.format(time_diff.get('hours'))
        elif time_diff.get('mins', 0):
            return 'published {} mins ago'.format(time_diff.get('mins'))
        else:
            return 'published {} seconds ago'.format(time_diff.get('secs', 0))

    def post_upvote(self):
        self.upvote_count = self.upvote_count + 1
        self.save()

    def post_downvote(self):
        self.downvote_count = self.downvote_count - 1
        self.save()

    def __str__(self):
        return self.content


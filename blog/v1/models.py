from django.db import models
from django.core.urlresolvers import reverse


class TrackingField(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Blog(TrackingField):

    content = models.CharField(max_length=255)
    upvote_count = models.IntegerField(null=True, blank=True)
    downvote_count = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('detail-blog', kwargs={'pk': self.pk})


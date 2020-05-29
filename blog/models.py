from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import pgettext_lazy
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    # to filter posts using published
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250,
                             verbose_name=pgettext_lazy('Model: Post', 'Title'))
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name=pgettext_lazy('Model: Post', 'Author'),
                               related_name='blog_posts')
    body = models.TextField(verbose_name=pgettext_lazy('Model: Post', 'Body'))
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name=pgettext_lazy('Model: Post', 'Publish date'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()
    published = PublishedManager()

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # Will be used in post to link to specific posts.
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    # related_name helps where post.comments.all() will retrieve
    # all comments of a post object
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80,
                            verbose_name=pgettext_lazy('Model: Comment', 'Name'))
    email = models.EmailField(verbose_name=pgettext_lazy('Model: Comment', 'E-Mail'))
    body = models.TextField(verbose_name=pgettext_lazy('Model: Comment', 'Body'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment By {self.name} on {self.post}'

    # Gets all replies of a parent comment
    def children(self):
        return Comment.objects.filter(parent=self)

    # If there is a parent it means this object
    # is a chilren (not parent)
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        # returns the qs of objects to include in this sitemap,
        # get_absolute_url() is called on each object to get its URL
        return Post.published.all()

    def lastmodefied(self, obj):
        # receive each object from items() and returns the last time
        # the object was updated
        return obj.updated

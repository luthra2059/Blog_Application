from django.db import models

# Create your models here.

from django.contrib.auth.models import User

STATUS = {
    (0, "Draft"),
    (1, "Publish")
}

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(active=True)

class Post(models.Model):
    title = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

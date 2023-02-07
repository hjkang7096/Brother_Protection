from django.db import models
from django.conf import settings
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Video(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    video = EmbedVideoField()
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    n_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("firetube:video_detail", args=[self.pk])

    @property
    def update_counter(self):
        self.n_count = self.n_count + 1
        self.save()
        return self.n_count

    class Meta:
        ordering = ["-id"]


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)  # 1:다수는 다수측에 정의
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="firetube_my_author_set",
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "{}::{}".format(self.author, self.message)

    def get_absolute_url(self):
        return f"{self.video.get_absolute_url()}#comment-{self.pk}"

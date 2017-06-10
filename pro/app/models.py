from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.

class Post(models.Model):
	User = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	Title = models.CharField(max_length=100, blank=False)
	Image = models.ImageField(blank=True, null=True, height_field="height_field", width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	Content = models.TextField()
	Draft = models.BooleanField(default=False)
	Publish = models.DateField(auto_now=True, auto_now_add=False)
	Timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	Updated = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.Title

	def get_absolute_url(self):
		return reverse("post_detail", kwargs={'id': self.id})
		# return "/app/%s/" %(self.id)

	class Meta:
		ordering = ["-id", '-Timestamp', '-Updated']
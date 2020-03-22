from django.db import models

# Create your models here.

class Project(models.Model):

    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    github_link = models.CharField(max_length=100, blank=True, default="Repo name only")
    other_link = models.CharField(max_length=100, blank=True, default="Domain without https://")
    date_added = models.DateTimeField(auto_now_add=True)

    def Meta(self):
        verbose_name_plural = 'Projects'

    def __str__(self):

        if len(self.name) > 50:
            return self.name[:50]
        else:
            return self.name
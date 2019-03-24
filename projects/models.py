from django.db import models
from markdownx.models import MarkdownxField
from django.urls import reverse
from markdownx.utils import markdownify

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = MarkdownxField()
    video_link = models.CharField(max_length=50, null=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.description)

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('project-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

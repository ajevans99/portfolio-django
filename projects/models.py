from django.db import models
from markdownx.models import MarkdownxField
from django.urls import reverse
from markdownx.utils import markdownify

class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=6, verbose_name="Hex code")

    def __str__(self):
        return self.name
class Project(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = MarkdownxField()
    video_link = models.CharField(max_length=200, null=True, blank=True)
    preview_image_link = models.CharField(max_length=200, null=True, blank=True)
    preview_description = MarkdownxField(null=True, blank=True)
    github_link = models.CharField(max_length=200, null=True, blank=True)
    external_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=("list of tags"), blank=True)

    class Meta:
        ordering = ('date', )

    @property
    def formatted_description_markdown(self):
        return markdownify(self.description)

    @property
    def formatted_preview_markdown(self):
        return markdownify(self.preview_description)

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('project-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

from django.db import models
from wagtail.snippets.models import register_snippet


@register_snippet
class Testimonial(models.Model):
    
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    quote = models.TextField(max_length=500, blank=False, null=False)
    testimonial_name = models.CharField(max_length=100, blank=False, null=False)
    testimonial_profession = models.CharField(max_length=100, blank=False, null=False)
     
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


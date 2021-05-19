from django.db import models
from wagtail.snippets.models import register_snippet


@register_snippet
class Testimonial(models.Model):
    
    quote = models.TextField(max_length=500, blank=False, null=False)
    testimonial_name = models.CharField(max_length=100, blank=False, null=False)
    testimonial_profession = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self) -> str:
        return f"{self.quote} by {self.testimonial_name}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
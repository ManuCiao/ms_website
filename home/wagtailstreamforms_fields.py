from django import forms
from wagtailstreamforms.fields import BaseField, register

@register('mytextarea')
class CustomTextAreaField(BaseField):
    # the form field class
    field_class = forms.CharField
    # the widget for the form field
    widget = forms.widgets.Textarea(attrs={'rows': 5})
    # the icon in the streamfield
    icon = 'placeholder'
    # the label to show in the streamfield
    label = 'Customised TextArea field'


@register('multiline')
class MultiLineTextField(BaseField):
    field_class = forms.CharField
    widget = forms.widgets.Textarea(attrs={'rows': 4})
import django_filters
from django import forms

from .models import Tag


class ItemFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.widgets.CheckboxSelectMultiple,
        label="Tags",
    )

    class Meta:
        model = Tag
        fields = ["tags"]

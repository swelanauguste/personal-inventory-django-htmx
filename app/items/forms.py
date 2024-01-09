from django import forms

from .models import Item, Tag


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
            "description": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }


class ItemFilterForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Tag.objects.all(),
        required=False,
    )

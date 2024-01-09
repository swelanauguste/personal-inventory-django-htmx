from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .filters import ItemFilter
from .forms import ItemCreateForm, ItemFilterForm
from .models import Item
from .utils import calculate_total_value

class ItemListView(ListView):
    model = Item
    form_class = ItemFilterForm

    def get_queryset(self):
        f = ItemFilter(self.request.GET, queryset=Item.objects.all())
        return f.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class(self.request.GET)
        context["total_value"] = calculate_total_value()
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if self.request.headers.get("HX-Request"):
            return render(request, "items/item_list_partial.html", context)
        return self.render_to_response(context)


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemCreateForm


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemCreateForm


class ItemDetailView(DetailView):
    model = Item

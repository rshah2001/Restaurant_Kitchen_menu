from django.shortcuts import render
from django.views import generic
from .models import Item, Meal_type


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = Meal_type
        return context


class MenuItemDetial(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"


class About(generic.TemplateView):
    template_name = "about.html"

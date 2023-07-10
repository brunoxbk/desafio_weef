from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from todo.models import Item
from todo.forms import ItemForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemList(LoginRequiredMixin, ListView):
    model = Item
    queryset = Item.objects.all()

    def get_queryset(self):
        queryset = self.model.objects.filter(created_by=self.request.user)
        return queryset


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('todo:list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super().form_valid(form)


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('todo:list')


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('todo:list')


class ItemCheck(RedirectView):
    permanent = False
    query_string = True
    url = reverse_lazy('todo:list')

    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs["pk"])
        item.checked = True
        item.save()
        return super().get_redirect_url(*args, **kwargs)

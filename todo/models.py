from django.db import models
from django.utils import timezone


class Item(models.Model):
    description = models.CharField(
        "Descrição", max_length=150, blank=False, null=False)
    checked = models.BooleanField("Feito", default=False)
    due_date = models.DateField("Data", blank=False, null=False)
    created = models.DateTimeField("Criado", auto_now_add=True)
    updated = models.DateTimeField("Alterado", auto_now=True)

    created_by = models.ForeignKey(
        'auth.User', verbose_name="Criador",
        on_delete=models.CASCADE,
        related_name='created_by', blank=False, null=False)

    @property
    def is_due(self):
        return self.due_date < timezone.now().date() and not self.checked

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"
        ordering = ['-pk']

    def __str__(self):
        return f"{self.pk} - {self.description} - {self.due_date}"

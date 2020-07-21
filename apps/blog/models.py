from django.contrib.auth import get_user_model
from django.db import models


class BlogPage(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="pages",
    )
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержимое")
    created = models.DateTimeField("Время создания", auto_now_add=True)
    updated = models.DateTimeField("Время обновления", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=False)

    def __str__(self):
        return f"Статья «{self.title}» ({self.user.username}, создано {self.created})"

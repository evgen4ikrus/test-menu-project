from django.db import models


class Menu(models.Model):
    title = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField('Название', max_length=100)
    menu = models.ForeignKey('Menu', verbose_name='Меню', on_delete=models.CASCADE, related_name='menu_items')
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский пункт меню',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title

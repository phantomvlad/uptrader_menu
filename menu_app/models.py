from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class MenuCategory(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    main_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, )
    category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.title

    def get_three(self):
        if not self.category:
            return [self]
        return self.category.get_three() + [self.category, self] if self.category else []


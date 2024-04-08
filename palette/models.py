import requests
from django.db import models

from users.models import User


class Palette(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'палитра'
        verbose_name_plural = 'палитры'
        ordering = ('pk',)


class Color(models.Model):
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE, related_name='colors')
    hex_code = models.CharField(max_length=7, verbose_name='HEX цвета')
    name = models.CharField(max_length=100, verbose_name='название', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.get_color_name()
        super().save(*args, **kwargs)

    def get_color_name(self):
        return get_color_name(self.hex_code)

    def __str__(self):
        return self.name

    def get_color_name(self):
        return get_color_name(self.hex_code)

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'
        ordering = ('pk',)


def get_color_name(hex_code):
    url = "https://www.thecolorapi.com/id"
    params = {
        "hex": hex_code,
        "format": "json"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

    try:
        data = response.json()
        if 'name' in data:
            color_name = data['name']['value']
            return color_name
        else:
            print("Не найдено название цвета")
            return None
    except Exception as e:
        print(f"Ошибка при анализе ответа: {e}")
        return None

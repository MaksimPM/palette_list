from rest_framework import serializers

from palette.models import Palette, Color


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = ['pk', 'name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['pk', 'palette', 'hex_code', 'name']

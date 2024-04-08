from rest_framework import permissions, generics
from rest_framework.generics import get_object_or_404

from palette.models import Palette, Color
from palette.serializers import PaletteSerializer, ColorSerializer


class PaletteListCreateView(generics.ListCreateAPIView):
    serializer_class = PaletteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Palette.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaletteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaletteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Palette.objects.filter(user=self.request.user)


class ColorListCreateView(generics.ListCreateAPIView):
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        palette_id = self.kwargs.get('palette_id')
        return Color.objects.filter(palette_id=palette_id)

    def perform_create(self, serializer):
        palette_id = self.kwargs.get('palette_id')
        palette = get_object_or_404(Palette, pk=palette_id)
        serializer.save(palette=palette)


class ColorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        palette_id = self.kwargs.get('palette_id')
        return Color.objects.filter(palette_id=palette_id)

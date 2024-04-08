from django.urls import path
from palette.apps import PaletteConfig
from palette.views import PaletteListCreateView, PaletteRetrieveUpdateDestroyView, ColorListCreateView, \
    ColorRetrieveUpdateDestroyView

app_name = PaletteConfig.name

urlpatterns = [
    path('list-create/', PaletteListCreateView.as_view(), name='palette_list_create'),
    path('list-update/<int:pk>/', PaletteRetrieveUpdateDestroyView.as_view(), name='palette_retrieve_update_destroy'),
    path('color-list-create/<int:palette_id>/colors/', ColorListCreateView.as_view(), name='color_list_create'),
    path('color-list-update/<int:palette_id>/colors/<int:pk>/', ColorRetrieveUpdateDestroyView.as_view(),
         name='color_retrieve_update_destroy'),
]

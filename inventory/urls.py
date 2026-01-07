from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ItemViewSet,
    export_items_pdf,
    export_items_excel,
    inventory_home
)

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    # Frontend home page
    path('', inventory_home, name='inventory-home'),

    # REST API
    path('api/', include(router.urls)),

    # Exports
    path('api/items/export/pdf/', export_items_pdf, name='export-pdf'),
    path('api/items/export/excel/', export_items_excel, name='export-excel'),
]

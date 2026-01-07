from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from openpyxl import Workbook
from django.shortcuts import render

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'quantity': ['gte', 'lte'],
        'price': ['gte', 'lte'],
    }


def inventory_home(request):
    return render(request, 'inventory/index.html')
def export_items_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="items_report.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 10)

    y = 800
    p.drawString(50, y, "ID | Name | Quantity | Price | Created At")
    y -= 20

    for item in Item.objects.all():
        p.drawString(
            50,
            y,
            f"{item.id} | {item.name} | {item.quantity} | {item.price} | {item.created_at.strftime('%Y-%m-%d')}"
        )
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.save()
    return response

def export_items_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Items"

    headers = ['ID', 'Name', 'Quantity', 'Price', 'Created At']
    ws.append(headers)

    for item in Item.objects.all():
        ws.append([
            item.id,
            item.name,
            item.quantity,
            float(item.price),
            item.created_at.strftime('%Y-%m-%d')
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="items_report.xlsx"'
    wb.save(response)

    return response
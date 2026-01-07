Inventory Management System (Django)

A full-stack Inventory Management System built with Django, Django REST Framework, SQLite, and a pure HTML/CSS/JavaScript frontend.
Includes REST APIs, PDF & Excel exports, filtering, pagination, and a simple UI.

- Features

    CRUD APIs for inventory items
    
    SQLite database (default Django DB)
    
    PDF export of items
    
    Excel export of items
    
    Filtering by quantity & price
    
    Pagination

    Pure HTML, CSS & JavaScript frontend (no frameworks)

- Tech Stack

    Python 3.x
    
    Django
    
    Django REST Framework
    
    SQLite
    
    ReportLab (PDF generation)
    
    OpenPyXL (Excel export)
    
    Vanilla HTML / CSS / JavaScript

- Setup Instructions
    - Clone the Repository
    git clone <your-repository-url>
    cd inventory_management
    
    - Create & Activate Virtual Environment (macOS)
    python3 -m venv venv
    source venv/bin/activate
    
    - Install Dependencies
    pip install django djangorestframework reportlab openpyxl django-filter
    
    - Run Database Migrations
    python manage.py makemigrations
    python manage.py migrate
    
    - Create Superuser (Optional – Admin Panel)
    python manage.py createsuperuser
    
    - How to Run the Server
    python manage.py runserver
    
    
    Access the application:
    
    Frontend UI
    http://127.0.0.1:8000/
    
    Admin Panel
    http://127.0.0.1:8000/admin/

- API Endpoints

    Base URL
    
    http://127.0.0.1:8000/api/
    
    - Create Item
    
    POST /api/items/
    
    {
      "name": "Laptop",
      "description": "MacBook Pro",
      "quantity": 5,
      "price": 1500.00
    }
    
    - Retrieve All Items
    
    GET /api/items/
    
    Supports pagination & filtering:
    
    /api/items/?quantity__gte=5&price__lte=2000
    
    - Retrieve Single Item
    
    GET /api/items/<id>/
    
    - Update Item
    
    PUT / PATCH /api/items/<id>/
    
    {
      "quantity": 10,
      "price": 1450.00
    }
    
    - Delete Item
    
    DELETE /api/items/<id>/
    
    - How to Test APIs
    
    You can test APIs using:
    
    Postman
    
    curl
    
    Browser (GET requests)
    
    Example (curl)
    curl http://127.0.0.1:8000/api/items/
    
    - PDF Report Generation
    Endpoint
    
    GET
    
    /api/items/export/pdf/
    
    Report Includes
    
    ID
    
    Name
    
    Quantity
    
    Price
    
    Created At
    
    - Downloaded file:
    
    items_report.pdf
    
    - Excel Export
    Endpoint
    
    GET
    
    /api/items/export/excel/
    
    Report Includes
    
    ID
    
    Name
    
    Quantity
    
    Price
    
    Created At

- Downloaded file:

    items_report.xlsx

- Frontend Usage

    Open browser at:
    
    http://127.0.0.1:8000/


    Add items using the form
    
    Edit or delete items from the table
    
    Export inventory using PDF or Excel buttons


- Notes
    
    SQLite is used by default (no configuration required)
    
    Suitable for development and demos
    
    Easily extendable with authentication, search, or UI frameworks

- Author

    Built with Django :)

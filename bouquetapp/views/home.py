import sqlite3
from django.shortcuts import render, redirect, reverse
from bouquetapp.models import Bouquet, model_factory
from .connection import Connection

def home(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Bouquet)
            db_cursor = conn.cursor()
            db_cursor.execute(""" 
                SELECT
                    b.id,
                    b.name,
                    b.occasion
                    FROM bouquetapp_bouquet b
                    ORDER BY b.name;
                """)

            bouquet_data = db_cursor.fetchall()

            template = 'home.html'
            context = {
                'bouquet_data' : bouquet_data
            }

            return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            db_cursor.execute("""
            INSERT INTO bouquetapp_bouquet
            (name, occasion
            )
            VALUES (?, ?)
            """,
                (form_data['name'], form_data['occasion']))
        return redirect(reverse('bouquetapp:home'))        
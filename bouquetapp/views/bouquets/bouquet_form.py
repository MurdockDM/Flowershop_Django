import sqlite3
from django.shortcuts import render, redirect, reverse
from bouquetapp.models import Bouquet, Flower, BouquetFlower, model_factory
from ..connection import Connection



def get_bouquets():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bouquet)
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
            SELECT 
                *
            FROM 
                bouquetapp_bouquet b
        """)

        return db_cursor.fetchall()


def create_bouquet_form(request):
    if request.method == 'GET':
        current_bouquets = get_bouquets()
        template = "bouquets/bouquet_form.html"            
        context = {
            "current_bouquets": current_bouquets
        }
        return render(request, template, context)
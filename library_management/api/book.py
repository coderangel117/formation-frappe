import frappe
from frappe import _
import json
from werkzeug.wrappers import Response


@frappe.whitelist(allow_guest=True)
def get_book_details(name):
    """Fetch book details from the database."""
    book_details = frappe.get_doc("Book", name)
    return {
        "title": book_details.title,
        "description": book_details.description,
        "isbn": book_details.isbn,
        "author": book_details.author,
    }


@frappe.whitelist(allow_guest=True, methods='GET')
def get_books():
    """Fetch all books from the database."""
    books = frappe.get_all("Book", fields=[
        "title",
        "description",
        "isbn",
        "author",
    ])
    return books

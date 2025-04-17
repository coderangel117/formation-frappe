import frappe
from frappe import _
import json


@frappe.whitelist(allow_guest=True)
def get_articles():
    if frappe.request.method != "GET":
        frappe.local.response["http_status_code"] = 405
        frappe.local.response["message"] = "Method Not Allowed"
        frappe.response.status_code = 405
        return
    return frappe.get_all("Article", fields=["article_name", "author", "status", "isbn"])


@frappe.whitelist(allow_guest=True)
def get_article(name):
    print(frappe.request.method)
    if frappe.request.method != "GET":
        frappe.local.response["http_status_code"] = 405
        frappe.local.response["message"] = "Method Not Allowed"
        return
    return frappe.get_doc("Article", name).as_dict()


@frappe.whitelist()
def create_article():
    if frappe.request.method != "POST":
        frappe.local.response["http_status_code"] = 405
        frappe.local.response["message"] = "Method Not Allowed"
    data = frappe.local.form_dict or json.loads(frappe.request.data)
    doc = frappe.get_doc({
        "doctype": "Article",
        "article_name": data.get("article_name"),
        "description": data.get("description"),
        "publisher": data.get("publisher"),
        "author": data.get("author"),
        "isbn": data.get("isbn"),
        "status": "Available"
    })
    doc.insert()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def update_article(name):
    data = frappe.local.form_dict or json.loads(frappe.request.data)
    doc = frappe.get_doc("Article", name)
    doc.update(data)
    doc.save()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def delete_article(name):
    frappe.delete_doc("Article", name)
    frappe.db.commit()
    return {"status": "ok"}

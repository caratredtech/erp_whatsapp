"""
PDF on Submit. Creates a PDF when a document is submitted.
Copyright (C) 2019  Raffael Meyer <raffael@alyf.de>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from cmath import pi
import frappe

from frappe import _
from frappe import publish_progress
from frappe.core.doctype.file.file import create_new_folder
from frappe.utils.file_manager import save_file
from tenacity import retry

@frappe.whitelist()
def attach_pdf(name,doctype,printformat,customer):
    fallback_language = frappe.db.get_single_value("System Settings", "language") or "en"
    print(customer)
    # mobile_response =get_mobile_number(customer)
    args = {
        "doctype": doctype,
        "name": name,
        "title": "Creating PDF",
        "lang": fallback_language,
        "printformat":printformat
    }

    response = execute(**args)
    return {"success":True,"file_name":frappe.utils.get_url()+"/files/"+response}

def get_customer_name():
    customer_name = frappe.db.sql("""select customer_name from `tabCustomer`""")


def execute(doctype, name, title, lang=None, show_progress=True,printformat=None):
    """
    Queue calls this method, when it's ready.

    1. Create necessary folders
    2. Get raw PDF data
    3. Save PDF file and attach it to the document
    """
    progress = frappe._dict(title=_("Creating PDF ..."), percent=0, doctype=doctype, docname=name)

    if lang:
        frappe.local.lang = lang

    if show_progress:
        publish_progress(**progress)

    doctype_folder = create_folder(_(doctype), "Home")
    title_folder = create_folder(title, doctype_folder)

    if show_progress:
        progress.percent = 33
        publish_progress(**progress)

    pdf_data = get_pdf_data(doctype, name,printformat)

    if show_progress:
        progress.percent = 66
        publish_progress(**progress)

    file_name =  save_and_attach(pdf_data, doctype, name, title_folder)

    if show_progress:
        progress.percent = 100
        publish_progress(**progress)
    return file_name


def create_folder(folder, parent):
    """Make sure the folder exists and return it's name."""
    new_folder_name = "/".join([parent, folder])
    
    if not frappe.db.exists("File", new_folder_name):
        create_new_folder(folder, parent)
    
    return new_folder_name


def get_pdf_data(doctype, name,print_format):
    """Document -> HTML -> PDF."""
    html = frappe.get_print(doctype, name,print_format)
    return frappe.utils.pdf.get_pdf(html)


def save_and_attach(content, to_doctype, to_name, folder):
    """
    Save content to disk and create a File document.

    File document is linked to another document.
    """
    file_name = "{}.pdf".format(to_name.replace(" ", "-").replace("/", "-"))
    # save_file(fname, content, dt, dn, folder=None, decode=False, is_private=0, df=None):
    save_file(file_name, content, to_doctype,
              to_name, folder=folder, is_private=0)
    return file_name

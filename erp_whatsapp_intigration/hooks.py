from . import __version__ as app_version

app_name = "erp_whatsapp_intigration"
app_title = "Erp Whatsapp Intigration"
app_publisher = "caratred"
app_description = "WhatsAPP"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "infor@caratred.com"
app_license = "MIT"


fixtures = [
    {
        "dt":
        "Custom Field",
        "filters": [[
            "name",
            "in",
            ["Contact-whatsapp_enabled"]]]}]



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erp_whatsapp_intigration/css/erp_whatsapp_intigration.css"
app_include_js = "/assets/erp_whatsapp_intigration/js/whatsapp_button.js"

# include js, css files in header of web template
# web_include_css = "/assets/erp_whatsapp_intigration/css/erp_whatsapp_intigration.css"
# web_include_js = "/assets/js/page.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erp_whatsapp_intigration/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/page.js"}

# include js in doctype views
# doctype_js = {"Sales Invoice" : "public/js/sales_invoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erp_whatsapp_intigration.install.before_install"
# after_install = "erp_whatsapp_intigration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erp_whatsapp_intigration.uninstall.before_uninstall"
# after_uninstall = "erp_whatsapp_intigration.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erp_whatsapp_intigration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erp_whatsapp_intigration.tasks.all"
# 	],
# 	"daily": [
# 		"erp_whatsapp_intigration.tasks.daily"
# 	],
# 	"hourly": [
# 		"erp_whatsapp_intigration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erp_whatsapp_intigration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erp_whatsapp_intigration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erp_whatsapp_intigration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erp_whatsapp_intigration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erp_whatsapp_intigration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"erp_whatsapp_intigration.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []

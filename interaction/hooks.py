# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "interaction"
app_title = "Interaction"
app_publisher = "DIgitalPrizm Infotech"
app_description = "Manages Interactions with customers"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "contact@digitalprizm"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/interaction/css/interaction.css"
# app_include_js = "/assets/interaction/js/interaction.js"

# include js, css files in header of web template
# web_include_css = "/assets/interaction/css/interaction.css"
# web_include_js = "/assets/interaction/js/interaction.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
fixtures = ["Custom Field","Property Setter","Custom Script","Print Format"]
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "interaction.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "interaction.install.before_install"
# after_install = "interaction.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "interaction.notifications.get_notification_config"

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
# 		"interaction.tasks.all"
# 	],
# 	"daily": [
# 		"interaction.tasks.daily"
# 	],
# 	"hourly": [
# 		"interaction.tasks.hourly"
# 	],
# 	"weekly": [
# 		"interaction.tasks.weekly"
# 	]
# 	"monthly": [
# 		"interaction.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "interaction.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "interaction.event.get_events"
# }


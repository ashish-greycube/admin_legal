from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	config = [
		{
			"label": _("System Administrator"),
			"items": [
				{
					"type": "doctype",
					"name": "DocType",
					"description": _("DocType")
				}			
			]
		}
		]
	return config
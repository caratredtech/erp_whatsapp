// Copyright (c) 2022, caratred and contributors
// For license information, please see license.txt

frappe.ui.form.on('Configuration', {
	setup: function (frm) {
		frm.set_query("document_type", function () {
			return {
				filters: [
					["DocType", "name", "in", "Purchase Order,Purchase Invoice,Sales Invoice"]
				]
			}
		});
	}
});
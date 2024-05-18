/ Copyright (c) 2022, kiran@caratred.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Invoice', {
    refresh: function (frm) {
        if (frm.doc.docstatus == 1) {
            frm.add_custom_button(__('Send Via WhatsAPP'), (frm) => {
                // get_print_format(frm)

                frappe.db.get_list('Print Format', {
                    fields: ["`tabPrint Format`.`name`", "`tabPrint Format`.`owner`", "`tabPrint Format`.`creation`", "`tabPrint Format`.`modified`", "`tabPrint Format`.`modified_by`", "`tabPrint Format`.`_user_tags`", "`tabPrint Format`.`_comments`", "`tabPrint Format`.`_assign`", "`tabPrint Format`.`_liked_by`", "`tabPrint Format`.`docstatus`", "`tabPrint Format`.`parent`", "`tabPrint Format`.`parenttype`", "`tabPrint Format`.`parentfield`", "`tabPrint Format`.`idx`", "`tabPrint Format`.`doc_type`", "`tabPrint Format`.`disabled`"],
                    filters: [["Print Format", "doc_type", "=", "Sales Invoice"]],
                }).then((response) => {
                    console.log(response)
                    if (response) {
                        let printformats = []
                        response.forEach(data => {
                            printformats.push(data.name)
                        })

                        get_print_format(frm, printformats)
                    }
                }).catch((err) => {
                    console.log(err)
                })

            })

        }

    }
});




const get_customer_mobile_number = (callback) => {
    let phone_number = ""
    try {
        frappe.db.get_list('Contact', {
            fields: ["*"],
            filters: [["Contact", "name", "like", `%${cur_frm.doc.customer}%`]],
        }).then((response) => {
            console.log(response)
            if (response) {
                console.log(response)
                // let printformats = []
                response.some(data => {
                    if (data.is_primary_contact == 1) {
                        phone_number = data.mobile_no
                        return true
                    }

                })
                // get_print_format(frm, printformats)
            }
            console.log(phone_number)
            callback(phone_number)
        }).catch((err) => {
            console.log(err)
        })
    }
    catch (err) {
        console.log(err)
    }
}


const get_print_format = function (frm, printformats = []) {
    try {
        let get_link = true
        let text = ' ';

        console.log(cur_frm)
        let dialog = new frappe.ui.Dialog({
            title: 'Choose Invoice Template',
            fields: [
                {
                    label: 'Formats',
                    fieldname: 'print_formats',
                    fieldtype: 'Select',
                    length: 13,
                    options: printformats,
                },
                {
                    label: 'Phone Number',
                    fieldname: 'phone_number',
                    fieldtype: 'Data',
                    length: 13,
                    reqd: 1,
                },
                {
                    label: 'Message',
                    fieldname: 'message',
                    fieldtype: 'Small Text',
                    length: 13,
                    default: "Dear {Customer name} your Invoice {Invoice Number} is avaliable via the below link {Invoice link}. \n * please note link will not valid after 30 days. \n-{Company Name}."
                },
            ],
            primary_action_label: 'Submit',
            primary_action(values) {
                console.log(values)
                if (get_link == true) {
                    frappe.call({
                        method: "erp_whatsapp_intigration.public.python.generate_pdf.attach_pdf",
                        args: {
                            name: cur_frm.doc.name,
                            doctype: "Sales Invoice",
                            printformat: values.print_formats,
                            customer: cur_frm.doc.customer,
                        }
                        , callback: function (message) {

                            console.log(message)
                            // let text = `Dear ${cur_frm.doc.customer_name} your Invoice ${cur_frm.doc.name} is avaliable via the below link ${message.message.file_name}. \n * please note link will not valid after 30 days. \n-Daimond Modular.`
                            text = values.message.replace("{Customer name}", cur_frm.doc.customer_name).replace("{Invoice Number}", cur_frm.doc.name).replace("{Invoice link}", message.message.file_name).replace("{company name}",cur_frm.doc.company)
                            dialog.fields_dict.message.set_value(text);
                            dialog.fields_dict.message.refresh();

                            get_link = false
                            // values.message = text
                            // dialog.hide()
                            // this.hide()
                            // show_message(text)
                        }
                    })
                }
                else {
                    window.open("https://api.whatsapp.com/send?phone=91" + values.phone_number + "&text=" + text + "&source=&data=")
                    dialog.hide()
                }


            }
        });

        dialog.show()
        get_customer_mobile_number((text) => {
            dialog.fields_dict.phone_number.set_value(text);
            dialog.fields_dict.phone_number.refresh();
        })
    }
    catch (err) {
        console.log(err)
    }
}


const show_message = (message) => {
    let message_dialog = new frappe.ui.Dialog({
        title: 'Message',
        fields: [
            {
                label: 'Message',
                fieldname: 'message',
                fieldtype: 'Small Text',
                length: 13,
                default: message
            },

        ],
        primary_action_label: 'Submit',
        primary_action(values) {
            window.open("https://api.whatsapp.com/send?phone=91" + values.phone_number + "&text=" + values.message + "&source=&data=")
            this.hide()
            
        }
    });

    message_dialog.show()
}



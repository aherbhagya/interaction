from __future__ import unicode_literals
import frappe, json
import frappe.desk.form.meta
import frappe.desk.form.load

from frappe import _


@frappe.whitelist()
def ping():
	print("s")
	return 1
# @frappe.whitelist()
# def add_expense(exp_approver,expense_date,expense_type,description,claim_amount,sanctioned_amount,employee):
# 	print("aas")
# 	expense = frappe.new_doc("Expense Claim")
# 	expense.exp_approver=exp_approver
# 	expense.expense_date=expense_date
# 	expense.expense_type=expense_type
# 	expense.description=description
# 	expense.claim_amount=claim_amount
# 	expense.sanctioned_amount=sanctioned_amount
# 	expense.employee=employee
# 	expense.insert(ignore_permissions=True)
# 	expense.insert()
# 	frappe.msgprint("Expense added successfully!..")

# @frappe.whitelist()
# def add_expense():
# 	expense = frappe.new_doc("Expense Claim")
# 	expense.exp_approver=exp_approver
# 	expense.expense_date=expense_date
# 	expense.expense_type=expense_type
# 	expense.description=description
# 	expense.claim_amount=claim_amount
# 	expense.sanctioned_amount=sanctioned_amount
# 	expense.employee=employee
# 	expense.insert(ignore_permissions=True)
# 	expense.save(ignore_permissions=True)
# 	frappe.db.commit()
# 	return {"Expense added successfully!.."}

@frappe.whitelist()
def add_expense(exp_approver='',employee='',employee_name=''):
	print("hello")
	"""allow any logged user to post toDo via interaction master"""
	expense = frappe.new_doc("Expense Claim")
	print("in")
	expense.exp_approver=exp_approver
	# expense.expense_date=expense_date
	# expense.expense_type=expense_type
	# expense.description=description
	# expense.claim_amount=claim_amount
	# expense.sanctioned_amount=sanctioned_amount
	expense.employee=employee
	expense.employee_name=employee_name
	expense.insert(ignore_permissions=True)
	expense.save(ignore_permissions=True)
	frappe.db.commit()
	# frappe.msgprint("Error...............")
	return expense
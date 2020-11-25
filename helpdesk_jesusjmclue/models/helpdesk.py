from odoo import models, fields

class HelpdeskTicket(models.Model):
	_name = 'helpdesk.ticket'
	_description = "Helpdesk Ticket"

	name = fields.Char(
		string = 'Name',
		required = True)
	description = fields.Text(
		string = 'Description')
	date = fields.Date(
		string = 'Date')

	state = fields.Selection(
		[('new', 'New'),
		 ('assigned', 'Assigned'),
		 ('progress', 'In Progress'),
		 ('waiting', 'Waiting'),
		 ('done', 'Done'),
		 ('cancelled', 'Cancelled')],
		string = 'State',
		default = 'new')

	dedicated_time = fields.Float(
		string = 'Time')

	assigned = fields.Boolean(
		string = 'Assigned',
		readonly = True)

	due_date = fields.Date(
		string = 'Due Date')

	corrective_action = fields.Html(
		help = 'Detail of corrective action after this issue')

	preventive_action = fields.Html(
		help = 'Detail of preventive action after this issue')

	def set_assigned_multi(self):
		for ticket in self:
			ticket.set_assigned()

	def set_assigned(self):
		self.ensure_one()
		self.write({
			'assigned' : True,
			'state' : 'assigned',
		})

	def set_progress(self):
		self.ensure_one()
		self.state = 'progress'

	def set_waiting(self):
		self.ensure_one()
		self.state = 'waiting'

	def set_done(self):
		self.ensure_one()
		self.state = 'done'

	def set_cancel(self):
		self.ensure_one()
		self.state = 'cancelled'

	

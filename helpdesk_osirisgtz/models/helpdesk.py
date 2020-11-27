from odoo import models, fields


class HelpdeskTicket (models.Model):
    """   """
    _name = 'helpdesk.ticket'
    _description = "Helpdesk Ticket"

    name = fields.Char(
            'Name',
            required=True)
    description = fields.Text(
            'Description')
    date = fields.Date( 'Date' )

    state = fields.Selection(
            [('new','New'),
             ('assigned','Assigned'),
             ('in_progress', 'In Progress'),
             ('pendign', 'Pending'),
             ('done', 'Done'),
             ('cancel','Cancel')],
            default = 'new')

    dedicated_time = fields.Float('Time')

    assigned = fields.Boolean(
            readonly= True )

    due_date = fields.Date('Due Date')

    corrective_action = fields.Html(
            help = 'To add all actions taken to fix the issue'
            )
    preventive_action = fields.Html(
            help = 'To add actions to prevent the issue to happen')


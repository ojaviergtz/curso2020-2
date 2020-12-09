from odoo import fields, models

class HelpdeskTicket (models.Model):
    _name = 'helpdesk.ticket'
    _description = 'HelpDesk Ticket'

    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
    date = fields.Date(
        string='Date',
    )
    state = fields.Selection(
        [
            ('new', 'New'),
            ('assigned', 'Assigned'),
            ('progress', 'Progress'),
            ('waiting', 'Waiting'),
            ('done', 'Done'),
            ('cancel', 'Cancel'),
        ],
        string='Date',
        default='new',
    )
    dedicated_time = fields.Float(
        string='Time',
    )
    assigned = fields.Boolean(
        string='Assigned',
        readonly=True,
    )
    due_date = fields.Date(
        string='Due Date',
    )
    corrective_action =fields.Html(
        help='Default of corrective action after this issue',
    )
    preventive_action =fields.Html(
        help='Default of preventive action after this issue',
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to',
    )



    def set_assigned_multi(self):
        for ticket in self:
            ticket.set_assigned()

    def set_assigned(self):
        self.ensure_one()
        self.write(
            {
                'assigned': True,
                'state': 'assigned',
                'user_id': self.env.user.id,
            }

        )

    def set_progress(self):
        self.ensure_one()
        self.state = 'progress'

    def set_waiting(self):
        self.ensure_one()
        self.state = 'waiting'

    def set_cancel(self):
        self.ensure_one()
        self.state = 'cancel'

    def set_done(self):
        self.ensure_one()
        self.state = 'done'
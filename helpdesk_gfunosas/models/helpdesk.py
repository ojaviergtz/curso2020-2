# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpDeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

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
    user_id = fields.Many2one(
        "res.users",
        string="Assigned to",
    )

    state = fields.Selection(
        [
            ('new', 'New'),
            ('assigned', 'Assigned'),
            ('progress', 'Progress'),
            ('waiting', 'Waiting'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ],
        string="State",
        default="new",
    )
    dedicated_time = fields.Float(
        string='Time',
    )
    assigned = fields.Boolean(
        string='Assigned',
        readonly=True,
    )
    date_due = fields.Date(
        string="Date Due",
    )
    corrective_action = fields.Html(
        help='Detail of corrective action after this issue',
    )
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue',
    )

    def set_assigned_multi(self):
        for ticket in self:
            ticket.set_assigned()

    def set_assigned(self):
        self.ensure_one()
        self.write({
            'assigned': True,
            'state': 'assigned',
            'user-id': self.env.user.id # ID integer
            })
        # "self.user" --> RecordSet

    def set_progress(self):
        self.ensure_one()
        self.state = 'progress'

    def set_waiting(self):
        self.ensure_one()
        self.state = 'waiting'

    def set_done(self):
        self.ensure_one()
        self.state = 'done'

    def set_cancelled(self):
        self.ensure_one()
        self.state = 'cancelled'
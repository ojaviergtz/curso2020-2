from odoo import models, fields


class HelpdeskTicket (models.Model):
    """   """
    _name = 'helpdesk.ticket'
    _description = "Helpdesk Ticket"

    name = fields.Char(
            'Name')
    description = fields.Text(
            'Description')
    date = fields.Date( 'Date' )

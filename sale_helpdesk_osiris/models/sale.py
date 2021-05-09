from odoo import models, fields


class Sale (models.Model):
    """  """
    _inherit = "sale.order"

    ticket_id = fields.One2many(
            comodel_name='helpdesk.ticket',
            inverse_name='sale_ids',
            string='Tickets lines',
            )

from odoo import models, fields


class SaleHelpdestTicket(models.Model):
    """   """
    _inherit = "helpdesk.ticket"

    sale_ids = fields.Many2one(
            comodel_name='sale.order',
            # inverse_name="ticket_id",
            string='Ticket'
            )

from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    helpdesk_tag_id = fields.Many2one(comodel_name='helpdesk.tag',
                                      string='Helpdesk Tag')

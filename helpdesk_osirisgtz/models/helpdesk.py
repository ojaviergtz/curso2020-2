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
             ('pending', 'Pending'),
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

    user_id = fields.Many2one(
            comodel_name = 'res.users',
            string = 'Assigned to')

    # Methods
    def btn_assigned(self):
        """"""
        self.ensure_one()
        self.write({
            'state':'assigned',
            'assigned': True,
            'user_id': self.env.user.id
            })

    def btn_progress(self):
        """  """
        self.ensure_one()
        self.state = 'in_progress'

    def btn_pending(self):
        """  """
        self.ensure_one()
        self.state = 'pending'

    def btn_done(self):
        """  """
        self.ensure_one()
        self.state = 'done'

    def btn_cancel(self):
        """  """
        self.ensure_one()
        self.state = 'cancel'


##Añadir en el header los siguiente botones:
##
##    Asignar, cambia estado a asignado y pone a true el campo asignado, visible sólo con estado = nuevo
##    En proceso, visible sólo con estado = asignado
##    Pendiente, visible sólo con estado = en proceso o asignado
##    Finalizar, visible en cualquier estado, menos cancelado y finalizado
##    Cancelar, visible si no está cancelado
##
##Cada botón pondrá el objeto en el estado correspondiente.

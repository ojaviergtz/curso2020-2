from odoo import models, fields, api


class HelpdeskTicketAction(models.Model):
    """  """
    _name= 'helpdesk.ticket.action'
    _description= " Model to define all Actions in tickets"

    name = fields.Char(
            'Name')
    date = fields.Date(
            'Date')
    ticket_id = fields.Many2one(
            comodel_name='helpdesk.ticket')

class HelpdeskTags(models.Model):
    """   """
    _name = 'helpdesk.tag'
    _description = " Model to define tags to helpdesk tickets"

    name = fields.Char('Name')
    ticket_ids = fields.Many2many(
            comodel_name= 'helpdesk.ticket',
            relation= 'helpdesk_ticket_tag_rel',
            column1= 'tag_id',
            column2= 'ticket_id',
            string="Tickets")


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
            compute="_compute_assigned")

    due_date = fields.Date('Due Date')

    corrective_action = fields.Html(
            help = 'To add all actions taken to fix the issue'
            )
    preventive_action = fields.Html(
            help = 'To add actions to prevent the issue to happen')

    user_id = fields.Many2one(
            comodel_name = 'res.users',
            string = 'Assigned to')

    action_ids = fields.One2many(
            comodel_name='helpdesk.ticket.action',
            inverse_name='ticket_id',
            string='Actions')
    tag_ids = fields.Many2many(
            comodel_name= 'helpdesk.tag',
            relation= 'helpdesk_ticket_tag_rel',
            column1='ticket_id',
            column2= 'tag_id',
            string='Tags')

    tickets_for_user = fields.Integer(
            string='Tickets for user assigned',
            compute="_compute_tickets_for_user")

    tag_generator = fields.Char(
            string= 'Add new Tag')


    # Methods
    def create_new_tag(self):
        """   """
        self.ensure_one()
        if self.tag_generator:
            new_tag = self.env['helpdesk.tag'].create({
                'name': self.tag_generator,
                #'ticket_ids':[(4,self.id,0)]
                })
            #self.write({'tag_ids': [(4,new_tag.id,0)]})
            self.tag_ids += new_tag # This works in this odoo version

    @api.depends('user_id')
    def _compute_tickets_for_user(self):
        """  """
        for ticket in self:
            user = ticket.user_id
            all_tickets = self.env['helpdesk.ticket'].search([
                ('user_id', '=', user.id)
                ])
            ticket.tickets_for_user = len(all_tickets)

    @api.depends('user_id')
    def _compute_assigned(self):
        """  """
        for ticket in self:
            ticket.assigned = ticket.user_id and True

    def btn_assigned(self):
        """"""
        self.ensure_one()
        self.write({
            'state':'assigned',
            #'assigned': True,
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


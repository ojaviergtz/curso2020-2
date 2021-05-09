from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestHelpdesk(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestHelpdesk, self).setUp(*args, **kwargs)
        self.Test_ticket = self.env.ref('helpdesk_osirisgtz.helpdesk_demo_1')

        self.DemoUser = self.env['res.users'].create({
            'login': 'testuser',
            'partner_id': self.env['res.partner'].create({
                'name': 'Partner demo'
                }).id,
            })
        tmp_group = self.env['res.groups'].search([
            ('category_id.name', '=', 'Helpdesk'),
            ('name', '=', 'User')]).users
        tmp_group = [(4, self.DemoUser.id)]
        self.env.uid = self.DemoUser.id

        print("--->", self.DemoUser, tmp_group)

    def test_00_raise_axception(self):
        """"""
        with self.assertRaises(ValidationError) as e:
            self.Test_ticket.dedicated_time = -1

    def test_05_raise_create(self):
        """  """
        new_ticket = self.env['helpdesk.ticket'].create({
            'description': "Description TEST",
            'name': "Ticked 2",
            })
        self.assertEqual(new_ticket.create_uid.id, self.env.uid)

# Copyright 2020 Analistas Cooffee
#   Enrique López de Roda López - e.lrl@hotmail.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Enrique Lopez",
    "summary": "Helpdesk and Tickets",
    "description":"""
Helpdesk
========
Módulo de prueba de Helpdesk curso Aeodoo
    """,
    "version": "13.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/Helpdesk",
    "author": "Analistas Cooffee, Odoo Community Association (OCA)",
    "maintainers": ["e-lrl"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
    'security/helpdesk_security.xml',
    'security/ir.model.access.csv',
    'views/helpdesk_ticket_views.xml',
    ],
    "demo": [
    ],
}

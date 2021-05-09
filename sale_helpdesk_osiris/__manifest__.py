# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Helpdesk Osiris Gutierrez",
    "summary": "Sale Helpdesk module created for the AEODOO course 2020-2",
    "description": """
    SALE HELPDESK
    ===
    Detail description for the module developed in the __AEODOO course 2020-2__
    """,
    "version": "13.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "AEODOO, Odoo Community Association (OCA)",
    "maintainers": ["osiris"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ["base",
                "sale_management",
                "helpdesk_osirisgtz", ],
    "data": [
        "views/sale_views.xml",
        "views/helpdesk_ticket_views.xml",
    ],
    "demo": [
    ]
}

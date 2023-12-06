from odoo import models, fields


class SaleCommission(models.Model):
    _name = "sale.commission"
    _description = "SAles Commission Model"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    date = fields.Date(string='Date')
    priority = fields.Integer(string='Priority')
    percent = fields.Float(string='Percent Value')
    notes = fields.Html(string='Notes')
    state = fields.Selection(
        [('draft', 'Draft'),
         ('done', 'Done'),
         ('rejected', 'Rejected')], string='draft', default='draft')

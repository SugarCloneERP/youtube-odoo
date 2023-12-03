from odoo import models, fields


class SaleCommission(models.Model):
    _name = "sale.commission"
    _description = "SAles Commission Model"

    name = fields.Char(string='Name')

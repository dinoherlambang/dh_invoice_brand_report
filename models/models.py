from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    brand_id = fields.Many2one(related='product_tmpl_id.product_brand_id', string='Brand', store=True)

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    brand_id = fields.Many2one(related='product_id.brand_id', string='Brand', store=True)

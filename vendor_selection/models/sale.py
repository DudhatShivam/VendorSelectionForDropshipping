# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, AccessError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    vendor_id = fields.Many2one('product.supplierinfo', 'Vendor')
    is_route = fields.Boolean('Is Route', defualt=False)
    
    @api.multi
    @api.onchange('route_id')
    def _onchange_route_id(self):
        if self.route_id:
            self.is_route = True
            
class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    def _make_po_select_supplier(self, values, suppliers):
        """ Method intended to be overridden by customized modules to implement any logic in the
            selection of supplier.
        """
        print "\n\n values-------", values
        print "\n\n rioute ids----",  values.get('route_ids')
        if values.get('route_ids'):
            so = self.env['sale.order.line'].browse(values.get('sale_line_id'))
            supplier = so.vendor_id or suppliers[0]
            
            return supplier
        else:
            return super(ProcurementRule, self)._make_po_select_supplier(values, suppliers)
                     
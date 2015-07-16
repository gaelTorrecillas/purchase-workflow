# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################
from openerp.osv import fields, orm


class PurchaseLineInvoice(orm.TransientModel):
    _inherit = 'purchase.order.line_invoice'

    def makeInvoices(self, cr, uid, ids, context=None):
        po_line_obj = self.pool['purchase.order.line']
        record_ids = context.get('active_ids', [])
        line_ids = [line.id for line in po_line_obj.browse(
            cr, uid, record_ids, context=context)
            if line.state != 'cancel']
        context.update({'active_ids': line_ids})
        return super(PurchaseLineInvoice, self).makeInvoices(
            cr, uid, ids, context=context)

# -*- coding: utf-8 -*-

#charges.py

from odoo import models, fields, api

class hoteldocuments(models.Model):
    _name = 'hotel.documents'
    _description = 'hotel documents'
    _order = "name"
    
    name = fields.Char("Document Name")
    description = fields.Char("Document Description")
from odoo import models, fields # type: ignore

class Medicamento(models.Model):
    _name = 'medicamento'
    _description = 'Gestión de Medicamentos'
    
    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio')
    stock = fields.Integer(string='Stock')
    fecha_expiracion = fields.Date(string='Fecha de Expiración')
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('agotado', 'Agotado')
    ], string="Estado", default="disponible")
    caducidad = fields.Datetime(string="Fecha y hora de Caducidad")  # Nuevo Campo
    es_alergico = fields.Boolean(string='es alergico?',default=False)
    laboratorio_id = fields.Many2one('medicamento.laboratorio', string='Laboratorio')

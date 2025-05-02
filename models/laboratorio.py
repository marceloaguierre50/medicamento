from odoo import models, fields # type: ignore

class Laboratorio(models.Model):
    _name = 'medicamento.laboratorio'  # Nombre técnico del modelo
    _description = 'Laboratorio'

    name = fields.Char(string='Nombre', required=True)
    medicamento_ids = fields.One2many('medicamento.medicamento', 'laboratorio_id', string='Medicamentos')

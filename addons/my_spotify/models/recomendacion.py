# -*- coding: utf-8 -*-
"""
Prueba Desarrollador Python - OMNI.PRO
Adrian Cuero
andretti86@gmail.com

* Integración Odoo + Spotify *
"""
from odoo import models, fields



class SpotifyRecomendacion(models.TransientModel):
    """
    Clase que representa una canción.
    """
    _name = 'spotify.recomendacion'
    
    cancion_id = fields.Many2one('spotify.cancion', string='Canción')
    cliente_id = fields.Many2one('spotify.cliente', String='Cliente')


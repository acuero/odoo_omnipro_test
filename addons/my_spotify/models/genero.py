# -*- coding: utf-8 -*-
"""
Prueba Desarrollador Python - OMNI.PRO
Adrian Cuero
andretti86@gmail.com

* Integración Odoo + Spotify *
"""
# Odoo
from odoo import models, fields, api


# Utilidades
import logging
_logger = logging.getLogger(__name__)



class SpotifyGenero(models.Model):
    """
    Clase que representa un género musical.
    """
    _name = 'spotify.genero'
    name = fields.Char('Nombre', required=True)



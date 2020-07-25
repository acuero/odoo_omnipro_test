# -*- coding: utf-8 -*-
"""
Prueba Desarrollador Python - OMNI.PRO
Adrian Cuero
andretti86@gmail.com

* Integración Odoo + Spotify *
"""
from odoo import models, fields



class SpotifyCancion(models.Model):
    """
    Clase que representa una canción.
    """
    _name = 'spotify.cancion'
    name        = fields.Char('Canción', required=True)
    spotify_id  = fields.Char('Spotify ID', required=True)
    spotify_uri = fields.Char('Spotify URI', required=True)
    url_externa = fields.Char('URL Externa', required=True)


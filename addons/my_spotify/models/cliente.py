# -*- coding: utf-8 -*-
"""
Prueba Desarrollador Python - OMNI.PRO
Adrian Cuero
andretti86@gmail.com

* Integración Odoo + Spotify *
"""
# Odoo
from odoo import models, fields, api


# Models
from .genero import SpotifyGenero


# Utilidades
from .spotify import Spotify
import logging
_logger = logging.getLogger(__name__)



class SpotifyCliente(models.Model):
    """
    Clase que representa una canción recomendada.
    """
    _name = 'spotify.cliente'
    name            = fields.Char('Nombres', required=True)
    apellidos       = fields.Char('Apellidos', required=True)
    email           = fields.Char('E-mail', required=True)
    generos_ids     = fields.Many2many('spotify.genero', string='Géneros musicales')
    recomendaciones = fields.One2many('spotify.recomendacion', 'cliente_id', String='Canciones recomendadas')
    



    @api.model
    def create(self, vals_list):
        cambios   = self.validacion_cambios_generos(vals_list)
        resultado = super(SpotifyCliente, self).create(vals_list)

        if cambios:
            self.recomendar_canciones(resultado)
        
        return resultado
    



    def write(self, vals_list):
        cambios   = self.validacion_cambios_generos(vals_list)
        resultado = super(SpotifyCliente, self).write(vals_list)
        if cambios:
            self.recomendar_canciones(vals_list)
        
        return resultado




    def validacion_cambios_generos(self, vals_list):
        """
        Método que valida si han variado los géneros musicales seleccionados.
        """
        if 'generos_ids' not in vals_list:
            return False

        

        previos = self.generos_ids.ids
        nuevos  = vals_list['generos_ids'][0][2]
        diff    = list(set(previos) ^ set(nuevos))
        cambios = True if diff else False

        return cambios




    def recomendar_canciones(self, vals_list):
        """
        Método que obtiene los recomendados desde el api de spotify.
        """
        seed_genres    = self.obtener_spotify_seed_genres(vals_list.generos_ids.ids)
        spotify        = Spotify()
        spotify_tracks = spotify.obtener_recomendados(seed_genres)
        
        recomendados = []
        if spotify_tracks:
            for track in spotify_tracks:
                cancion = self.env['spotify.cancion'].search([('spotify_id', '=', track['id'])], limit=1)

                if not cancion:
                    cancion = self.env['spotify.cancion'].create({
                        'name'       : track['name'],
                        'spotify_id' : track['id'],
                        'spotify_uri': track['uri'],
                        'url_externa': track['external_urls']['spotify'],
                    })

                recomendacion = self.env['spotify.recomendacion'].create({
                    'cancion_id': cancion.id,
                    'cliente_id': vals_list.id
                })

                recomendados.append(recomendacion.id)
        
        
        if len(recomendados) > 0:
            self.recomendaciones = [(6, 0, recomendados)]




    def obtener_spotify_seed_genres(self, generos_ids):
        """
        Método que retorna seed (string formateado) para consulta de recomendados.
        """
        generos_models = self.env['spotify.genero'].search([('id', 'in', tuple(generos_ids))])
        generos        = [genero.name for genero in generos_models]
        seed_genres    = ",".join(generos)

        _logger.debug("obtener_spotify_seed_genres.generos_ids: %s", generos_ids)
        _logger.debug("obtener_spotify_seed_genres.seed_genres: %s", seed_genres)

        return seed_genres








    

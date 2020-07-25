# -*- coding: utf-8 -*-
"""
Prueba Desarrollador Python - OMNI.PRO
Adrian Cuero
andretti86@gmail.com

* Integración Odoo + Spotify *
"""
# Python
import requests
import base64
import os


# Utilities
import logging
_logger = logging.getLogger(__name__)




class Spotify():
    """
    Clase que manipula api de spotify.
    """
    CLIENT_ID             = '37b6497961ee467fa01a40af3ecb6153'
    CLIENT_SECRET         = '75a4c5802eaa4ba3a9fc08b7a47c80cb'
    GET_TOKEN_URL         = 'https://accounts.spotify.com/api/token'
    GENEROS_ENDPOINT      = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'
    RECOMENDADOS_ENDPOINT = 'https://api.spotify.com/v1/recommendations'
    LIMITE_RECOMENDADOS   = 10
    


    def __init__(self):
        self.headers = {}
        self.data    = {}
        self.token   = None

        self.generar_autorizacion()
    
    


    def generar_autorizacion(self):
        """
        Método que obtiene token para uso de api.
        """
        try:
            response = requests.post(
                self.GET_TOKEN_URL, 
                {
                    'grant_type'   : 'client_credentials',
                    'client_id'    : self.CLIENT_ID,
                    'client_secret': self.CLIENT_SECRET,
                }
            )
            response.raise_for_status()
            if response.ok:
                response_data = response.json()
                token         = response_data['access_token']
                self.token    = token
        
        except requests.exceptions.Timeout as e:
            _logger.debug("response.Timeout.error: {}".format(e.response.text))
        except requests.exceptions.TooManyRedirects as e:
            _logger.debug("response.TooManyRedirects.error: {}".format(e.response.text))
        except requests.exceptions.RequestException as e:
            _logger.debug("response.RequestException.error: {}".format(e.response.text))
        except requests.exceptions.HTTPError as e:
            _logger.debug("response.HTTPError.error: {}".format(e.response.text))




    def obtener_recomendados(self, seed_genres):
        """
        Método que obtiene los recomendados de spotify dado los nombres clave de unos géneros.
        """
        if not self.token:
            return None
        

        if not seed_genres:
            return None
        
        
        self.headers = {
            'Authorization': 'Bearer {token}'.format(token=self.token)
        }

        try:
            response = requests.get(
                '{endpoint}?limit={limite}&seed_genres={seed_genres}'.format(
                    endpoint=self.RECOMENDADOS_ENDPOINT,
                    limite=self.LIMITE_RECOMENDADOS,
                    seed_genres=seed_genres
                ),
                headers=self.headers
            )
            response.raise_for_status()

            if not response.ok:
                return None
            

            response_data = response.json()
            tracks = response_data['tracks']

            return tracks
        except requests.exceptions.Timeout as e:
            return None
        except requests.exceptions.TooManyRedirects as e:
            return None
        except requests.exceptions.RequestException as e:
            return None
        except requests.exceptions.HTTPError as e:
            return None



# -*- coding: utf-8 -*-
{
    'name'       : "MySpotify",
    'version'    : "1.0",
    'depends'    : ["base"],
    'author'     : "Adrian Cuero, andretti86@gmail.com",
    'category'   : "Uncategorized",
    'description': """Prueba python developer OMNI.PRO""",
    #'qweb'       : ['static/src/xml/syncgeneros_btn.xml'],
    'data'       : [
        'data/genero.xml',
        'security/ir.model.access.csv',
        'views/genero.xml',
        'views/cancion.xml',
        'views/cliente.xml',
        'views/recomendacion.xml',
        #'views/syncgeneros_btn_asset.xml'
    ],
    'demo' : [],
    # 'external_dependencies': {
    #     'python': ['spotipy']
    # },
}
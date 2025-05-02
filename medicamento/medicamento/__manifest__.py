{
    'name': 'Gestión de Medicamentos',
    'version': '18.0',
    'category': 'Medical',
    'summary': 'Módulo para la gestión de medicamentos',
    'author': 'Marcelo aguierre',
    'depends': ['base'],
    'data': [
        'views/medicamento_form.xml',
        'views/medicamento_list.xml',
        'views/medicamento_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'medicamento/static/src/js/medicamento_widget.js',
        ],
    },
    'images': ['medicamento/static/description/10.png'],  # Aquí se define el logo
    
    'installable': True,
    'application': True,
}
{
    'name': 'AI Livechat Agent',
    'version': '17.0.1.0.0',
    'category': 'Website/Live Chat',
    'summary': 'AI Agent integration with Odoo Livechat and agent handoff',
    'license': 'LGPL-3',
    'depends': ['im_livechat', 'mail'],
    'data': [
        'views/livechat_channel_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'ai_livechat/static/src/js/ai_livechat.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
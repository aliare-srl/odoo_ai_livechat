from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ai_endpoint = fields.Char(
        string="AI Endpoint",
        config_parameter='mi_modulo.ai_endpoint'
    )
    default_ai_api_key = fields.Char('Default AI API Key',
                                    config_parameter='ai_livechat.default_api_key')

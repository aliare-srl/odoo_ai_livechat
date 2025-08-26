from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_ai_endpoint = fields.Char(
        string="AI Endpoint",
        config_parameter="odoo_ai_livechat.default_ai_endpoint"
    )

    default_ai_api_key = fields.Char(
        string="AI API Key",
        config_parameter="odoo_ai_livechat.default_ai_api_key"
    )

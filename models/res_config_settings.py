from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ai_endpoint = fields.Char(
        string="AI Endpoint",
        config_parameter="odoo_ai_livechat.ai_endpoint"
    )

    ai_api_key = fields.Char(
        string="AI API Key",
        config_parameter="odoo_ai_livechat.ai_api_key"
    )

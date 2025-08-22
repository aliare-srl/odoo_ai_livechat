from odoo import models, fields, api

class LivechatChannel(models.Model):
    _inherit = 'im_livechat.channel'

    ai_enabled = fields.Boolean('Enable AI Agent', default=False)
    ai_endpoint = fields.Char('AI Service Endpoint')
    ai_api_key = fields.Char('AI API Key')
    ai_handoff_keywords = fields.Text('Handoff Keywords', 
                                     default='human,agent,speak to someone,transfer')
    ai_greeting = fields.Text('AI Greeting Message', 
                             default='Hello! I am an AI assistant. How can I help you today?')
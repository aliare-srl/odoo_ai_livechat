from odoo import models, fields, api
import requests
import json

class LivechatChannel(models.Model):
    _inherit = 'im_livechat.channel'

    ai_enabled = fields.Boolean('Enable AI Agent', default=False)
    ai_endpoint = fields.Char('AI Service Endpoint')
    ai_api_key = fields.Char('AI API Key')
    ai_handoff_keywords = fields.Text('Handoff Keywords', 
                                     default='human,agent,speak to someone,transfer')
    ai_greeting = fields.Text('AI Greeting Message', 
                             default='Hello! I\'m an AI assistant. How can I help you today?')

    @api.model
    def _get_ai_response(self, message, channel_id):
        """Get response from AI service"""
        channel = self.browse(channel_id)
        if not channel.ai_enabled or not channel.ai_endpoint:
            return None
            
        try:
            response = requests.post(channel.ai_endpoint, 
                json={'message': message, 'channel_id': channel_id},
                headers={'Authorization': f'Bearer {channel.ai_api_key}'},
                timeout=10)
            return response.json().get('response') if response.status_code == 200 else None
        except:
            return None

    def _should_handoff_to_human(self, message):
        """Check if message contains handoff keywords"""
        keywords = self.ai_handoff_keywords.lower().split(',')
        return any(keyword.strip() in message.lower() for keyword in keywords)
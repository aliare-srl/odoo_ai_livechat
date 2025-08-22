from odoo import http
from odoo.http import request

class AILivechatController(http.Controller):

    @http.route('/ai_livechat/webhook', type='json', auth='public', methods=['POST'], csrf=False)
    def ai_webhook(self, **kwargs):
        """Webhook endpoint for external AI services"""
        channel_id = kwargs.get('channel_id')
        response = kwargs.get('response')
        
        if channel_id and response:
            channel = request.env['mail.channel'].sudo().browse(channel_id)
            if channel.exists():
                channel.with_context(mail_create_nosubscribe=True).message_post(
                    body=response,
                    author_id=request.env.ref('base.partner_root').id,
                    message_type='comment'
                )
        
        return {'status': 'success'}
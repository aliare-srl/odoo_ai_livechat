from odoo import models, fields, api

class MailChannel(models.Model):
    _inherit = 'mail.channel'

    ai_active = fields.Boolean('AI Agent Active', default=False)
    human_requested = fields.Boolean('Human Agent Requested', default=False)

    @api.model
    def message_post(self, **kwargs):
        """Override to handle AI responses"""
        message = super().message_post(**kwargs)
        
        if (self.livechat_channel_id and 
            self.livechat_channel_id.ai_enabled and 
            not self.human_requested and
            kwargs.get('author_id') != self.env.user.partner_id.id):
            
            self._handle_ai_response(kwargs.get('body', ''))
        
        return message

    def _handle_ai_response(self, user_message):
        """Process user message and generate AI response"""
        # Check for handoff request
        if self.livechat_channel_id._should_handoff_to_human(user_message):
            self._request_human_agent()
            return

        # Get AI response
        ai_response = self.livechat_channel_id._get_ai_response(user_message, self.id)
        
        if ai_response:
            self.with_context(mail_create_nosubscribe=True).message_post(
                body=ai_response,
                author_id=self.env.ref('base.partner_root').id,
                message_type='comment',
                subtype_xmlid='mail.mt_comment'
            )

    def _request_human_agent(self):
        """Handle handoff to human agent"""
        self.human_requested = True
        self.ai_active = False
        
        # Notify available operators
        self.with_context(mail_create_nosubscribe=True).message_post(
            body="Customer has requested to speak with a human agent.",
            author_id=self.env.ref('base.partner_root').id,
            message_type='notification'
        )

    def assign_operator(self, operator_id):
        """Override to handle AI to human handoff"""
        result = super().assign_operator(operator_id)
        if self.human_requested:
            self.with_context(mail_create_nosubscribe=True).message_post(
                body="A human agent has joined the conversation.",
                message_type='notification'
            )
        return result
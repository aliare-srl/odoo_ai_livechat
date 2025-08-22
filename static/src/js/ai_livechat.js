/** @odoo-module **/

import { LivechatButton } from '@im_livechat/legacy/widgets/livechat_button/livechat_button';
import { patch } from "@web/core/utils/patch";

patch(LivechatButton.prototype, 'ai_livechat', {
    
    async _openChat() {
        const result = await this._super(...arguments);
        
        // Send AI greeting if enabled
        if (this.options.ai_enabled && this.options.ai_greeting) {
            setTimeout(() => {
                this._sendAIGreeting();
            }, 1000);
        }
        
        return result;
    },

    _sendAIGreeting() {
        if (this.livechatWidget && this.options.ai_greeting) {
            this.livechatWidget._sendMessage({
                body: this.options.ai_greeting,
                author_id: [0, 'AI Assistant'],
                message_type: 'comment'
            });
        }
    },

    _onTyping() {
        this._super(...arguments);
        // Add typing indicator for AI responses
        if (this.options.ai_enabled) {
            this._showAITyping();
        }
    },

    _showAITyping() {
        // Show AI typing indicator logic here
        console.log('AI is typing...');
    }
});
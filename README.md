# AI Livechat Agent for Odoo Community Edition

This module integrates AI agents with Odoo's livechat functionality while maintaining seamless agent handoff capabilities.

## Features

- **AI Agent Integration**: Connect any AI service via REST API
- **Smart Handoff**: Automatic detection of requests for human agents
- **Seamless Transition**: Maintains chat history during AI-to-human handoff
- **Configurable Keywords**: Customize trigger words for agent handoff
- **Custom Greetings**: Set personalized AI greeting messages

## Setup

1. **Install the module** in your Odoo instance
2. **Configure AI settings** in Settings > AI Livechat
3. **Enable AI** for specific livechat channels
4. **Set up your AI endpoint** that accepts POST requests with:
   ```json
   {
     "message": "user message",
     "channel_id": 123
   }
   ```

## AI Service Requirements

Your AI service should:
- Accept POST requests with JSON payload
- Return JSON response: `{"response": "AI reply"}`
- Handle authentication via Bearer token (optional)

## Handoff Keywords

Default keywords that trigger human agent handoff:
- "human"
- "agent" 
- "speak to someone"
- "transfer"

Customize these in the livechat channel configuration.

## Usage

1. Customer starts chat
2. AI agent responds automatically
3. If customer requests human help, seamless handoff occurs
4. Human agents can take over maintaining full chat context
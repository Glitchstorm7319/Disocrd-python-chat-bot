# AI Discord Bot

A Discord bot powered by OpenAI that can chat with users in Discord servers.

## Features

- AI-powered conversations using OpenAI's GPT-4o model
- Responds to mentions and direct messages
- Command-based chat functionality
- Typing indicators for better user experience
- Handles long messages by splitting them appropriately
- Comprehensive logging and error handling

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Discord bot token
- OpenAI API key

### Installation

1. Clone or download this project
2. Install required dependencies:
   ```bash
   pip install discord.py openai python-dotenv
   ```

### Configuration

Set up the following environment variables in .evn.example:

```
DISCORD_BOT_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

### Getting Your Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Create a bot and copy the token
5. Invite the bot to your server with "Send Messages" and "View Channels" permissions

### Getting Your OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy the key for use in your environment variables

### Running the Bot

Run the bot with:
```bash
python main.py
```

## How to Use

### Chat with the Bot

1. **Mention the bot**: `@YourBot Hello, how are you?`
2. **Use the chat command**: `!chat Tell me a joke`
3. **Send a direct message**: DM the bot directly

### Commands

- `!chat <message>` - Chat with the AI
- `!help` - Show help information

### Examples

- `@bot What's the weather like today?`
- `!chat Explain quantum physics in simple terms`
- `@bot Tell me a programming joke`

## Important Notes

- **Permissions**: The bot needs "Send Messages" and "View Channels" permissions
- **Rate Limits**: The bot respects Discord's rate limits and OpenAI's API limits
- **Costs**: Using OpenAI's API incurs costs based on usage
- **Privacy**: Messages are sent to OpenAI for processing

## Troubleshooting

### Common Issues

1. **"Invalid bot token"**: Check your `DISCORD_BOT_TOKEN`
2. **"OPENAI_API_KEY required"**: Make sure you've set your OpenAI API key
3. **Bot not responding**: Ensure the bot has proper permissions in the channel
4. **API errors**: Check your OpenAI API key and account status
**contact me**
For any other issues pls visit  my discord https://discord.gg/HCGr9d8Aa8.

### Logs

Check the `bot.log` file for detailed information about bot activity and any errors.

## Legal Disclaimer

This bot sends user messages to OpenAI for processing. Ensure compliance with your organization's data policies and Discord's Terms of Service.

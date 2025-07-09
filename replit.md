# AI Discord Bot

## Overview

This is an AI-powered Discord bot application written in Python that can have intelligent conversations with users in Discord servers using OpenAI's GPT-4o model. The bot responds to mentions, direct messages, and commands with contextually appropriate AI-generated responses.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Application Type
- **Standalone Python Application**: AI-powered Discord bot with OpenAI integration
- **Event-Driven Architecture**: Uses Discord.py's event system for handling Discord API interactions
- **Asynchronous Programming**: Built with asyncio for non-blocking operations

### Core Components
- **Main Entry Point** (`main.py`): Complete bot implementation with AI integration
- **OpenAI Integration**: GPT-4o model for intelligent conversation responses
- **Discord Commands**: Command system for user interaction

## Key Components

### Bot Engine (`main.py`)
- **Discord Bot Setup**: Main bot implementation using discord.py library
- **Event Handlers**: Discord client events (on_ready, message handling)
- **OpenAI Integration**: GPT-4o API calls for intelligent responses
- **Message Processing**: Handles mentions, DMs, and command parsing
- **Response Generation**: AI-powered conversation with context awareness

### Command System
- **!chat**: Direct chat with AI using command syntax
- **!ping**: Bot responsiveness check
- **!bothelp**: Help information display

### AI Response System
- **Context-Aware**: Maintains conversation context through system prompts
- **Message Splitting**: Handles long responses by splitting into chunks
- **Error Handling**: Graceful handling of API errors and rate limits

### Logging System
- **File and Console Logging**: Dual output for monitoring
- **Structured Logging**: Consistent format with timestamps and log levels
- **Error Tracking**: Comprehensive error logging for debugging

## Data Flow

1. **Initialization**: Load configuration from environment variables
2. **Validation**: Verify bot token and OpenAI API key
3. **Discord Connection**: Establish connection to Discord API
4. **Message Reception**: Listen for mentions, DMs, and commands
5. **AI Processing**: Send user messages to OpenAI API
6. **Response Generation**: Return AI-generated responses to Discord

## External Dependencies

### Primary Dependencies
- **discord.py**: Discord API interaction library
- **openai**: OpenAI API client for GPT-4o access
- **python-dotenv**: Environment variable management

### API Integrations
- **Discord API**: Bot token authentication and message handling
- **OpenAI API**: GPT-4o model for intelligent conversation
- **Rate Limiting**: Built-in awareness of both Discord and OpenAI API limits

## Deployment Strategy

### Environment Configuration
- **Environment Variables**: Configuration through environment secrets
- **Required Variables**: DISCORD_BOT_TOKEN, OPENAI_API_KEY
- **API Key Security**: Secure handling of sensitive credentials

### Runtime Requirements
- **Python 3.8+**: Minimum Python version requirement
- **Discord Bot Setup**: Bot application created in Discord Developer Portal
- **OpenAI Account**: Valid OpenAI API key with sufficient credits
- **Bot Permissions**: Send Messages and View Channels permissions

### Monitoring and Maintenance
- **Log Files**: bot.log file for persistent logging
- **Graceful Shutdown**: Proper cleanup on termination
- **API Error Recovery**: Automatic retry with appropriate error messages

### Scalability Considerations
- **Multi-Server Support**: Bot can operate across multiple Discord servers
- **Rate Limiting**: Respects both Discord and OpenAI API rate limits
- **Resource Usage**: Optimized for minimal CPU and memory footprint

## Recent Changes (2025-07-09)
- **Complete Rebuild**: Converted from spam bot to AI chat bot
- **OpenAI Integration**: Added GPT-4o model for intelligent responses
- **Command System**: Implemented chat commands and help functionality
- **API Key Requirement**: Users must now provide OpenAI API key
- **Enhanced Error Handling**: Better error messages and API failure handling
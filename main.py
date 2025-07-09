#!/usr/bin/env python3
"""
AI Discord Bot
A Discord bot powered by OpenAI that can chat with users.
"""

import asyncio
import logging
import sys
import os
import discord
from discord.ext import commands
from openai import OpenAI

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Initialize OpenAI client
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)

openai_client = get_openai_client()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Called when bot is ready"""
    logger.info(f'Bot logged in as {bot.user}')
    logger.info(f'Bot is ready and connected to {len(bot.guilds)} servers')

@bot.event
async def on_message(message):
    """Handle incoming messages"""
    # Don't respond to own messages
    if message.author == bot.user:
        return
    
    # Don't respond to other bots
    if message.author.bot:
        return
    
    # Only respond if bot is mentioned or it's a DM
    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        try:
            # Remove the bot mention from the message
            content = message.content.replace(f'<@{bot.user.id}>', '').strip()
            
            if not content:
                await message.reply("Hi! I'm an AI bot. Ask me anything!")
                return
            
            # Check if OpenAI is available
            if not openai_client:
                await message.reply("Sorry, I need an OpenAI API key to chat. Please contact the bot owner to configure it.")
                return
            
            # Show typing indicator
            async with message.channel.typing():
                # Generate AI response
                response = openai_client.chat.completions.create(
                    model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful AI assistant in a Discord server. Be friendly, conversational, and helpful. Keep responses concise but informative."
                        },
                        {
                            "role": "user",
                            "content": content
                        }
                    ],
                    max_tokens=1000,
                    temperature=0.7
                )
                
                ai_response = response.choices[0].message.content
                
                # Split long messages to avoid Discord's 2000 character limit
                if len(ai_response) > 2000:
                    chunks = [ai_response[i:i+2000] for i in range(0, len(ai_response), 2000)]
                    for chunk in chunks:
                        await message.reply(chunk)
                else:
                    await message.reply(ai_response)
                    
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            await message.reply("Sorry, I encountered an error while processing your message. Please try again!")
    
    # Process commands
    await bot.process_commands(message)

@bot.command(name='chat')
async def chat_command(ctx, *, message):
    """Chat with the AI using a command"""
    try:
        if not openai_client:
            await ctx.reply("Sorry, I need an OpenAI API key to chat. Please contact the bot owner to configure it.")
            return
            
        async with ctx.typing():
            response = openai_client.chat.completions.create(
                model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant in a Discord server. Be friendly, conversational, and helpful. Keep responses concise but informative."
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                max_tokens=1000,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            if len(ai_response) > 2000:
                chunks = [ai_response[i:i+2000] for i in range(0, len(ai_response), 2000)]
                for chunk in chunks:
                    await ctx.reply(chunk)
            else:
                await ctx.reply(ai_response)
                
    except Exception as e:
        logger.error(f"Error in chat command: {e}")
        await ctx.reply("Sorry, I encountered an error. Please try again!")

@bot.command(name='ping')
async def ping_command(ctx):
    """Check if the bot is responsive"""
    await ctx.reply(f"Pong! 🏓 Latency: {round(bot.latency * 1000)}ms")

@bot.command(name='bothelp')
async def help_command(ctx):
    """Show help information"""
    embed = discord.Embed(
        title="AI Discord Bot Help",
        description="I'm an AI-powered Discord bot that can chat with you!",
        color=0x00ff00
    )
    embed.add_field(
        name="How to use:",
        value="• Mention me (@bot) in any message to chat\n• Send me a DM\n• Use commands with `!` prefix",
        inline=False
    )
    embed.add_field(
        name="Commands:",
        value="• `!chat <message>` - Chat with the AI\n• `!ping` - Check bot responsiveness\n• `!bothelp` - Show this help message",
        inline=False
    )
    embed.add_field(
        name="Examples:",
        value="• `@bot Hello, how are you?`\n• `!chat Tell me a joke`\n• `@bot What's the weather like?`",
        inline=False
    )
    await ctx.reply(embed=embed)

async def main():
    """Main function to run the bot"""
    try:
        # Check for required environment variables
        bot_token = os.getenv("DISCORD_BOT_TOKEN")
        openai_key = os.getenv("OPENAI_API_KEY")
        
        if not bot_token:
            logger.error("DISCORD_BOT_TOKEN environment variable is required")
            return
        
        if not openai_key:
            logger.error("OPENAI_API_KEY environment variable is required")
            return
        
        logger.info("Starting AI Discord bot...")
        await bot.start(bot_token)
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Failed to start bot: {e}")
        sys.exit(1)
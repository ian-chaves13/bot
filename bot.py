import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot_logic import gen_pass

# Carrega as credenciais de segurança do ficheiro .env
load_dotenv()

# Configuração de permissões (Intents)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True # Permissão adicionada para o comando 'joined' funcionar

# Inicialização do Bot
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
await ctx.send(f'Olá eu sou um bot {bot.user}!')

@bot.command()
async def pasw(ctx):
await ctx.send(gen_pass(10))

@bot.command()
async def joined(ctx, member: discord.Member):
"""Says when a member joined."""
await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

# O bot inicia utilizando a variável de ambiente, mantendo o token secreto
bot.run(os.getenv('DISCORD_TOKEN'))
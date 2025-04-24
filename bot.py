import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emodji

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hi! I am a bot')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$bye'):
        await message.channel.send("👋")
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)

client.run("token")

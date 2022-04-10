from concurrent.futures import process
import discord

client = discord.Client()


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):

        if str(message.author) == "RahilDev#7975":  # make sure to change to your user name with hash code
            await message.channel.send("Hello Master!")
        else:
            await message.channel.send("Hello, I am a test bot.")


client.run('OTYxMjg0OTYzNzU0NDUxMDA2.Yk2wYw.M5Dz_26AgE3Id3qlXql85FZwke4')
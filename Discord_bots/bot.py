# import discord
# import asyncio
# import datetime
# import requests
# from discord.ext import commands

# # client=commands.Bot(command_prefix='.')

# # @client.event
# # async def on_ready():
# #     print('Bot is Ready')

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#     while True:
#         url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCDdKEz8e7m5g-hXg42-HBQg&order=date&maxResults=1&access_token=[Collect_From_google_dev_console]"
#         payload = {}
#         files = {}
#         headers= {}
#         response = requests.request("GET", url, headers=headers, data = payload, files = files)
#         # print(response.text.encode('utf8'))
#         rs=response.json()
#         youtube="https://www.youtube.com/watch?v="
#         video_id= rs["items"][0]["id"]["videoId"]
#         msg="Check out "+youtube+""+video_id
#         memes = client.get_channel([collect_from_discord])
#         await memes.send(msg)
#         await asyncio.sleep(100)


# @client.event
# async def on_message(message):
#     # if message.author == client.user:
#     #     return

#     if message.content.startswith('hello'):
#         await message.channel.send('Hello!')



#  -------------Basic stuff-------------
# import discord

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))
# ------------------------------------------



import discord

client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}!'.format(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    if message.content.startswith('$xicz'):
        await message.channel.send('Hello!')


client.run('[collect_from_discord]')





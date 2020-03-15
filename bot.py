# Importing discord and other dependencies
import discord

import os,string
from serp import search_google
import db
import statements

#Loading our secret token from environment file
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN=os.environ.get("DISCORD_TOKEN")


class MyClient(discord.Client):
    
    #Using nodejs async await to wait for the result (provided by discord)
    async def on_ready(self):
        print('Logged on as', self.user)
    
    #Making sure not to reply to our own messages
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        #Separating keywords and values
        try:
            if sum([i.strip(string.punctuation).isalpha() for i in message.content.split()]) > 1:
                keyword,value = message.content.split(' ', 1)
            else:
                keyword = "Nan"
        except Exception as e:
            # Not using logger as of now to log errors, otherwise we should always use logger to log errors
            print(e)
        
        try:
            if keyword != "Nan":
                if keyword == '!google':
                    print(value)
                    await message.channel.send(statements.GOOGLE_SEARCH)
                    #Using our serp module to search google and get results
                    await message.channel.send(search_google({"q": value}))
                    #Inserting into database to persist the search history
                    db.insert_search(value)

                if keyword == '!recent':
                    await message.channel.send(statements.RECENT_SEARCH)
                    await message.channel.send(db.find_history(value))
            
            if message.content == 'hi':
                await message.channel.send(statements.GREETING)
            
        except Exception as e:
            print(e)
            pass
        

client = MyClient()
client.run(TOKEN)
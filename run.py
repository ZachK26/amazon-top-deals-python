from Crawler import Crawler
import webbrowser
import discord
import time

bot = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

store = "com"

product_name = "Gaming Mouse"


@bot.event
async def on_message(message):

    if message.content.startswith('getdeals'):
        await message.channel.send("Getting deals... Give me a moment...")
        craw = Crawler(product_name, store)
        top_ten = craw.get_best_deal()
        await message.channel.send("Here are the best deals!")
        for item in top_ten:
            phrase = item["link"]
            name = item["name"]
            discount = str(item["price_diff"])
            await message.channel.send(name + " at a $" + discount + " discount: " + phrase)  
            time.sleep(6)
        time.sleep(3600)
        await message.channel.send("getdeals")
    if message.content.startswith('getdeals'):
        await message.delete(message) 
bot.run('ODM3NDIxOTY3NDIxMjEwNjQ2.YIsT-w.9cS9a3nKACYvMir75S-2DuegQ_E')

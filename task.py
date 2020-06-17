from os import environ
import discord
import shlex

def makeInd(number):
    if number > 9:
        num=0
    else:
        num = round(abs(number))
    maked=eval('"\\U0000003'+str(num)+'"')
    return maked
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game("!vote and !kill"))
@client.event
async def on_message(message):
    if message.content.startswith('!'):
        cmd=message.content[1:]
        params=cmd.split(" ",1)[:]
        if params[0] in ['vote','kill']:
            if params[0]=='vote':
                guildVillagers=[]
                for Person in message.channel.guild.members:
                    for Role in Person.roles:
                        if Role.id == 722863423934693447:
                            guildVillagers.append(Person)
                toSend='vote'+str(len(guildVillagers))+':Who do you want to put on trial?'
                for i in guildVillagers:
                    toSend+='\n'+str(guildVillagers.index(i))+') `'+i.display_name+'`'
                await message.channel.send(toSend)
    elif message.author==message.channel.guild.me and message.content.startswith("vote"):
        for i in range(int((' '+message.content).split('vote')[1].split(':')[0])):
            nextEmoji= ('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣')[i]
            print(nextEmoji)
            await message.add_reaction(nextEmoji)
        await message.add_reaction('\U0000274C')
        await message.edit(content=(message.content).split(":",1)[1])
    elif message.author==message.channel.guild.me and message.content.startswith("poll: "):
        await message.add_reaction('\U00002705')
        await message.add_reaction('\U0000274C')
        await message.edit(content=('filler'+message.content).split("poll: ",1)[1],allowed_mentions=discord.AllowedMentions(everyone=message.mention_everyone))

bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
    print('\n'*100)
client.run(bot_token)

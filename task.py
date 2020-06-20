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
                    x='0123456789abcdefghij'[guildVillagers.index(i)]
                    toSend+='\n'+x+') `'+i.display_name+'`'
                sentMessage=await message.channel.send(toSend)
                print(sentMessage.channel.name,sentMessage.author.display_name,sentMessage.content)
                for i in len(guildVillagers):
                    await sentMessage.add_reaction(('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯')[i])
            elif params[0]=='kill':
                sentMessage=await message.channel.send('kill: Do you want to kill '+params[1]+'?')
                await sentMessage.add_reaction('\U00002705')
                await sentMessage.add_reaction('\U0000274C')

bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
    print('\n'*100)
client.run(bot_token)

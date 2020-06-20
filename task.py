from os import environ
import discord
bot = discord.Client()
@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))
    await bot.change_presence(activity=discord.Game("!vote and !kill"))
@bot.event
async def on_message(message):
    if message.content.startswith('!'):
        cmd=message.content[1:]
        params=cmd.split(" ",1)[:]
        if params[0] in ['vote','kill']:
            if params[0]=='vote':
                guildVillagers=[]
                for Person in message.channel.guild.members:
                    for Role in Person.roles:
                        if Role.name == 'Alive':
                            guildVillagers.append(Person)
                toSend='Who do you want to put on trial?'
                for i in guildVillagers:
                    x='0123456789abcdefghij'[guildVillagers.index(i)]
                    toSend+='\n'+x+') `'+i.display_name+'`'
                aliveMention='"Alive"'
                if len(guildVillagers)==0:
                    for i in message.channel.guild.roles:
                        if i.name=="Alive":
                            aliveMention=i.mention
                    toSend='There is no one to put on trial! Try giving some people the {} role to get started.'.format(aliveMention)
                sentMessage=await message.channel.send(toSend)
                for i in range(len(guildVillagers)):
                    await sentMessage.add_reaction(('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯')[i])
            elif params[0]=='kill':
                sentMessage=await message.channel.send('Do you want to kill '+params[1]+'?')
                await sentMessage.add_reaction('\U00002705')
                await sentMessage.add_reaction('\U0000274C')

bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
    print('\n'*100)
bot.run(bot_token)

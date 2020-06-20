from os import environ
from discord.ext import commands
bot = commands.Bot(command_prefix='!',owner_id=600130839870963725)
@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user))
    #presence here later
@bot.command()
async def vote(ctx):
    guildVillagers=[]
    for Person in ctx.guild.members:
        for Role in Person.roles:
            if Role.name == 'Alive':
                    guildVillagers.append(Person)
    toSend='Who do you want to put on trial?'
    for i in guildVillagers:
        x='0123456789abcdefghij'[guildVillagers.index(i)]
        toSend+='\n'+x+') `'+i.display_name+'`'
    aliveMention='"Alive"'
    if len(guildVillagers)==0:
        for i in ctx.guild.roles:
            if i.name=="Alive":
                aliveMention=i.mention
        toSend='There is no one to put on trial! Try giving some people the {} role to get started.'.format(aliveMention)
    sentMessage=await ctx.send(toSend)
    for i in range(len(guildVillagers)):
        await sentMessage.add_reaction(('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯')[i])
@bot.command()
async def kill(ctx,arg):
    sentMessage=await ctx.send('Do you want to kill '+arg+'?')
    await sentMessage.add_reaction('\U00002705')
    await sentMessage.add_reaction('\U0000274C')
bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
    print('\n'*100)
bot.run(bot_token)

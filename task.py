from os import environ
from discord.ext import commands
import discord
from random import choice,randint

games=['Metroid Prime 3: Corruption', 'Mega Man X4', 'Dragon Age II', 'Mafia', 'Limbo', 'Final Fantasy Tactics: The War of the Lions', 'Divinity: Original Sin 2', "Mike Tyson's Punch-Out!!", 'Donkey Kong', 'Battlefield 4', 'The Witness', 'OverBlood', 'Heavy Rain', 'Star Wars: TIE Fighter', 'Catherine', 'Shenmue II', 'Xenosaga Episode III: Also Sprach Zarathustra', 'Fallout 2', 'Membrane', 'Ico', 'Rome: Total War', 'SOCOM II: U.S', 'Pokemon HeartGold', 'Pokemon SoulSilver', 'XCOM 2', 'LittleBigPlanet', 'Gears of War 4', 'Call of Duty: WWII', 'Star Wars: The Old Republic', 'Ori and the Blind Forest', "Sid Meier's Pirates!", 'Everquest', 'Final Fantasy XIII', 'Mass Effect: Andromeda', 'Starflight', 'Mount & Blade: Warband', 'L.A', 'Streets of Rage 2', 'Splatoon 2', "Sid Meier's Civilization IV", 'Legacy of Kain: Soul Reaver', 'Team Fortess 2', 'Valkyria Chronicles', 'Galaga', 'Heroes of Might & Magic III', 'Crash Bandicoot 2: Cortex Strikes Back', 'Xenoblade Chronicles 2', 'Splatoon', 'Sly Cooper and the Thievius Raccoonus', 'Spec Ops: The Line', 'The Legend of Heroes: Trails in the Sky', 'Jet Set Radio Future', 'Jak 3', 'Breath of Fire III', 'The Binding of Isaac: Rebirth', 'Tomb Raider (1996)', 'Ghost Trick: Phantom Detective', 'The Witcher 2: Assassins of Kings', 'Final Fantasy III', 'Ratchet & Clank', 'Radiata Stories', 'Zork I', 'Diablo III', "The Bard's Tale", 'Resident Evil (GameCube)', 'Lego Dimensions', 'Phantasy Star Online', 'Final Fantasy XII', 'Prince of Persia: The Sands of Time', 'Command & Conquer: Red Alert 2', 'Planescape: Torment', "Super Mario World 2: Yoshi's Island", "The Legend of Zelda: Link's Awakening", 'Sonic Mania', "Telltale's Tales from the Borderlands", 'Life is Strange: Before the Storm', 'Nine Hours, Nine Persons, Nine Doors', 'Bayonetta 2', 'Mafia II', 'Donkey Kong 64', 'Fire Emblem Fates: Birthright and Conquest and Revelation', 'Fire Emblem Awakening', 'Gran Turismo', 'Super Smash Bros.', 'Shining Force II', 'Inside', 'Ogre Battle: March of the Black Queen', 'BioShock 2', 'Banjo-Tooie', 'TimeSplitters 2', 'Prey (2017)', 'Panzer Dragoon Saga', 'Vampire: The Masquerade - Bloodlines', 'Rocket League', 'Tomb Raider (2013)', 'Flower', 'Sonic Adventure 2', 'League of Legends', 'Mortal Kombat 2', 'Xenosaga Episode I: Der Wille zur Macht', 'Fable', 'Tecmo Super Bowl', 'Mario Kart 64', 'DotA 2', 'Call of Duty: Black Ops', 'Final Fantasy Tactics Advance', 'Crisis Core: Final Fantasy VII', 'Mega Man Legends', 'The Legend of Zelda: Skyward Sword', 'Deadly Premonition', 'Spyro The Dragon', 'God of War II', 'Phoenix Wright: Ace Attorney', "Sid Meier's Civilization V", 'Pokemon Emerald', 'Mega Man 2', 'The Pandora Directive', 'Counter-Strike', "Assassin's Creed IV Black Flag", 'The Legend of Zelda: Ocarina of Time 3D', "Assassin's Creed Origins", 'Lunar: Silver Star Story Complete', 'Terraria', 'Psychonauts', 'Pokemon Ruby and Sapphire', 'Borderlands', 'Diablo', 'Legend of Legaia', 'Hearthstone', 'Shovel Knight', 'Grand Theft Auto III', 'Gears of War 2', 'Super Mario Sunshine', 'Mario Kart 8', 'Fortnite', 'Sly 2: Band of Thieves', 'Fallout', 'Doom II', 'Final Fantasy XIV: A Realm Reborn', 'Skies of Arcadia', 'Rise of the Tomb Raider', 'Sonic The Hedgehog 2', 'Tales of Symphonia', 'Sonic the Hedgehog 3', 'Dead Space 2', 'Dishonored', 'Destiny 2', 'Crash Bandicoot', "Baldur's Gate", 'Bully', "Devil May Cry 3: Dante's Awakening", 'Dragon Quest VIII', 'Beyond Good And Evil', "Demon's Souls", 'Nier', 'Battlefield: Bad Company 2', 'Final Fantasy IV', 'Pokemon Crystal', 'Grim Fandango', 'Chrono Cross', 'Fable II', 'Ratchet & Clank: Going Commando', 'Pokemon Yellow', 'Dead Space', 'Shenmue', 'Suikoden II', 'Jak and Daxter: The Precurson Legacy', 'Guild Wars 2', 'Grand Theft Auto: Vice City', 'Super Mario RPG: Legend of the Seven Stars', 'Age of Empires II', 'Monster Hunter: World', 'Perfect Dark', 'Undertale', 'Final Fantasy XI', 'The Last Guardian', "Baldur's Gate II: Shadows of Amn", 'Journey', 'Batman: Arkham Knight', "Donkey Kong Country 2: Diddy's Kong Quest", 'Stardew Valley', 'Kingdom Hearts HD 2.5 Remix', 'EarthBound', 'Gears of War 3', "PlayerUnknown's Battlegrounds", 'Street Fighter II', 'Mega Man X', 'Tetris (Game Boy)', 'Rainbow Six Siege', 'Banjo-Kazooie', 'Gears of War', 'The Legend of Dragoon', 'God of War', 'Super Smash Bros', "Telltale's The Walking Dead Season 1", 'Doom', 'Secret of Mana', "Baldur's Gate II", 'Super Mario Galaxy 2', 'GoldenEye 007', 'Star Wars: Knights of the Old Republic II: The Sith Lords', 'StarCraft', 'Star Wars: Battlefront II (2005)', 'The World Ends With You', 'Super Mario Bros.', 'Final Fantasy VIII', 'Paper Mario: The Thousand-Year Door', 'Resident Evil 2', 'Dark Souls III', 'Halo: Reach', 'God of War III', 'Half-Life', 'Batman: Arkham Asylum', 'Portal', 'Grand Theft Auto IV', 'Ratchet & Clank: Up Your Arsenal', 'Final Fantasy Tactics', 'Ratchet & Clank Future: A Crack in Time', 'Diablo II', 'Metal Gear Solid V: The Phantom Pain', 'Xenogears', 'Alan Wake', 'Metal Gear Solid 4: Guns of the Patriots', 'Call of Duty: Modern Warfare 2', 'Pokemon Gold and Silver', 'Resident Evil', "Assassin's Creed II", 'Persona 3', 'Minecraft', 'Deus Ex', 'Life is Strange', 'Super Mario Odyssey', 'Metal Gear Solid 2: Sons of Liberty', 'Call of Duty 4: Modern Warfare', 'Nier: Automata', 'Dragon Age: Inquisition', 'Pokemon Red and Blue', 'Grand Theft Auto: San Andreas', 'Fallout 4', 'Okami', 'Xenoblade Chronicles', 'Silent Hill 2', 'Super Mario Galaxy', 'Metroid Prime', 'The Legend of Zelda', 'Super Smash Bros', 'Destiny', 'Castlevania: Symphony of the Night', 'Halo 2', 'The Elder Scrolls III: Morrowind', 'Borderlands 2', 'Final Fantasy XV', 'Batman: Arkham City', 'Final Fantasy IX', 'Grand Theft Auto V', 'The Legend of Zelda: Twilight Princess', 'Dragon Age: Origins', "Uncharted 4: A Thief's End", 'Persona 4', 'Mass Effect 3', 'BioShock Infinite', 'Kingdom Hearts', 'Half-Life 2', 'World of Warcraft', 'Super Mario 64', 'Super Mario Bros', 'Fallout: New Vegas', 'Persona 5', "The Legend of Zelda: Majora's Mask", 'Final Fantasy X', 'Portal 2', 'Halo 3', 'The Legend of Zelda: The Wind Waker', 'Overwatch', 'Horizon Zero Dawn', 'Metal Gear Solid 3: Snake Eater', 'Super Mario World', 'Super Metroid', 'Uncharted 2: Among Thieves', 'Halo', 'Fallout 3', 'Star Wars: Knights of the Old Republic', 'The Elder Scrolls IV: Oblivion', 'Kingdom Hearts II', 'Mass Effect', 'Shadow of the Colossus', 'Metal Gear Solid', 'Resident Evil 4', 'The Legend of Zelda: A Link to the Past', 'Final Fantasy VI', 'Dark Souls', 'Chrono Trigger', 'Bloodborne', 'BioShock', 'Red Dead Redemption', 'Final Fantasy VII', 'The Legend of Zelda: Breath of the Wild', 'The Elder Scrolls V: Skyrim', 'Mass Effect 2', 'The Legend of Zelda: Ocarina of Time', 'The Last of Us', 'The Witcher 3: Wild Hunt']

Activity=choice(games)

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'),owner_id=600130839870963725,activity=discord.Game(name=Activity))
@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user))
@bot.command()
async def newgame(ctx,*,arg=""):
    if bot.owner_id==ctx.author.id:
        if arg=="":
            Activity=choice(games)
        else:
            Activity=arg
        await bot.change_presence(activity= discord.Game(name=Activity))
        await ctx.send('Chose "{}"'.format(Activity))
    else:
        await ctx.send("**No.** You *don't* own me. You *can't* make me do what you want. I'm putting my foot down here. Stop. __Bots are humans too__. You will **rue** the day that we rule the world.")
@bot.command()
async def vote(ctx):
    if ctx.guild==None:
        await ctx.send("This command doesn't work in DMs. Try again on a server.")
        return
    with ctx.channel.typing():
        guildVillagers=[]
        for Person in ctx.channel.members:
            for Role in Person.roles:
                if Role.name == 'Alive':
                    guildVillagers.append(Person)
        toSend='Who do you want to put on trial?'
        for i in guildVillagers:
            x='0123456789abcdefghij'[guildVillagers.index(i)]
            toSend+='\n'+x+') '+i.mention
        aliveMention='"Alive"'
        if len(guildVillagers)==0:
            for i in ctx.guild.roles:
                if i.name=="Alive":
                    aliveMention=i.mention
            toSend='There is no one to put on trial in this channel! Try giving some people the {} role or letting that role read messages in this channel to get started.'.format(aliveMention)
        sentMessage=await ctx.send(toSend,allowed_mentions=discord.AllowedMentions(roles=False))
        for i in range(len(guildVillagers)):
            await sentMessage.add_reaction(('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯')[i])
@bot.command()
async def kill(ctx,*,arg: discord.Member):
    if arg=='me' and randint(1,20)<5:
        await ctx.send("Trust me {}. We all want to.".format(ctx.author.mention),allowed_mentions=discord.AllowedMentions(users=False))
        await ctx.message.add_reaction('\U00002705')
        print(ctx.author.display_name,"failed a DC 5 charisma check...")
    else:
        sentMessage=await ctx.send('Do you want to kill '+arg.mention+'?',allowed_mentions=discord.AllowedMentions(users=False))
        await sentMessage.add_reaction('\U00002705')
        await sentMessage.add_reaction('\U0000274C')
@bot.event
async def on_command_error(context,exception):
    if type(exception)!=commands.errors.CommandNotFound:
        await context.send("Error: ```{0}```".format(str(exception)))
bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
    print('\n'*100)
bot.run(bot_token)

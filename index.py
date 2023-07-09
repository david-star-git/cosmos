import discord
from discord import client, SelectOption
from discord.ext import commands
from discord import app_commands
from discord.utils import get
from discord.ui import View, Button, button

from dotenv import load_dotenv
import os
import asyncio
import json
import sqlite3
import random
from easy_pil import *

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
client = commands.Bot(command_prefix='/', intents=intents, application_id=1061127271081062532)


blacklist = [
    "anus","anal", "biatch", "bitch","cum", "cock",
    "dick", "dick","faggot", "fatass","gay", "goyim",
    "gypsy", "gipsy","homo","hurensohn","hure",
    "lesbo","lesbe","negress","negro","nig",
    "nig-nog","nigga","nigger","nigg4","neger",
    "nigguh","neger","nutte","nuttensohn","penis",
    "prostitute","pussie","pussy","schlampe","slut",
    "schwuchtel","schwanz","tits","titt","whore",
    ]




#---------< users.db >---------#
connection = sqlite3.connect('users.db')

sql_create_table_members = """
CREATE TABLE members (
    id UNIQUE,
    bans INTEGER,
    kicks INTEGER,
    mutes INTEGER,
    warns INTEGER,
    level INTEGER,
    xp INTEGER
)
"""

try:
    cursor = connection.cursor()
    cursor.execute(sql_create_table_members)
    connection.commit()
    print("connected to users.db")
except Exception as e:
    connection.rollback()


#---------< on ready >---------#
@client.event
async def on_ready():
    print(f"logged in as {str(client.user)[:-5]} (ID: {client.user.id})")
    synced = await client.tree.sync()
    print(f"Synced {str(len(synced))} Commands")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the Universe."))



##################################
#---------< moderation >---------#
##################################



#---------< ban >---------#
@client.tree.command(name="ban", description="Bans a specified user")
async def ban_user(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if interaction.user.guild_permissions.ban_members:
        try:
            embed = discord.Embed(title=f"**{user.name} was banned by {interaction.user.name}**",
                              color=discord.Colour.from_rgb(177, 26, 33))
            embed.add_field(name="📆**Date **", value=interaction.created_at.strftime("%d/%m/%Y"))
            embed.add_field(name="🆔**User ID**", value=user.id)
            embed.add_field(name="💬**Reason**", value=reason)
            embed.set_thumbnail(url=user.avatar.url)
            embed.set_footer(text="🌌 Cosmos • VampiricShadow")
            await interaction.response.send_message(embed=embed)
            log = client.get_channel(990388132815990824)
            await log.send(embed=embed)
            try:
                await user.send(embed=embed)
            except Exception as e:
                print(f"{user} Does not allow direct messages!")
                print(e)
            await user.ban(reason=reason)
            id_value = user.id
            cursor.execute("SELECT * FROM members WHERE id = ?", (id_value,))
            row = cursor.fetchone()
            if row is not None:
                ban = row[1]
                ban += 1
                cursor.execute("UPDATE members SET bans = ? WHERE id = ?", (ban, id_value))
                connection.commit()
        except:
            await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< kick >---------#
@client.tree.command(name="kick", description="Kicks a specified user")
async def kick_user(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if interaction.user.guild_permissions.kick_members:
        try:
            embed = discord.Embed(title=f"**{user.name} was kicked by {interaction.user.name}**",
                              color=discord.Colour.from_rgb(177, 26, 33))
            embed.add_field(name="📆**Date **", value=interaction.created_at.strftime("%d/%m/%Y"))
            embed.add_field(name="🆔**User ID**", value=user.id)
            embed.add_field(name="💬**Reason**", value=reason)
            embed.set_thumbnail(url=user.avatar.url)
            embed.set_footer(text="🌌 Cosmos • VampiricShadow")
            await interaction.response.send_message(embed=embed)
            log = client.get_channel(990388132815990824)
            await log.send(embed=embed)
            try:
                await user.send(embed=embed)
            except Exception as e:
                print(f"{user} Does not allow direct messages!")
                print(e)
            await user.kick(reason=reason)
            id_value = user.id
            cursor.execute("SELECT * FROM members WHERE id = ?", (id_value,))
            row = cursor.fetchone()
            if row is not None:
                kick = row[2]
                kick += 1
                cursor.execute("UPDATE members SET kicks = ? WHERE id = ?", (kick, id_value))
                connection.commit()
        except:
            await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< clear >---------#
@client.tree.command(name="clear", description="clears a number of chat messages")
async def clear(interaction: discord.Interaction, amount: int = 0):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        try:
            await interaction.response.send_message("*standby*", ephemeral=True, delete_after=1)
            await channel.purge(limit=amount + 0)
            embed = discord.Embed(title=f"{interaction.user.name} cleared {amount} Messages",
                                  color=discord.Colour.from_rgb(177, 26, 33))
            embed.add_field(name="🆔 **User ID**", value=interaction.user.id)
            embed.add_field(name="📆**Cleared Messages At**", value=interaction.created_at.strftime("%d/%m/%Y %H:%M:%S"))
            embed.set_footer(text="🌌 Cosmos • VampiricShadow")
            await channel.send(embed=embed,  delete_after=5)
            log = client.get_channel(990388132815990824)
            await log.send(embed=embed)
        except ValueError:
            await interaction.response.send_message("*Please enter a valid number of messages to be deleted*", ephemeral=True, delete_after=5)
    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< unmute >---------#
@client.tree.command(name="unmute", description="unmutes a user from the chat")
async def unmute_user(interaction: discord.Interaction, user: discord.User, reason: str = None):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        await channel.set_permissions(user, send_messages=True)
        embed = discord.Embed(
            title=f"**{user.name} has been unmuted by {interaction.user.name}**", color=discord.Colour.from_rgb(177, 26, 33))
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.add_field(name="📆**Unmuted on**", value=interaction.created_at.strftime("%d/%m/%Y %H:%M:%S"))
        embed.set_footer(text="🌌 Cosmos • VampiricShadow")
        await interaction.response.send_message(embed=embed)
        log = client.get_channel(990388132815990824)
        await log.send(embed=embed)
    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< mute >---------#
@client.tree.command(name="mute", description="mutes a user from the chat")
async def mute_user(interaction: discord.Interaction, user: discord.User, reason: str = None, time: int = 0):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        await channel.set_permissions(user, send_messages=False)
        embed = discord.Embed(
            title=f"**{user.name} has been muted by {interaction.user.name}**", color=discord.Colour.from_rgb(177, 26, 33))
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.add_field(name="📆**Muted on**", value=interaction.created_at.strftime("%d/%m/%Y %H:%M:%S"))
        embed.add_field(name="🕒**Muted for**", value=f"{time} seconds")
        embed.set_footer(text="🌌 Cosmos • VampiricShadow")
        await interaction.response.defer()
        await interaction.followup.send(embed=embed)
        log = client.get_channel(990388132815990824)
        await log.send(embed=embed)
        await asyncio.sleep(time)
        await channel.set_permissions(user, send_messages=True)
        id_value = user.id
        cursor.execute("SELECT * FROM members WHERE id = ?", (id_value,))
        row = cursor.fetchone()
        if row is not None:
            mute = row[3]
            mute += 1
            cursor.execute("UPDATE members SET mutes = ? WHERE id = ?", (mute, id_value))
            connection.commit()
    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< info >---------#
@client.tree.command(name="info", description="shows information about a player")
async def info(interaction: discord.Interaction, user: discord.User):
    if interaction.user.guild_permissions.kick_members:
        id_value = user.id
        cursor.execute("SELECT * FROM members WHERE id = ?", (id_value,))
        row = cursor.fetchone()
        if row is not None:
            bans = row[1]
            kicks = row[2]
            mutes = row[3]
            warns = row[4]
        else:
            bans = 0
            kicks = 0
            mutes = 0
            warns = 0
        embed = discord.Embed(
            title=f"**information about {user.name}**", color=discord.Colour.from_rgb(177, 26, 33))
        embed.add_field(name="⛔️ **Bans**", value=bans)
        embed.add_field(name="🚫 **Kicks**", value=kicks)
        embed.add_field(name="🔕 **Mutes**", value=mutes)
        embed.add_field(name="❗️ **Warns**", value=warns)
        embed.set_footer(text="🌌 Cosmos • VampiricShadow")
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< warn >---------#
@client.tree.command(name="warn", description="warns a player")
async def warn(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if interaction.user.guild_permissions.manage_messages:
        id_value = user.id
        cursor.execute("SELECT * FROM members WHERE id = ?", (id_value,))
        row = cursor.fetchone()
        if row is not None:
            warn = row[4]
            warn += 1
            cursor.execute("UPDATE members SET warns = ? WHERE id = ?", (warn, id_value))
            connection.commit()
        embed = discord.Embed(title=f"**{user.name} has been warned by {interaction.user.name}**", color=discord.Colour.from_rgb(177, 26, 33))
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.add_field(name="❗️ **Warns**", value=warn)
        embed.set_footer(text="🌌 Cosmos • VampiricShadow")
        await interaction.response.send_message(embed=embed)
        log = client.get_channel(990388132815990824)
        await log.send(embed=embed)

    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< reset >---------#
@client.tree.command(name="reset", description="Resets the database entries for a user")
async def reset(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if interaction.user.guild_permissions.administrator:
        id_value = user.id
        cursor.execute("SELECT * FROM members WHERE id = ?", (id_value,))
        row = cursor.fetchone()
        if row is not None:
            bans = row[1]
            kicks = row[2]
            mutes = row[3]
            warns = row[4]
            levels = row[5]
            xp = row[6]
        else:
            bans = 0
            kicks = 0
            mutes = 0
            warns = 0
            levels = 0
            xp = 0
        embed = discord.Embed(
            title=f"**information about {user.name} was deleted by: {interaction.user.name}**", color=discord.Colour.from_rgb(177, 26, 33))
        embed.add_field(name="⛔️ **Bans**", value=bans)
        embed.add_field(name="🚫 **Kicks**", value=kicks)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.add_field(name="🔕 **Mutes**", value=mutes)
        embed.add_field(name="❗️ **Warns**", value=warns)
        embed.add_field(name="📆**Date**", value=interaction.created_at.strftime("%d/%m/%Y %H:%M:%S"))
        embed.set_footer(text="🌌 Cosmos • VampiricShadow")
        log = client.get_channel(990388132815990824)
        await log.send(embed=embed)

        cursor.execute("DELETE FROM members WHERE id = ?", (id_value,))
        params = (
        user.id,
        0,
        0,
        0,
        0,
        0,
        0)
        try:
            cursor.execute(f"INSERT INTO members VALUES (?, ?, ?, ?, ?, ?, ?);", params)
            connection.commit()
            await interaction.response.send_message("*success*", ephemeral=True, delete_after=5)
        except Exception as e:
            print(e)
    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)



#############################
#---------< utils >---------#
#############################



#---------< server info >---------#
@client.tree.command(name="serverinfo", description="shows you basic info about the server")
async def serverinfo(interaction: discord.Interaction):
    server = interaction.guild
    embed = discord.Embed(title=f"Server Info for {server.name}", color=discord.Colour.from_rgb(177, 26, 33))
    embed.add_field(name="💬**Server Name**", value=server.name)
    embed.add_field(name="🆔**Server ID**", value=server.id)
    embed.add_field(name="📆**Created On**", value=server.created_at.strftime('%d/%m/%Y'))
    embed.add_field(name="👑**Server Owner**", value=server.owner)
    embed.add_field(name="👥**Server Member Count**", value=server.member_count)
    embed.set_thumbnail(url=server.icon.url)
    embed.set_footer(text="🌌 Cosmos • VampiricShadow")
    await interaction.response.send_message(embed=embed)


#---------< avatar >---------#
@client.tree.command(name="avatar", description="prints the users avatar")
async def avatar(interaction: discord.Interaction, user: discord.User):
    embed = discord.Embed(title=f"**{user}s Avatar:**", color=discord.Colour.from_rgb(177, 26, 33)).set_image(url=user.avatar.url)
    embed.set_footer(text="🌌 Cosmos • VampiricShadow")
    await interaction.response.send_message(embed=embed)


#---------< suggest >---------#
@client.tree.command(name="suggest", description="suggest things")
async def suggest(interaction: discord.Interaction, suggestion: str = None):
    channel = client.get_channel(1065075901974450298)
    try:
        embed = discord.Embed(title=f"{interaction.user.name}", color=discord.Colour.from_rgb(177, 26, 33))
        embed.add_field(name="💬**Suggestion**", value=suggestion)
        await channel.send(embed=embed)
        await interaction.response.send_message("*successfully sent!*", ephemeral=True, delete_after=5)
    except Exception as e:
        await interaction.response.send_message("*Message to long! Please try Explaining your thoughts more briefly!*", ephemeral=True, delete_after=10)
        print("Suggestion")
        print(e)


#---------< announce >---------#
@client.tree.command(name="announce", description="Write a uniform announcement")
async def announce(interaction: discord.Interaction, title: str = None, announcement: str = None):
    if interaction.user.guild_permissions.ban_members:
        channel = client.get_channel(1127244767714095165)
        try:
            embed = discord.Embed(title="💬**Announcement**", color=discord.Colour.from_rgb(177, 26, 33))
            embed.add_field(name=title, value=announcement)
            await channel.send(embed=embed)
            await interaction.response.send_message("*successfully sent!*", ephemeral=True, delete_after=5)
        except Exception as e:
            await interaction.response.send_message("*Message to long! Please try Explaining your thoughts more briefly!*", ephemeral=True, delete_after=10)
            print("Announcement")
            print(e)
    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< ping >---------#
@client.tree.command(name="ping", description="shows the latency of the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"*pong! My ping is {round(client.latency * 1000)}ms*", ephemeral=True)


#---------< level >---------#
@client.tree.command(name="level", description="displays your level")
async def level(interaction: discord.Interaction):
    id_value = interaction.user.id
    cursor.execute("SELECT * FROM members WHERE id = ?", (id_value,))
    row = cursor.fetchone()
    level = row[5]
    xp = row[6]

    userData = {
        "name": f"{interaction.user.name}",
        "xp": xp,
        "level": level,
        "next_level_xp": 100,
        "percentage": xp,
    }

    background = Editor(Canvas((900, 300), color="#141414"))
    profilePicture = await load_image_async(str(interaction.user.avatar.url))
    profile = Editor(profilePicture).resize((150,150)).circle_image()

    poppins = Font.poppins(size=40)
    poppins_small = Font.poppins(size=30)

    cardShape = [(600, 0), (750, 300), (900, 300), (900, 0)]

    background.polygon(cardShape, color="#b11a21")
    background.paste(profile, (30, 30))

    background.rectangle((30, 220), width=650, height=40, color="#2D2424", radius=20,)
    background.bar((30, 220), max_width=650, height=40, percentage=userData["percentage"], color="#b11a21", radius=20,)
    background.text((200, 40), userData["name"], font=poppins, color="#b11a21")

    background.rectangle((200, 100), width=350, height=2, fill="#b11a21")
    background.text((200, 130), f"Level - {userData['level']} | XP - {userData['xp']}/{userData['next_level_xp']}", font=poppins_small, color="#b11a21")

    file = discord.File(fp=background.image_bytes, filename="levelcard.png")
    await interaction.response.send_message(file=file)


#---------< set level >---------#
@client.tree.command(name="setlevel", description="displays your level")
async def setlevel(interaction: discord.Interaction, user: discord.User, level: int = 0):
    if interaction.user.guild_permissions.administrator:
        if level >= 200:
            await user.add_roles(interaction.guild.get_role(1127579753663172608))
        elif level >= 160:
            await user.add_roles(interaction.guild.get_role(1127583438690603079))
        elif level >= 130:
            await user.add_roles(interaction.guild.get_role(1127583471947235338))
        elif level >= 115:
            await user.add_roles(interaction.guild.get_role(1127583507514929294))
        elif level >= 90:
            await user.add_roles(interaction.guild.get_role(1127583535272820737))
        elif level >= 80:
            await user.add_roles(interaction.guild.get_role(1127583573856239627))
        elif level >= 70:
            await user.add_roles(interaction.guild.get_role(1127583602851446814))
        elif level >= 60:
            await user.add_roles(interaction.guild.get_role(1127583919001313450))
        elif level >= 50:
            await user.add_roles(interaction.guild.get_role(1127583980565299273))
        elif level >= 45:
            await user.add_roles(interaction.guild.get_role(1127584069883019375))
        elif level >= 40:
            await user.add_roles(interaction.guild.get_role(1127584121418416178))
        elif level >= 35:
            await user.add_roles(interaction.guild.get_role(1127584186715353098))
        elif level >= 30:
            await user.add_roles(interaction.guild.get_role(1127584248652627999))
        elif level >= 25:
            await user.add_roles(interaction.guild.get_role(1127584304713695323))
        elif level >= 20:
            await user.add_roles(interaction.guild.get_role(1127584356777599047))
        elif level >= 15:
            await user.add_roles(interaction.guild.get_role(1127584401342091314))
        elif level >= 10:
            await user.add_roles(interaction.guild.get_role(1127584455456981002))
        elif level >= 5:
            await user.add_roles(interaction.guild.get_role(1127584523702521916))
        elif level >= 0:
            await user.add_roles(interaction.guild.get_role(1127584577683202148))

        level = level
        id_value = user.id
        cursor.execute("UPDATE members SET level = ? WHERE id = ?", (level, id_value))
        connection.commit()

        await interaction.response.send_message(
            f"*Successfully updated the level of {user} to Lvl {level}*", ephemeral=True, delete_after=5
        )

    else:
        await interaction.response.send_message(
            "*Insufficient permission*", ephemeral=True, delete_after=5
        )



#---------< Verify Button >---------#
class verifyButton(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Verify", style=discord.ButtonStyle.green, emoji="✔️", custom_id="verify")
    async def close(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer(ephemeral=True)
        await interaction.user.add_roles(interaction.guild.get_role(959811526842282036))


#---------< verify command >---------#
@client.tree.command(name="verify", description="verification")
async def verify(interaction: discord.Interaction):
    if interaction.guild.get_role(959811526842282036) not in interaction.user.roles:
        embed=discord.Embed(description="If you have understood the rules please press the Verification button!", color=discord.Colour.from_rgb(177, 26, 33))
        embed.set_footer(text="🌌 Cosmos • VampiricShadow")
        await interaction.response.send_message(embed=embed, view=verifyButton(), ephemeral=True, delete_after=120)                                                                                                                                                                                                                               
    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)


#---------< rules >---------#
@client.tree.command(name="rules", description="rules")
async def rules(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title=f"**Rules**", color=discord.Colour.from_rgb(177, 26, 33))
        embed.add_field(name="**1.) Follow Discord's TOS**", value="Be sure to follow Discord's TOS found at https://discordapp.com/tos. You must be 13 to use Discord, so if you admit to being under 13, you will be banned from the server.", inline=False)
        embed.add_field(name="**2.) Be Respectful**", value="Racist, sexist, homophobic, xenophobic, transphobic, ableist, hate speech, slurs, or any other derogatory, toxic, or discriminatory behavior will not be tolerated.", inline=False)
        embed.add_field(name="**3.) No Spamming**", value="Including but not limited to: any messages that do not contribute to the conversation, repeated messages, linebreaking, randomly tagging users, and chat flood.", inline=False)
        embed.add_field(name="**4.) English**", value="The primary language of the server is English, please keep all discussions in English.", inline=False)
        embed.add_field(name="**5.) Safe for Work**", value="Please keep NSFW and NSFL content out of this server, avoid borderline images as well as keeping your status and profile picture SFW.", inline=False)
        embed.add_field(name="**6.) No Advertising**", value="Do not promote anything without prior approval from a staff member, this includes DM advertising.", inline=False)
        embed.add_field(name="**7.) Impersonation**", value="Do not try to impersonate others for the express intent of being deceitful, defamation, and/or personal gain.", inline=False)
        embed.add_field(name="**8.) Swearing**", value="Swearing is allowed only when not used as an insult.", inline=False)
        embed.add_field(name="**9.) Sending videos/GIFs that are able to crash a user's Discord**", value="Sending videos/GIFs that are able to do this will result in a permanent ban that cannot be appealed.", inline=False)
        embed.add_field(name="**10.) No Backseat Moderating**", value="If you see a rule being broken be broken, please report it using a ticket: /ticket", inline=False)
        embed.add_field(name="**11.) Staff may moderate at their discretion**", value="If there are loopholes in our rules, the staff team may moderate based on what they deem appropriate. The staff team holds final discretion.", inline=False)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("*insufficient permission*", ephemeral=True, delete_after=5)




###############################
#---------< tickets >---------#
###############################



#---------< Ticket Button >---------#
class CreateButton(View):
    def __init__(self):
        super().__init__(timeout=None)


    @button(label="Create Ticket", style=discord.ButtonStyle.blurple, emoji="🎟️", custom_id="ticketopen")
    async def ticket(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer(ephemeral=True)
        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id=1127316268173758674)
        for ch in category.text_channels:
            if ch.topic == f"{interaction.user.id} DO NOT CHANGE TE TOPIC OF THIS CHANNEL!":
                await interaction.followup.send("You already have a ticket in {0}".format(ch.mention), ephemeral=True)
                return
        r1: discord.Role = interaction.guild.get_role(959813484294586409)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            r1: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages = True, send_messages=True),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel = await category.create_text_channel(
            name=str(interaction.user),
            topic=f"{interaction.user.id} DO NOT CHANGE TE TOPIC OF THIS CHANNEL!",
            overwrites=overwrites
        )

        embed=discord.Embed(title="**Ticket Created!**", description="Don't ping a staff member, they will be here soon.", color=discord.Colour.from_rgb(177, 26, 33))
        embed.set_footer(text="🌌 Cosmos • VampiricShadow")
        await channel.send(embed=embed, view=CloseButton())


#---------< Close Button >---------#
class CloseButton(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Close Ticket", style=discord.ButtonStyle.red, emoji="🔒", custom_id="closeticket")
    async def close(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer(ephemeral=True)

        await interaction.channel.send("Closing this ticket in 3 seconds")
        await asyncio.sleep(3)

        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id=1127317613903626411)

        r1: discord.Role = interaction.guild.get_role(959813484294586409)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            r1: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages = False, send_messages=False),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        await interaction.channel.edit(category=category, overwrites=overwrites)


#---------< ticket cmd >---------#
@client.tree.command(name="ticket", description="create a ticket")
async def ticket(interaction: discord.Interaction):
    embed=discord.Embed(description="Press the button to open a new ticket!", color=discord.Colour.from_rgb(177, 26, 33))
    embed.set_footer(text="🌌 Cosmos • VampiricShadow")
    await interaction.response.send_message(embed=embed, view=CreateButton(), ephemeral=True, delete_after=120)
    


##############################
#---------< events >---------#
##############################



#---------< on member join >---------#
@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined the Server")
    server = member.guild
    embed = discord.Embed(title=f"**Welcome {member.name}**👋", color=discord.Colour.from_rgb(177, 26, 33))
    embed.add_field(name="📚**Rules**", value="Please make sure that you read the rules")
    embed.add_field(name="❓**Support**", value="If you have any questions open a ticket ")
    embed.add_field(name="🍿**Enjoy**", value=f"Have Fun and enjoy chatting and talking on the Server **{server.name}**")
    embed.set_footer(text="🌌 Cosmos • VampiricShadow")
    try:
        await member.send(embed=embed)
    except Exception as e:
        print(f"{member} Does not allow direct messages!")
        print(e)
    params = (
    member.id,
    0,
    0,
    0,
    0,
    0,
    0)
    try:
        cursor.execute(f"INSERT INTO members VALUES (?, ?, ?, ?, ?, ?, ?);", params)
        connection.commit()
    except Exception as e:
        print(e)



#--------< on message >---------#
@client.event
async def on_message(message):
    #--------< filter >---------#
    if message.author.bot:
        return
    for word in blacklist:
        if word in message.content:
            if message.author.id !=377185902998323203:
                await message.channel.set_permissions(message.author, send_messages=False)
                embed = discord.Embed(
                    title=f"**{message.author.name}** has been automatically  muted by  **Cosmos**", color=discord.Colour.from_rgb(177, 26, 33))
                embed.add_field(name="🆔**User ID**", value=message.author.id)
                embed.add_field(name="💬**Reason**", value="using blacklisted word")
                embed.add_field(name="📆**Muted on**", value=message.created_at.strftime("%d/%m/%Y %H:%M:%S"))
                # embed.set_thumbnail(url=client.avatar.url)
                embed.set_footer(text="🌌 Cosmos • VampiricShadow")
                await message.channel.send(embed=embed)
                log = client.get_channel(990388132815990824)
                await log.send(embed=embed)
            else:
                print(f"mute prevented on {message.author}")

    #--------< level >---------#
    id_value = message.author.id
    cursor.execute("SELECT * FROM members WHERE id = ?", (id_value,))
    row = cursor.fetchone()
    level = row[5]
    xp = row[6]


    if level < 5:
        xp += random.randint(1,3)
        cursor.execute("UPDATE members SET xp = ? WHERE id = ?", (xp, id_value))

    else:
        rand = random.randint(1, (level//4))
        if rand == 1:
            xp += random.randint(1,3)
            cursor.execute("UPDATE members SET xp = ? WHERE id = ?", (xp, id_value))
    if xp >= 100:
        level += 1
        xp = 0
        cursor.execute("UPDATE members SET level = ? WHERE id = ?", (level, id_value))
        cursor.execute("UPDATE members SET xp = ? WHERE id = ?", (xp, id_value))
        await message.channel.send(f"*{message.author.mention} has leveled up to {level}*")
    connection.commit()

    if level >= 200:
        await message.author.add_Roles(message.guild.get_role(1127579753663172608))
    elif level >= 160:
        await message.author.add_roles(message.guild.get_role(1127583438690603079))
    elif level >= 130:
        await message.author.add_roles(message.guild.get_role(1127583471947235338))
    elif level >= 115:
        await message.author.add_roles(message.guild.get_role(1127583507514929294))
    elif level >= 90:
        await message.author.add_roles(message.guild.get_role(1127583535272820737))
    elif level >= 80:
        await message.author.add_roles(message.guild.get_role(1127583573856239627))
    elif level >= 70:
        await message.author.add_roles(message.guild.get_role(1127583602851446814))
    elif level >= 60:
        await message.author.add_roles(message.guild.get_role(1127583919001313450))
    elif level >= 50:
        await message.author.add_roles(message.guild.get_role(1127583980565299273))
    elif level >= 45:
        await message.author.add_roles(message.guild.get_role(1127584069883019375))
    elif level >= 40:
        await message.author.add_roles(message.guild.get_role(1127584121418416178))
    elif level >= 35:
        await message.author.add_roles(message.guild.get_role(1127584186715353098))
    elif level >= 30:
        await message.author.add_roles(message.guild.get_role(1127584248652627999))
    elif level >= 25:
        await message.author.add_roles(message.guild.get_role(1127584304713695323))
    elif level >= 20:
        await message.author.add_roles(message.guild.get_role(1127584356777599047))
    elif level >= 15:
        await message.author.add_roles(message.guild.get_role(1127584401342091314))
    elif level >= 10:
        await message.author.add_roles(message.guild.get_role(1127584455456981002))
    elif level >= 5:
        await message.author.add_roles(message.guild.get_role(1127584523702521916))
    elif level >= 0:
        await message.author.add_roles(message.guild.get_role(1127584577683202148))


# Run the bot
client.run(os.getenv("TOKEN"))
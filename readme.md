# Discord Bot Readme

## Language Versions
[![English](https://img.shields.io/badge/English-English-blue)](readme.md)
[![German](https://img.shields.io/badge/German-German-blue)](readme_de.md)
[![Spanish](https://img.shields.io/badge/Spanish-Spanish-blue)](readme_es.md)

Welcome to the documentation for **Cosmos**, a versatile and powerful Discord bot designed to enhance the experience on your server. This readme provides an overview of the bot's features and how to use them effectively.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Bot Commands](#bot-commands)
- [Contribution](#contribution)

## Introduction

**Cosmos** is a Discord bot designed to make your server more interactive and entertaining. It comes with a range of features that enable moderation, entertainment, information retrieval, and more. Whether you manage a gaming community, a study group, or any other type of server, **Cosmos** has something to offer.

## Getting Started

### Prerequisites

- An account on [Discord](https://discord.com/)
- Access to a Discord server where you have administrator permissions

### Installation

#### Step 1: Discord Developer Portal

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications/).
2. Log in with your Discord account.

#### Step 2: Create a New Application

1. Click the "New Application" button.
2. Enter a name for your application (this will be your bot's name).
3. Click "Create."

#### Step 3: Create a Bot

1. In the left menu, select "Bot."
2. Click "Add Bot."
3. Confirm the action with "Yes, do it!"

#### Step 4: Copy Bot Token

1. Under the "TOKEN" section, you will find your bot token. Click "Copy" to copy the token to your clipboard. Note: Keep this token secret, as it grants access to your bot.

#### Step 5: Invite the Bot to a Server

1. Return to your application page by clicking on the application name in the top left.
2. In the left menu, select "OAuth2."
3. In the "OAuth2 URL Generator," select "bot" and "applications.commands" under Scopes.
4. Choose the permissions your bot should have (e.g., "Read Messages," "Send Messages," etc.). The bot should have administrator permissions.
5. Copy the generated OAuth2 link and paste it into your web browser.
6. Select a server to invite your bot to and confirm the invitation.

#### Step 6: Configure the Bot

# Configuration

The `config.json` file allows you to customize various aspects of the **Cosmos** bot to fit the needs of your server. Here's a breakdown of the configuration options:

- **name:** The display name of the bot on the server.
- **id:** The ID of the bot.
- **activity:** The activity status displayed for the bot (e.g., "Watching over the universe.").
- **owner:** The ID of the bot owner who has special privileges.

### Channels

- **log_channel:** The channel where bot activity logs and notifications are sent.
- **announcement_channel:** The channel for important team announcements to the server.
- **suggestion_channel:** The channel where users can submit suggestions.
- **ticket_category:** The category for creating support ticket channels.
- **closed_category:** The category to which closed or completed ticket channels are moved.

### Roles

- **verify_role:** The role assigned to users after they are verified.
- **ticket_role:** The role granted to users who have access to moderate support tickets.
- **double_xp_role:** The role that grants users double experience points on the server.

Additionally, the main bot file allows you to map roles to specific levels for a leveling system. The `roles` dictionary maps levels to their corresponding role IDs. Users are assigned these roles when they reach the specified levels. To add or remove roles and levels, you can edit this dictionary.

```py
roles = {
    0:   1127584577683202148,
    5:   1127584523702521916,
    10:  1127584455456981002,
    15:  1127584401342091314,
    20:  1127584356777599047,
    25:  1127584304713695323,
    30:  1127584248652627999,
    35:  1127584186715353098,
    40:  1127584121418416178,
    45:  1127584069883019375,
    50:  1127583980565299273,
    60:  1127583919001313450,
    70:  1127583602851446814,
    80:  1127583573856239627,
    90:  1127583535272820737,
    115: 1127583507514929294,
    130: 1127583471947235338,
    160: 1127583438690603079,
    200: 1127579753663172608
}
```

### Token

1. Create a file named `.env` in the same folder where `index.py` is located.
2. Add the following line to it: `TOKEN = "YourToken"` replacing `YourToken` with the actual bot token.

#### Step 7: Run the Code

1. Make sure you have Python installed. If not, you can download it [here](https://www.python.org/downloads/).
2. Install the Python packages: `pip install -r requirements.txt`
3. Run your code.
Your bot should now log into Discord and respond to commands or events.

## Bot Commands

Here are some of the key commands supported by **Cosmos**:

### Ban

- **Description:** Bans a user from the server.
- **Usage:** `/ban [user] [reason]`

### Kick

- **Description:** Kicks a user from the server.
- **Usage:** `/kick [user] [reason]`

### Mute

- **Description:** Mutes a user (they cannot write after being muted).
- **Usage:** `/mute [user] [reason]`

### Unmute

- **Description:** Unmutes a user.
- **Usage:** `/unmute [user] [reason]`

### Clear

- **Description:** Deletes a number of messages in a channel.
- **Usage:** `/clear [count]`

### Info

- **Description:** Displays a user's infraction history stored in `users.db`.
- **Usage:** `/info [user]`

### Warn

- **Description:** Warns a user.
- **Usage:** `/warn [user] [reason]`

### Reset

- **Description:** Resets a user's information (infraction history, level). It can also be used to add users to the database.
- **Usage:** `/reset [user] [reason]`

### Server Info

- **Description:** Displays information about the server.
- **Usage:** `/serverinfo`

### Avatar

- **Description:** Provides you with a user's avatar (profile picture).
- **Usage:** `/avatar [user]`

### Suggest

- **Description:** Allows users to submit suggestions to the team.
- **Usage:** `/suggest [message]`

### Announce

- **Description:** Allows the team to send uniform announcements to users.
- **Usage:** `/announce [message]`

### Ping

- **Description:** Displays the bot's ping.
- **Usage:** `/ping`

### Rank

- **Description:** Shows your level.
- **Usage:** `/rank`

### Set Level

- **Description:** Sets a user's level.
- **Usage:** `/level [user] [level]`

### Verify

- **Description:** Allows users to verify themselves.
- **Usage:** `/verify`

### Rules

- **Description:** Sends the server rules (these must be manually changed in `index.py` at lines 526-536).
- **Usage:** `/rules`

### Ticket

- **Description:** Allows users to create a support ticket.
- **Usage:** `/ticket`

## Contribution

We welcome contributions from the community! If you'd like to contribute to **Cosmos**, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Add your improvements or bug fixes.
4. Submit a pull request.

Thank you for choosing **Cosmos**! We hope this bot brings value and joy to your Discord server. If you have any suggestions or feature requests, please don't hesitate to let us know!

## License

This project is licensed under the [GNU General Public License, version 3.0](LICENSE). You can find the full license text [here](https://www.gnu.org/licenses/gpl-3.0.html).

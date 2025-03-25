# Overview
Steambot is a Discord bot written in Python using discord.py library. It provides various functionalities, including administrative commands and RapidAPI Steam API integration.

# Structure
- **main.py** - Entry point, loading cogs
- **Admin.py** - Cog responsible for administrative commands
- **Error_Handler.py** - Cog responsible for handling various errors in order to prevent bot from crashing
- **SteamAPI.py** - Cog responsible for creating requests to a Steam API

# Installation

1. Clone the repository (duh!)
```bash
git clone https://github.com/Asttraios/Steambot_Basic.git
cd Steambot_Basic
```
3. Receive your Discord Token [HERE](https://discord.com/developers/applications)

4. Sign in and receive your RapidAPI Steam API Key [HERE](https://rapidapi.com/psimavel/api/steam2/playground) 

5. In the project directory create .env file and add:
```bash
STEAM_API_KEY={INSERT YOUR STEAM API KEY (WITHOUT ANY BRACKETS) }
DISCORD_CLIENT_KEY={INSERT YOUR DISCORD TOKEN (WITHOUT ANY BRACKETS)}
```
6. Create virtual environment and activate it
```bash
python -m venv myenv
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
7. Install dependencies
```bash
pip install -r requirements.txt
```
8. Run the bot!
```bash
python main.py
```

# Commands
This is overview of all the commands you can use
## Administrative commands
- **!kick @USER** - kick specified user, requires kick permissions
- **!ban @USER** - ban specified user, requires ban/unban permissions
- **!unban @USER** - unban specified user, requires ban/unban permissions
- **!mute @USER** - mute specified user in voice channel, requires mute permissions
- **!timeout @USER {time in seconds, default=10s} {timeout_reason (optional)}** EXAMPLE: !timeout @user 10 spamming - requires timeout permissions

## Steam search commands
- !steamsearch {Name of the game} EXAMPLE: !steamsearch Helldivers 2.
Gives you information about:
- ✅ Game's Name<br/>
- ✅ Short Description<br/>
- ✅ Developer<br/>
- ✅ Publisher<br/>
- ✅ Current Price
- ✅ Release Date<br/>
- ✅ Steam Review<br/>
- ✅ Game's cover image

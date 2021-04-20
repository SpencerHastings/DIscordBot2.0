# DiscordBot 2.0

## Goal
Fully modular Discord bot where any feature can be enabled and disabled in a config file, save some core functionality.

## How to Use
Config file `examples` in config folder, already gitigored so just duplicate the example files without the `.example` extension and then change accordingly.

## How to make an addition
This bot separates functionality into cogs using discord.py. In the `modules` folder there is are folders and each python file inside the folders is a cog. After making a cog, unless it is an essential cog, add a feature toggle by adding an entry to the `features` dictionary in `config/settings.py`. To make sure the bot enables the cog, in `cogs.py` add the cog, and if there was a feature toggle added to the settings, make the cog adding be conditional on that dictionary value.

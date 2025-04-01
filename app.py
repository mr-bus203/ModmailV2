{
    "name": "Modmail",
    "description": "An easy to install Modmail bot for Discord - DM to contact mods!",
    "repository": "https://github.com/modmail-dev/modmail",
    "env": {
        "TOKEN": {
            "description": "Your discord bot's token.",
        },
        "GUILD_ID": {
            "description": "The id for the server you are hosting this bot for.",
        },
        "OWNERS": {
            "description": "Comma separated user IDs of people that are allowed to use owner only commands. (eval).",
        },
        "CONNECTION_URI": {
            "description": "The connection URI for your database.",
        },
        "DATABASE_TYPE": {
            "description": "The type of your database. There is only one supported database at the moment - MongoDB (default)."
        },
        "LOG_URL": {
            "description": "The url of the log viewer app for viewing self-hosted logs.",
        },
        "GITHUB_TOKEN": {
            "description": "A github personal access token with the repo scope.",
        },
        "REGISTRY_PLUGINS_ONLY": {
            "description": "If set to true, only plugins that are in the registry can be loaded.",
        }
    }
}

Garage Bot
======

Spectacular Telegram bot for group chats making all the interactions fun. There's nothing related to garages in it.


## Requirements

It is coded in `Python 3.6+` (f-strings are used everywhere). Following are the modules which are needed/used for various things.

- `python-telegram-bot`
- `google-api-python-client`


## Running the bot

First setup up the bot according to your needs. `bot/bot_setup.py` will help you with that. It'll do the following steps in order:

1. Make an empty `sqlite3` db in `assets` directory;
2. Make the chats table in the chats.db. Default table name is `CHATS`. If you want to change the table name, update the `chat_table` variable in the `config.ini` file;
3. Make an empty `assets/users.txt` file which should contain the set of telegram user ids which will have access to the bot and its features. Leave it blank to enable everyone to use it. Note that, this will also **enable strangers** to use the bot. So, have an exhaustive list of user ids if you don't want everyone to use the bot;
4. Make an empty `assets/start.txt` file which should contain the set of greeting messages the bot can use when `/start` (or `/s`) command is used;
5. Make an empty `assets/key_val.json` file which will contain the important things you want to keep in your reach whenever you want it with just a call to `/fetch`;

To execute all these steps, run

```
python bot/bot_setup.py
```

Now to run the bot, execute the following instruction:

```
python garagebot/bot.py
```

## Run Tests

To run the unit tests run the following command.

```
python tests/run_tests.py
```

To individually test a specific module run that particular ```test_*.py``` file.


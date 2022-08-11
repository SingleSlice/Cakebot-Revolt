# Cakebot

this is a dumb roleplay bot thing can be used as somewhat of a pluralkit alternative.\
its function are:
-   managing characters per user.
    -   creating characters.
    -   editing characters.
    -   deleting characters.

-   sending messages as those characters.
-   thats all for now.

##  hosting your own instance of this bot.

clone this repo, and install the following python dependencies
-   voltage==0.1.5a8
-   pymongo==4.2.0

then make a config file named configCakebot.py with the following variables:
-   token   (str) => Your revolt bot token.
-   prefix  (str) => The bot's prefix. ex prefix = ">>"

-   connectionString    (str) => Your mongodb's database connection string
-   serverDatabase      (str) => The server settings collection's name
-   userDatabase        (str) => The user characters collection's name

-   max_oc_user (int) => the maximum number of characters each user can make.
# zeltir
Automating the inventory of toys and reworking the report from a beautiful table into a terrible format, which was needed by my boss at that time

# In general, why, and what is it?
The story began simply - I got a job at a low rate at a shooting range with pneumatics and mediocre quality toys through some acquaintances. 
Everything was going well until one moment: Until the recount. We sent the recount in the worst possible way - a message in a telegram and it was painful to watch.

It doesn't even fit on one screen:

![THIS is what needed to be dealt with](https://i.imgur.com/8AKTfID.png)

This report was made by a person manually, you can see that some numbers are simply missing, you can often find errors in calculating the amount and everything else that depends on the human factor.

# How to fix it

Entering values ​​into a message one by one is disgusting and unpleasant, so we have a great option - a table. I created a table in Google Sheets and gave everyone access to it. 
Then I created a service account to collect information from there, so I transfer it to the server in json format and can finally normally operate with at least something.


![Cool table](https://imgur.com/nsJOG1M.png)

The translation into the format of fear, horror and the rapper's boss is done through a telegram bot, for convenience in forwarding the message, no one even suspected anything until I directly told the boss about it

![ugh](https://imgur.com/p0Rrcw6.png)

# Config

All settings are stored in a separate file config.py, there is everything that needs to be changed to connect, say, to another point

# TradingView_Telegram_Bot(Heroku)

## Summary

An automated script to send TradingView alerts to Telegram via webhook.

All the deployment is done in one click with heroku.

## Deploy

1. Deploy to Heroku 

   [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

2. Setup `channel`、`sce_key` and `tg_token`
<img src="https://i.imgur.com/oeeuN2V.png" width="600px">
    
    - channel : Telegram Channel ID. If occur the error "Chat not found" try to add "-100" prefix
    
    - sce_key : Can be any thing. For security check. Only messeage with correct key will send. 
    
    - tg_token : The API key of your telegram bot.

3. All set!

## Use

1. Get your Web address from Heroku

    Settings -> Domains

    Add "webhook" behind

    Example : https://xxxxxxx.herokuapp.com/webhook

2. Set TradingView alert

    Example : 
    ```
    {
      "key" : "sce_key",
      "msg" : "msg you want to send"
    } 
    ```

    If you want to send msg to different Channel. You can use this method. 

    ```
    {
      "key" : "sce_key",
      "telegram" : "Channel ID",
      "msg" : "msg you want to send"
    } 
    ```
    The Channel ID input here will overwrite which one you set in os.env.

    By the way, if you want to test with postman, Post with example as body to your address.

## Optimize

  Heroku's free dyno will turn to idle after 30min from the last request, and the restart will lead a 30s delay.
  
  We can easily use [UptimeRobot](https://uptimerobot.com/) to send requests every 15min.
  
  Set this URL on UptimeRobot: https://xxxxxxx.herokuapp.com/test

## Credit

Modify from repo [fabston/TradingView-Webhook-Botgit](https://github.com/fabston/TradingView-Webhook-Bot)

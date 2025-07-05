import os
import subprocess
import telebot
import shlex
import requests
import time

botToken = os.environ.get('bot_token')

bot = telebot.TeleBot(botToekn)

@bot.message_handler(commands=['buy'])
def run_buy_order(message):
    user_text = message.text

    print("received /buy command")
    info = str(user_text).replace('/buy', '').strip().split()
    print(f"extracted info list: {info}")    

    initial_command = ['/home/user/GoBOT/BUY/main']
    if info:
        initial_command.extend(info)

    final_comand = " ".join(shlex.quote(part) for part in initial_command)
    print(f"final command to run: {final_comand}")

    tmux_command = ['tmux', 'send-keys', '-t', f"s:buy", final_comand, 'Enter'] # s for session :)
    print(f"tmux command: {tmux_command}")
    try:
        res = subprocess.run(tmux_command, check=True)
        print("command sent to tmux successfully")
        bot.reply_to(message, "buy order sent to execution bot.")
    except subprocess.CalledProcessError as e:
        print(f"error sending command to tmux window: {e}")
        bot.reply_to(message, "failed to send buy order")

@bot.message_handler(commands=['stopbuy'])
def stop_buy_order(message):
    print("received /stopbuy command")
    tmux_command = ['tmux', 'send-keys', '-t', f"s:buy", 'C-c']

    try:
        res = subprocess.run(tmux_command, check=True, capture_output=True, text=True)
        print(f"tmux command execution result: {res}") 

        if res.returncode == 0:
            print("buy process stopped successfully")
            reply_message = "ctrl+c signal sent to tmux window."
        else:
            print(f"tmux command error (stderr):\n{res.stderr}")
            reply_message = f"error sending ctrl+c to tmux. tmux error:\n{res.stderr}"

        bot.reply_to(message, reply_message)

    except subprocess.CalledProcessError as e:
        print(f"python subprocess error: {e}")
        bot.reply_to(message, f"error sending ctrl+c to tmux: {e}")

@bot.message_handler(commands=['sell'])
def run_sell_order(message):
    user_text = message.text

    print("received /sell command")
    info = str(user_text).replace('/sell', '').strip().split()
    print(f"extracted info list: {info}")    

    initial_command = ['/home/SKYINR/GoBOT/SELL/main']
    if info:
        initial_command.extend(info)

    final_comand = " ".join(shlex.quote(part) for part in initial_command)
    print(f"final command to run: {final_comand}")

    tmux_command = ['tmux', 'send-keys', '-t', f"s:sell", final_comand, 'Enter']
    print(f"tmux command: {tmux_command}")
    try:
        res = subprocess.run(tmux_command, check=True)
        print("command sent to tmux successfully")
        bot.reply_to(message, "sell order sent to execution bot.")
    except subprocess.CalledProcessError as e:
        print(f"error sending command to tmux window: {e}")
        bot.reply_to(message, "failed to send sell order")

@bot.message_handler(commands=['stopsell'])
def stop_sell_order(message):
    print("received /stopsell command")
    tmux_command = ['tmux', 'send-keys', '-t', f"s:sell", 'C-c']

    try:
        res = subprocess.run(tmux_command, check=True, capture_output=True, text=True)
        print(f"tmux command execution result: {res}") 

        if res.returncode == 0:
            print("sell process stopped successfully")
            reply_message = "ctrl+c signal sent to tmux window."
        else:
            print(f"tmux command error (stderr):\n{res.stderr}")
            reply_message = f"error sending ctrl+c to tmux. tmux error:\n{res.stderr}"

        bot.reply_to(message, reply_message)

    except subprocess.CalledProcessError as e:
        print(f"python subprocess error: {e}")
        bot.reply_to(message, f"error sending ctrl+c to tmux: {e}")


telegram trade bot

a telegram bot for me to control trading scripts from a private chat.
commands
    
    /buy <coin> <price> <pre..> — starts buy script
    
    /sell <coin> <price> <pre..> — starts sell script
    
    /stopbuy — stops the buy script
    
    /stopsell — stops the sell script

how it works

    each command sends a message to a tmux session running go executables

    profit is calculated based on my algo and subtracts 1.5% fees

    bot is not public  only works in authorized telegram chat

run
set your bot token and run:

export botToekn=your_token
python3 main.py

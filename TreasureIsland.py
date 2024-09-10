print("""
              _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.' U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-U.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

""")

print("""
WELCOME TO THE TREASURE ISLAND
YOUR FIRST MISSION IS TO FIND THE TREASURE!
""")
choice1 = input("You are at a crossroad.Where do you want to go left or right?").lower()

if choice1 == 'left':
    choice2 = input("You have come across a lake.Do you want to swim or wait").lower()
    if choice2 == "wait":
        choice3 = input("""You have come across 3 doors : Red , Blue and Yellow.
             Which Do you Choose?""").lower()
        if choice3 == "red":
            print("It is a room full of fire.GAME OVER")
        elif choice3 == "blue":
            print("YOU HAVE BEEN EATEN BY TH BEASTS.GAME OVER")
        elif choice3 == "yellow":
            print("YOU WIN")
        else:
            print("You choose a door that doesn't exist.GAME OVER")
    else:
        print("Attacked by Tout.GAME OVER")
else :
    print("GAME OVER")



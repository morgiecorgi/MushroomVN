# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg test = "./images/backgrounds/hallwaytest.png"
image wizard normal = "./images/chars/wizard.png"
image Fogpart = SnowBlossom("./images/resources/fog.png", count=75, border=768, xspeed=35, yspeed=0, start=5, fast=True, horizontal=True)

# Declare characters used by this game.
define nar = Character(None, window_top_padding=50)
define w = Character('Wizard Man', color="#c8ffc8")


# The game starts here.
label start:
    scene bg test
    show Fogpart
    play music "./sound/music/moment.ogg"
    "Darkness."
    show wizard normal at Position(xpos=0.1,xanchor=0.1,ypos=0.5,yanchor=0.5)
    play sound "./sound/sfx/switch.wav"
    w "*Flicks the light switch on and off* Welcome to Hell! Welcome to Hell!"

    w "I do love a fine meme."
    stop music

    return

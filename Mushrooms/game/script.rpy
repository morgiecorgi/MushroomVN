# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg test = "./images/backgrounds/test.png"
image wizard normal = "./images/chars/wizard.png"
# Declare characters used by this game.
define w = Character('Wizard Man', color="#c8ffc8")


# The game starts here.
label start:
    scene bg test
    show wizard normal at Position(xpos=0.1,xanchor=0.1,ypos=0.6,yanchor=0.5)
    w "*Flicks the light switch on and off* Welcome to Hell! Welcome to Hell!"

    w "I do love a fine meme."

    return

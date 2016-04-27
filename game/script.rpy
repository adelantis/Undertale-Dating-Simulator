#character-images
image papyrus dummy = "character-dummy.png"


#background-images
image background dummy = "background-dummy.png"
image background papyrus-room = "background-papyrus-room.png"


#character-settings
define narration = Character(kind=nvl)
define system = Character('', color="#FFFFFF")
define papyrus = Character('Papyrus', color="#F69E18", what_prefix='{font=Parchment-MF.ttf}{size=50}', what_suffix='{/size}{/font}')

#default-font
init python:
    style.default.font = "DTM-Mono.otf"

#default-text-speed
#config.default_text_cps=20


label start:

    #scene-welcome
    scene background dummy
    narration "Welcome to the Undertale Dating Simulator Demo! \nTest Scenario: Date with Papyrus \nNote: Only dummy graphics were used for testing purposes of the engine. The music is from the original Undertale game."

    #scene: papyrus' house
    play music "audio/music-home.mp3"
    scene background dummy
    show papyrus dummy

    papyrus "So you came back to have a date with me!"
    papyrus "You must be really serious about this..."
    papyrus "I'll have to take you someplace really special..."
    papyrus "A place I like to spend a lot of time!!!"
    papyrus "My house!!!"
    papyrus "If you are done looking, maybe we can go in, and do whatever people do at dates???"



    #scene: papyrus' room
    scene background papyrus-room
    with fade
    #show papyrus dummy

    papyrus "The internet! I am a dozen followers again, from a double digits follower count!"

    #just an optional fade
    #scene background papyrus-room
    #with fade
    show papyrus dummy

    papyrus "These are all the bone attacks I used on you! Feels just like yersterday, even thought it basically just happened."
    papyrus "So, are you ready to start the date?"

    menu:
        "Yes":
            jump date
        "No":
            jump nodate

    label date:
        #scene: dating start
        scene background dummy
        with fade
        show papyrus dummy
        play music "audio/music-dating-start.mp3"

        papyrus "So, here we are, on our date."
        papyrus "I have never actually done this before. But you can’t spell prepared without several letters from my name. I actually brought a date rule book from the library. We are ready to have a great time!"
        papyrus "Let’s see, press C, for dating hud"

        hide papyrus dummy

        system "Demo ends here, thanks for testing."
        system "Stay determined..."
    return

    label nodate:
        papyrus "Ok! I will be right here if you need me!"

        hide papyrus dummy

        system "Demo ends here, thanks for testing."
        system "Stay determined..."
    return

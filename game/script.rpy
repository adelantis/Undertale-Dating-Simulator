#character-images
image papyrus dummy = "character-dummy.png"


#background-images
image background dummy = "background-dummy.png"
image background papyrus-room = "background-papyrus-room.png"


#character-settings
define narration = Character(kind=nvl)
define system = Character('', color="#FFFFFF")
define papyrus = Character('Papyrus', color="#F69E18")

#default-font
init python:
    style.default.font = "8bitOperatorPlus-Bold.ttf"

#default-text-speed
#config.default_text_cps=20


label start:

    #scene-welcome
    scene background dummy
    narration "{cps=20}Welcome to the Undertale Dating Simulator Demo! \nTest Scenario: Date with Papyrus \nNote: Only dummy graphics were used for testing purposes of the engine. The music is from the original Undertale game.{/cps}"
    
    #scene: papyrus' house
    play music "audio/music-home.mp3"
    scene background dummy
    show papyrus dummy
    
    papyrus "{font=papyrus.ttf}{cps=20}So you came back to have a date with me!{/cps}{/font}"
    papyrus "{font=papyrus.ttf}{cps=20}You must be really serious about this...{/cps}{/font}"
    papyrus "{font=papyrus.ttf}{cps=20}I'll have to take you someplace really special...{/cps}{/font}"
    papyrus "{font=papyrus.ttf}{cps=20}A place I like to spend a lot of time!!!{/cps}{/font}"
    papyrus "{font=papyrus.ttf}{cps=20}My house!!!{/cps}{/font}"
    papyrus "{font=papyrus.ttf}{cps=20}If you are done looking, maybe we can go in, and do whatever people do at dates???{/cps}{/font}"
    
    
    
    #scene: papyrus' room
    scene background papyrus-room
    with fade
    #show papyrus dummy
    
    papyrus "{font=papyrus.ttf}{cps=20}The internet! I am a dozen followers again, from a double digits follower count!{/cps}{/font}"
    
    #just an optional fade
    #scene background papyrus-room
    #with fade
    show papyrus dummy
    
    papyrus "{font=papyrus.ttf}{cps=20}These are all the bone attacks I used on you! Feels just like yersterday, even thought it basically just happened.{/cps}{/font}"
    papyrus "{font=papyrus.ttf}{cps=20}So, are you ready to start the date?{/cps}{/font}"
    
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
    
        papyrus "{font=papyrus.ttf}{cps=20}So, here we are, on our date.{/cps}{/font}"
        papyrus "{font=papyrus.ttf}{cps=20}I have never actually done this before. But you can’t spell prepared without several letters from my name. I actually brought a date rule book from the library. We are ready to have a great time!{/cps}{/font}"
        papyrus "{font=papyrus.ttf}{cps=20}Let’s see, press C, for dating hud{/cps}{/font}"
        
        hide papyrus dummy
        
        system "{cps=20}Demo ends here, thanks for testing.{/cps}}"
        system "{cps=20}Stay determined...{/cps}"
    return
    
    label nodate:
        papyrus "{font=papyrus.ttf}{cps=20}Ok! I will be right here if you need me!{/cps}{/font}"
        
        hide papyrus dummy
        
        system "{cps=20}Demo ends here, thanks for testing.{/cps}"
        system "{cps=20}Stay determined...{/cps}"
    return

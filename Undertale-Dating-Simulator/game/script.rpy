#Characters
image papyrus shape = "papyrus.png"

#Background
image bg forrest = "background.jpg"

# Character
define narration = Character(kind=nvl)
define system = Character('', color="#FFFFFF") #system, "invisible", white
define papyrus = Character('Papyrus', color="#F69E18") #papyrus, papyrus, orange

label start:

    #scene: welcome
    scene bg forrest
    narration "{cps=20}Welcome to the Undertale Dating Simulator Demo! \nTest Scenario: Date with Papyrus \nNote: Only dummy graphics were used for testing purposes of the engine. The music is from the original Undertale game.{/cps}"

    #scene: papyrus' house
    play music "home.mp3"
    scene bg forrest
    show papyrus shape

    papyrus "{cps=20}If you are done looking, maybe we can go in, and do whatever people do at dates?{/cps}"
    
    #scene: papyrus' room
    scene bg forrest
    with fade
    show papyrus shape
    
    papyrus "{cps=20}The internet! I am a dozen followers again, from a double digits follower count!{/cps}"
    
    #just an optional fade
    scene bg forrest
    with fade
    show papyrus shape
    
    papyrus "{cps=20}These are all the bone attacks I used on you! Feels just like yersterday, even thought it basically just happened.{/cps}"
    papyrus "{cps=20}So, are you ready to start the date?{/cps}"
    
    menu:
        "Yes":
            jump date
        "No":
            jump nodate
    
    label date:
        #scene: dating start
        scene bg forrest
        with fade
        show papyrus shape
        play music "dating start.mp3"
    
        papyrus "{cps=20}So, here we are, on our date.{/cps}"
        papyrus "{cps=20}I have never actually done this before. But you can’t spell prepared without several letters from my name. I actually brought a date rule book from the library. We are ready to have a great time!{/cps}"
        papyrus "{cps=20}Let’s see, press C, for dating hud{/cps}"
        
        hide papyrus shape
        
        system "{cps=20}Demo ends here, thanks for testing.{/cps}"
        system "{cps=20}Stay determined...{/cps}"
    return
    
    label nodate:
        papyrus "{cps=20}Ok! I will be right here if you need me!{/cps}"
        
        hide papyrus shape
        
        system "{cps=20}Demo ends here, thanks for testing.{/cps}"
        system "{cps=20}Stay determined...{/cps}"
    return

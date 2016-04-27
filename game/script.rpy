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

    #scene: Snowdin
    $ papyrus_love = 0
    play music "audio/music-home.mp3"
    scene background dummy
    show papyrus dummy

    papyrus "Oh, alright, Human! You have charmed I, the Great Papyrus, enough to get what you wish. A date!"
    papyrus "Well, where would you like to go?"
    menu:
        "Waterfall (Not included in Demo)":
            jump notincluded
        "Your Room":
            "Papyrus leads you to his house."
            play music "dating start.mp3"
            papyrus "Well, this is it! If you are ready, maybe we can go in and do whatever people do at dates?"
            #Sprite change: nervous smile
            jump papyrus-room
        "Snowdin (Not included in Demo)":
            jump notincluded

    label papyrusroom:
        #scene: papyrus's room
        scene background papyrus-room
        with fade
        #show papyrus dummy

        #This is a choice for now, but the writers want it to be point and click
        menu:
            "Check Computer":
                papyrus "The Internet! I'm quite popular there! I am a dozen away from a double-digit follower count!"
                jump ready-to-start
            "Check Closet":
                papyrus "What? It's not like I have skeletons hanging in my closet!"
                jump readytostart

        label readytostart:
            papyrus "So, are you ready to start the date?"
            menu:
                "Yes":
                    papyrus "Great!"
                    jump startdate
                "No":
                    papyrus "Okay! Just let me know when you are ready, Human!"
                    jump papyrusroom

            label startdate:
                "Dating... Start!"
                papyrus "So, here we are, on our date."
                papyrus "Actually, I have never done this before"
                #Sprite change: nervous glance
                papyrus "But, you can't spell prepared without several letters from my name."
                #Sprite change: reassuring smile/thumbs up
                papyrus "I actually brought a date rulebook from the library. We are ready to have a great time!"
                #Sprite change:
                papyrus "Let's see, press C for the dating HUD."
                #Dating menu appears
                papyrus "I feel so informed!"
                papyrus "Ahem! Human! I, The Great Papyrus, will go on a date with you!"
                menu:
                    "Okay!"
                        $ papyrus_love += 1
                        papyrus "WOWIE!"
                        #Sprite change: big smile
                        papyrus "That means we are ready for phase two!"
                        jump continuedate
                    "Uh..."
                        #papyrus_love does not change
                        papyrus "Oh, don't get all shy now! Nyeh. Don't worry, I'll use the book to make sure this date is splendid, no matter what lack of dating experience you have!"
                        #Sprite change: thumbs up
                        jump continuedate
                label continuedate:
                    papyrus "Let's see. Phase two. Put on nice clothes to show you care."
                    #Player equipment menu appears
                    #Include tutorial on how to equip clothing to make the player more appealing to cetain monsters
                    papyrus "Wait a minute..."
                    stop music
                    papyrus "That (insert clothing)... You are also wearing clothing right now! In fact! Earlier today, we were also wearing clothing!"
                    papyrus "Oh no! Could it be? You have wanted to date me from the very beginning?!"
                    papyrus "You are way better at dating than I am! Your dating power.....!"
                    $ papyrus_love += 1
                    play music "dating start.mp3"
                    papyrus "Nyeh! Don't think you bested me yet! But I won't be beaten at dating!"
                    jump question1

                    label question1:
                    papyrus "Okay!! In the manual, it says to get to know your partner. So, I, THE GREAT PAPYRUS shall ask you an easy question."
                    papyrus "What's your favorite dish?"
                    menu:
                        "Spaghetti"
                            $ papyrus_love += 3
                            $ spaghetti = True
                            $ pizza = False
                            $ broccoli = False
                            papyrus "Wowie!"
                            #Sprite Change: big smile
                            papyrus "That happens to be my favorite as well!"
                            jump question2
                        "Pizza"
                            $ papyrus_love += 1
                            $ pizza = True
                            $ spaghetti = False
                            $ broccoli = False
                            papyrus "You're just like my brother... always after that disgustingly greasy food."
                            #Sprite Change: disgusted face
                            jump question2
                        "Broccoli"
                            #papyrus_love does not change
                            $ broccoli = False
                            $ spaghetti = False
                            $ pizza = False
                            papyrus "Broccoli, eh? At least you're trying to eat healthy, unline my brother Sans..."
                            #Sprite Change: shift eyes
                            jump question2
                    label question2:
                        if spaghetti == True:
                            #Sprite Change: big smile
                            papyrus "Impressive! But how do you feel about..."
                            #Sprite Change: squints
                            papyrus "... puns?"
                            menu:
                                "Aren't they punderful?"
                                    $ papyrus_love -= 2
                                    $ punderful = True
                                    $ nopuns = False
                                    #Sprite Change: wide eyes/shock
                                    papyrus "You're pulling my leg, right?"
                                    jump question3
                                "No... just, no."
                                    $ papyrus_love += 3
                                    $ punderful = False
                                    $ nopuns = True
                                    papyrus "Wowie! Something else we can agree on! Nyeh heh heh!"
                                    jump question3
                        elif pizza == True:
                            papyrus "Well, THE GREAT PAPYRUS is merciful, so I'll give you another opportunity. How do you feel about..."
                            #Sprite Change: squints
                            papyrus "... puns?"
                            menu:
                                "Aren't they punderful?"
                                    $ papyrus_love -= 2
                                    $ punderful = True
                                    $ nopuns = False
                                    papyrus "MOVING ON..."
                                    #Sprite Change: annoyed
                                    jump question3
                                "No... just, no."
                                    $ papyrus_love += 3
                                    $ punderful = False
                                    $ nopuns = True
                                    papyrus "Something we can agree on!"
                                    jump question3
                        else:
                            #if broccoli is true
                            papyrus "You're not doing so bad! But how do you feel about..."
                            #Sprite Change: squints
                            papyrus "... puns?"
                            menu:
                                "Aren't they punderful?"
                                    $ papyrus_love -= 2
                                    $ punderful = True
                                    $ nopuns = False
                                    papyrus "Uh..."
                                    #Sprite Change: slightly annoyed
                                    papyrus "Gosh... Maybe I can let that slide..."
                                    jump question3
                                "No... just, no."
                                    $ papyrus_love += 3
                                    $ punderful = False
                                    $ nopuns = True
                                    papyrus "We can agree on something, then!"
                                    jump question3
                            label question3:
                                papyrus "Now, what do you think about my brother, Sans?"

                                #code to be continued



    label notincluded:
        hide papyrus dummy

        system "The Demo ends here, thanks for playing!"
        system "Stay determined..."
    return

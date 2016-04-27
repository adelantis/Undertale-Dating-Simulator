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
    style.default.font = "DTM-Mono.otf"

#default-text-speed
#config.default_text_cps=20


label start:

     #scene-welcome
     scene background dummy
     narration "{cps=20}Welcome to the Undertale Dating Simulator Demo! \nTest Scenario: Date with Papyrus \nNote: Only dummy graphics were used for testing purposes of the engine. The music is from the original Undertale game.{/cps}"

     #scene: Snowdin
     $ papyrus_love = 0
     play music "audio/music-home.mp3"
     scene background dummy
     show papyrus dummy

     papyrus "{cps=20}{font=PAPYRUS.ttf}Oh, alright, Human! You have charmed I, the Great Papyrus, enough to get what you wish. A date!{/font}{/cps}"
     papyrus "{cps=20}{font=PAPYRUS.ttf}Well, where would you like to go?{/font}{/cps}"
     menu:
         "Waterfall (Not included in Demo)":
             jump notincluded
         "Your Room":
             "Papyrus leads you to his house."
             play music "dating start.mp3"
             papyrus "{cps=20}{font=PAPYRUS.ttf}Well, this is it! If you are ready, maybe we can go in and do whatever people do at dates?{/font}{/cps}"
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
                papyrus "{cps=20}{font=PAPYRUS.ttf}The Internet! I'm quite popular there! I am a dozen away from a double-digit follower count!{/font}{/cps}"
                jump ready-to-start
             "Check Closet":
                papyrus "{cps=20}{font=PAPYRUS.ttf}What? It's not like I have skeletons hanging in my closet!{/font}{/cps}"
                jump readytostart
        
         label readytostart:
             papyrus "{cps=20}{font=PAPYRUS.ttf}So, are you ready to start the date?{/font}{/cps}"
             menu:
                 "Yes":
                    papyrus "{cps=20}{font=PAPYRUS.ttf}Great!{/font}{/cps}"
                    jump startdate
                 "No":
                    papyrus "{cps=20}{font=PAPYRUS.ttf}Okay! Just let me know when you are ready, Human!{/font}{/cps}"
                    jump papyrusroom
                    
             label startdate:
                 "Dating... Start!"
                 papyrus "{cps=20}{font=PAPYRUS.ttf}So, here we are, on our date.{/font}{/cps}"
                 papyrus "{cps=20}{font=PAPYRUS.ttf}Actually, I have never done this before{/font}{/cps}"
                 #Sprite change: nervous glance
                 papyrus "{cps=20}{font=PAPYRUS.ttf}But, you can't spell prepared without several letters from my name.{/font}{/cps}"
                 #Sprite change: reassuring smile/thumbs up
                 papyrus "{cps=20}{font=PAPYRUS.ttf}I actually brought a date rulebook from the library. We are ready to have a great time!{/font}{/cps}"
                 #Sprite change:
                 papyrus "{cps=20}{font=PAPYRUS.ttf}Let's see, press C for the dating HUD.{/font}{/cps}"
                 #Dating menu appears
                 papyrus "{cps=20}{font=PAPYRUS.ttf}I feel so informed!{/font}{/cps}"
                 papyrus "{cps=20}{font=PAPYRUS.ttf}Ahem! Human! I, The Great Papyrus, will go on a date with you!{/font}{/cps}"
                 menu:
                     "Okay!"
                         $ papyrus_love += 1
                         papyrus "{cps=20}{font=PAPYRUS.ttf}WOWIE!{/font}{/cps}"
                         #Sprite change: big smile
                         papyrus "{cps=20}{font=PAPYRUS.ttf}That means we are ready for phase two!{/font}{/cps}"
                         jump continuedate
                     "Uh..."
                         #papyrus_love does not change
                         papyrus "{cps=20}{font=PAPYRUS.ttf}Oh, don't get all shy now! Nyeh. Don't worry, I'll use the book to make sure this date is splendid, no matter what lack of dating experience you have!{/font}{/cps}"
                         #Sprite change: thumbs up
                         jump continuedate
                 label continuedate:
                     papyrus "{cps=20}{font=PAPYRUS.ttf}Let's see. Phase two. Put on nice clothes to show you care.{/font}{/cps}"
                     #Player equipment menu appears
                     #Include tutorial on how to equip clothing to make the player more appealing to cetain monsters
                     papyrus "{cps=20}{font=PAPYRUS.ttf}Wait a minute...{/font}{/cps}"
                     stop music
                     papyrus "{cps=20}{font=PAPYRUS.ttf}That (insert clothing)... You are also wearing clothing right now! In fact! Earlier today, we were also wearing clothing!{/font}{/cps}"
                     papyrus "{cps=20}{font=PAPYRUS.ttf}Oh no! Could it be? You have wanted to date me from the very beginning?!{/font}{/cps}"
                     papyrus "{cps=20}{font=PAPYRUS.ttf}You are way better at dating than I am! Your dating power.....!{/font}{/cps}"
                     $ papyrus_love += 1
                     play music "dating start.mp3"
                     papyrus "{cps=20}{font=PAPYRUS.ttf}Nyeh! Don't think you bested me yet! But I won't be beaten at dating!{/font}{/cps}"
                     jump question1
                     
                     label question1:
                     papyrus "{cps=20}{font=PAPYRUS.ttf}Okay!! In the manual, it says to get to know your partner. So, I, THE GREAT PAPYRUS shall ask you an easy question.{/font}{/cps}"
                     papyrus "{cps=20}{font=PAPYRUS.ttf}What's your favorite dish?{/font}{/cps}"
                     menu:
                         "Spaghetti"
                             $ papyrus_love += 3
                             $ spaghetti = True
                             $ pizza = False
                             $ broccoli = False
                             papyrus "{cps=20}{font=PAPYRUS.ttf}Wowie!{/font}{/cps}"
                             #Sprite Change: big smile
                             papyrus "{cps=20}{font=PAPYRUS.ttf}That happens to be my favorite as well!{/font}{/cps}"
                             jump question2
                         "Pizza"
                             $ papyrus_love += 1
                             $ pizza = True
                             $ spaghetti = False
                             $ broccoli = False
                             papyrus "{cps=20}{font=PAPYRUS.ttf}You're just like my brother... always after that disgustingly greasy food.{/font}{/cps}"
                             #Sprite Change: disgusted face
                             jump question2
                         "Broccoli"
                             #papyrus_love does not change
                             $ broccoli = False
                             $ spaghetti = False
                             $ pizza = False
                             papyrus "{cps=20}{font=PAPYRUS.ttf}Broccoli, eh? At least you're trying to eat healthy, unline my brother Sans...{/font}{/cps}"
                             #Sprite Change: shift eyes
                             jump question2
                     label question2:
                         if spaghetti == True:
                             #Sprite Change: big smile
                             papyrus "{cps=20}{font=PAPYRUS.ttf}Impressive! But how do you feel about...{/font}{/cps}"
                             #Sprite Change: squints
                             papyrus "{cps=20}{font=PAPYRUS.ttf}{/font}... puns?{/cps}"
                             menu:
                                 "Aren't they punderful?"
                                     $ papyrus_love -= 2
                                     $ punderful = True
                                     $ nopuns = False
                                     #Sprite Change: wide eyes/shock
                                     papyrus "{cps=20}{font=PAPYRUS.ttf}You're pulling my leg, right?{/font}{/cps}"
                                     jump question3
                                 "No... just, no."
                                     $ papyrus_love += 3
                                     $ punderful = False
                                     $ nopuns = True
                                     papyrus "{cps=20}{font=PAPYRUS.ttf}Wowie! Something else we can agree on! Nyeh heh heh!{/font}{/cps}"
                                     jump question3
                         elif pizza == True:
                             papyrus "{cps=20}{font=PAPYRUS.ttf}Well, THE GREAT PAPYRUS is merciful, so I'll give you another opportunity. How do you feel about...{/font}{/cps}"
                             #Sprite Change: squints
                             papyrus "{cps=20}{font=PAPYRUS.ttf}... puns?{/font}{/cps}"
                              menu:
                                 "Aren't they punderful?"
                                     $ papyrus_love -= 2
                                     $ punderful = True
                                     $ nopuns = False
                                     papyrus "{cps=20}{font=PAPYRUS.ttf}MOVING ON...{/font}{/cps}"
                                     #Sprite Change: annoyed
                                     jump question3
                                 "No... just, no."
                                     $ papyrus_love += 3
                                     $ punderful = False
                                     $ nopuns = True
                                     papyrus "{cps=20}{font=PAPYRUS.ttf}Something we can agree on!{/font}{/cps}"
                                     jump question3
                         else:
                             #if broccoli is true
                             papyrus "{cps=20}{font=PAPYRUS.ttf}You're not doing so bad! But how do you feel about...{/font}{/cps}"
                             #Sprite Change: squints
                             papyrus "{cps=20}{font=PAPYRUS.ttf}... puns?{/font}{/cps}"
                              menu:
                                 "Aren't they punderful?"
                                     $ papyrus_love -= 2
                                     $ punderful = True
                                     $ nopuns = False
                                     papyrus "{cps=20}{font=PAPYRUS.ttf}Uh...{/font}{/cps}"
                                     #Sprite Change: slightly annoyed
                                     papyrus "{cps=20}{font=PAPYRUS.ttf}Gosh... Maybe I can let that slide...{/font}{/cps}"
                                     jump question3
                                 "No... just, no."
                                     $ papyrus_love += 3
                                     $ punderful = False
                                     $ nopuns = True
                                     papyrus "{cps=20}{font=PAPYRUS.ttf}We can agree on something, then!{/font}{/cps}"
                                     jump question3
                             label question3:
                                 papyrus "{cps=20}{font=PAPYRUS.ttf}Now, what do you think about my brother, Sans?{/font}{/cps}"
                                 
                                 #code to be continued
        
    
    
    label notincluded:
        hide papyrus dummy
        
        system "{cps=20}The Demo ends here, thanks for playing!{/cps}"
        system "{cps=20}Stay determined...{/cps}"
    return

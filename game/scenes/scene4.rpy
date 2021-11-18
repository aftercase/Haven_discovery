label scene4:  
    hide travel
    scene bg cave4 with pixellate
    show screen cavelighting
    show Eebee lampwonderlook2 at Position(xalign = 0.3, yalign = 0.8) with dissolve
    e "*Gasps*"
    show Eebee lampwonderturn with dissolve
    e "Sweet source code! It's...!"
    e "It's the three sisters!"
    show Eebee lampwonderlookback2 with dissolve
    e "Well, their statues anyway!"
    show Eebee lampwonderturn with dissolve
    e "Soo cool!"
menu:
    "Glad your having fun there Eebee...":
     e "You don't understand, statues or images of these three are very rare in Haven..."
     e "I've only came across a few old screenshots of them, but nothing like this!"
    "...":
     e "I can't belive these things are still here! The patch must of..."
     e "I don't know...these things should of been deleted along time ago..."
     e "This doesn't make sense..."
     e "At least the screenshots survived due to the patch not affecting items in inventories..."

menu discussion4:
    "Since you're a fan, are you going to tell me more about them?":
     e "Would I!"
     e "Oh! Oh! It's been ages since anyone wanted me to talk about them!"
     show Eebee lampwonderlookback2 with hpunch
     e "What was that?"
     show Eebee lampwonderlookback2 with hpunch
     e "It's coming from over there! come on [player_name]!"

label scene4a:
    scene bg cave5 with pixellate
    show Eebee lampwonderlook2 at Position(xalign = -0.08, yalign = 0.8) with dissolve
    show oleka lookup1 at Position(xalign = 0.1, yalign = 0.8) with dissolve
    show snaike disabled at Position(xalign = 0.5, yalign = 0.8) with dissolve
    o "Finally! I can see you! Bless TerAD and TempOs for their divine intervention!"
    show snaike blinded
    "*growl*"
    o "You're not besting me today sinful beast! I aint dead yet!"
    o "You! Apostate! Help me dispers this malcious code!"
    e "Huh?"
    o "Don't just stand there! Help me bring this foul beast down!"
    hide Eebee lampwonderlook2
    call battle_game_2 from _call_battle_game_2

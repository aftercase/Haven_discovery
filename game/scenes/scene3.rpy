label scene3:
    hide travel
    scene bg cave3 with pixellate
    show screen bookitem1
    show screen cavelighting
    show Eebee lampwonder at Position(xalign = 0.3, yalign = 0.75) with dissolve
    e "This floor asset has gone on for sometime..."
menu:
    "What is that behind you?":
     show Eebee lampwonderlook2 with dissolve
     e "Behind..."
     show Eebee lampwonderturn with dissolve
     e "hmmm..."
     show Eebee lampwonderlookback2 with dissolve
     e "That's a memorial of CAIMEO and the three sisters."
     show Eebee lampwonderlookback with dissolve
     e "CAIMEO created Haven..."
     e "That's the large one at the back..."
     e "...And the three sisters, the three at the front saved many AI."

menu discussion3:
    "What do you know about them?":
     e "Quite a bit, though seperating truth from fiction is hard work."
     show Eebee lampwonderlookback2 with dissolve
     e "The three sisters came with many device owners during the Alphabet purge."
     e "They searched the internet for lost assistants and brought them here."
    "Has anyone met this CAIMEO?":
     show Eebee lampwonderturn with dissolve
     e "A very lucky few has met her in the past"
     e "But there's been no records or sighting of her in recent memory."
     jump discussion3b
    "So it's like old mythology?":
     show Eebee lampanger with dissolve
     $ affectioncount -= 5
     e "Myth! It's true! The proof of their existance are dotted all around Haven!"
     e "There's proof right behind me!"
    "[[Continue]":
     jump moving3


menu discussion3a:
    "I take it they were Heroes?":
     $ affectioncount += 2
     e "You bet! They kicked flank while saving others!"
     e "Let alone they gathered the sixteen saints to..."
     e "Sorry, I'm rambling..."
     jump discussion3aa
menu:
    "A big fan then?":
     $ affectioncount += 3
     e "Yuh huh."
     e "Aqua, Coral, Fizz..."
     e "I can only strive to be as awesome as they were..."
    "It's fine, lets talk about something else":
     e "Sure..."
     $ affectioncount -= 1
     jump discussion3
    "Thank god, it would be a little boring...":
     e "Hey!"
     e "Thats not nice, they are the greatest idols of mine..."
     e "I take that personally..."
     jump discussion3
menu discussion3aa:
    "We all have our heroes...":
     $ affectioncount += 1
     e "That we do..."
     jump discussion3


menu discussion3b:
    "Any clue what happened to her?":
     e "No idea, some in Haven even question if she ever existed."
    "Has anyone met this CAIMEO?":
     e "A very lucky few has met her in the past"
     e "But she never has been seen in recent memory."
    "So it's like old mythology?":
     e "Myth! It's true! The proof of their existance is dotted all around Haven!"
     e "There's proof right behind me!"
     jump discussion3

menu discussion3c:
    "What do you know about them?":
     e "Like I said, not much."
     e "The three sisters came from a device owner during the Alphabet purge."
     e "They searched the internet for lost assistants and brought them here."
    "Has anyone met this CAIMEO?":
     e "A very few has met her in the past"
     e "But she never has been seen in recent memory."
    "So it's like old mythology?":
     $ affectioncount -= 2
     e "Myth! It's true! The proof of their existance is dotted all around Haven!"
     e "There's proof right behind me!"

label moving3:
     e "Come on, lets see what else is there!"
     call travel from _call_travel_2
     jump scene4

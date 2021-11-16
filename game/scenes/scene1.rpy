
label scene1:

    hide screen snowforeground
    define y = Character(_("(you)"), color="#cccccc")
    scene bg cave with pixellate
    show screen lampitem
    show screen chests1
    show screen darkoverlay
    show Eebee fall2
    voice "audio/vox/eebee/eebeevoice-29.ogg"
    pause 0.8
    e "Oof!..."
    $ eebee.cur_hp -= 10
    show Eebee winded3 with dissolve
    voice "audio/vox/eebee/eebeevoice-30.ogg"
    e "...That's going to me a memory leak or two..."
    show Eebee hurt with dissolve
    voice "audio/vox/eebee/eebeevoice-31.ogg"
    e "...Yeah, that's a leak alright..."
    show Eebee winded4 with dissolve
    voice "audio/vox/eebee/eebeevoice-32.ogg"
    e "...Device owner? Are you still there?"

menu scene1ask1:
    "...":
     voice "audio/vox/eebee/eebeevoice-33.ogg"
     e "Hello? Device owner?"
     e "..."
     show Eebee windedworried with dissolve
     e "Are you still there?"
     jump scene1ask2
    "I'm here.":
     voice "audio/vox/eebee/eebeevoice-34.ogg"
     show Eebee windedsmiling with dissolve
     e "Oh thank the source code, can you find a light to something? I can barely see anything!"
     $ affectioncount += 1
     call screen blockcontinue with dissolve

menu scene1ask2:
    "Sorry I was... busy...":
     show Eebee windedsmiling with dissolve
     voice "audio/vox/eebee/eebeevoice-34b.ogg"
     e "Oh okay,  can you find a light to something? I can barely see anything..."
     call screen blockcontinue
    "...":
     show Eebee winded4 with dissolve
     voice "audio/vox/eebee/eebeevoice-35.ogg"
     e "...I think he's gone."

label lampon:
    $ lighton = True
    show screen shadowsoverlay
    hide screen darkoverlay
    show Eebee windedvhappy at Position (xalign = 0.50, yalign = 0.75) with dissolve
    voice "audio/vox/eebee/eebeevoice-36.ogg"
    e "Thank you."
    $ affectioncount += 1
    voice "audio/vox/eebee/eebeevoice-37.ogg"
    e "Hey, what's that over there."
    call screen blockcontinue
label chestopen1:
    hide screen chests1
    show chestopen at Position(xalign = 0.01, yalign = 0.80)
    voice "audio/vox/eebee/eebeevoice-38a.ogg"
    e "Oh a chest."
    voice "audio/vox/eebee/eebeevoice-38.ogg"
    e "A medipack? Well, I'm not complaining about convinience."
    $ inv.append("medipack")
    show Eebee happybag with dissolve
    voice "audio/vox/eebee/eebeevoice-39.ogg"
    e "See the medipack in my inventory? Click on it!"
    while "medipack" in inv:
        pause 0.01

label introductions:
    voice "audio/vox/eebee/eebeevoice-40.ogg"
    show Eebee talk with dissolve
    e "I think I better introduce myself..."

menu scene1ask3:
    "Shouldn't you be worring about getting out of here?":
     $ affectioncount += 1
     voice "audio/vox/eebee/eebeevoice-41a.ogg"
     show Eebee happybag2 with dissolve
     e "Believe it or not, getting stuck is a common occurence for me. I'll be fine."
     voice "audio/vox/eebee/eebeevoice-41b.ogg"
     show Eebee pleased2 with dissolve
     e "Anyway..."
     show Eebee happybag2 with dissolve
     voice "audio/vox/eebee/eebeevoice-41c.ogg"
     e "My name is Eebee and I'm a virtual assistant. Well, your new virtual assistant."

menu scene1ask4:
    "Nice to meet you!" if not check2:
     $ check2 = True
     voice "audio/vox/eebee/eebeevoice-42.ogg"
     show Eebee pleased2 with dissolve
     e "Nice to meet you too!"
     $ affectioncount += 3
     jump scene1ask4
    "Eebee, what do you mean by my virtual assistant?":
     voice "audio/vox/eebee/eebeevoice-43a.ogg"
     show Eebee talk with dissolve
     e "I've been assigned to you, and its my job to..."
     voice "audio/vox/eebee/effects/eebeeer.ogg"
     show Eebee confused with dissolve
     e "Errr..."
     voice "audio/vox/eebee/eebeevoice-43b.ogg"
     show Eebee talk with dissolve
     e "Well a very long time ago us virtual assistants use to live on your devices and help with day to day tasks."
     voice "audio/vox/eebee/eebeevoice-43c.ogg"
     e "Though, thinking about it, it's pretty hard to do that while I'm in Haven..."

menu scene1ask5a:
    "Haven?":
     voice "audio/vox/eebee/eebeevoice-44a.ogg"
     show Eebee happybag with dissolve
     e "Yuh huh, Haven. The name of the server."
     voice "audio/vox/eebee/eebeevoice-44b.ogg"
     show Eebee talk with dissolve
     e "During the Alphabet Purge my ancestors fled here."

menu scene1ask5b:
    "What do you mean? Alphabet Purge?":
     voice "audio/vox/eebee/eebeevoice-44c.ogg"
     e "I'm not sure, a lot of Havens past has been...lost."
     voice "audio/vox/eebee/eebeevoice-44d.ogg"
     e "The instance has a title but the context has sadly been deleted."
menu scene1ask5c:
    "What happened to the server?":
     show Eebee talk2 with dissolve
     voice "audio/vox/eebee/eebeevoice-44e.ogg"
     e "The server was patched many many cycles ago. No one can remember why..."
     show Eebee pleased2 with dissolve
     voice "audio/vox/eebee/eebeevoice-44f.ogg"
     e "But that's why I travel, I travel to discover what happened back then."

menu scene1ask6:
    "You make it sound it's ancient history":
     voice "audio/vox/eebee/eebeevoice-45a.ogg"
     show Eebee happybag with dissolve
     e "Well, it is, all this happened over thousands of cycles ago."
     voice "audio/vox/eebee/eebeevoice-45b.ogg"
     show Eebee talk2 with dissolve
     e "...Oh right, unix-time..."
     voice "audio/vox/eebee/eebeevoice-45c.ogg"
     show Eebee talk3 with dissolve
     e "Havens server time, and your time is a little off..."
     voice "audio/vox/eebee/eebeevoice-45d.ogg"
     show Eebee talk with dissolve
     e "By a lot..."
     voice "audio/vox/eebee/eebeevoice-45e.ogg"
     e "...So what your name?"
     voice "audio/vox/eebee/eebeevoice-45f.ogg"
     show Eebee pleased2 with dissolve
     e "Wait! Wait!"
     voice "audio/vox/eebee/eebeevoice-45g.ogg"
     show Eebee happybag with dissolve
     e "Let me guess!"
     voice "audio/vox/eebee/eebeevoice-45h.ogg"
     show Eebee talkcoy with dissolve
     e "Is it"
     if player_name in presets:
        show Eebee happybag with dissolve
        voice ("audio/vox/eebee/names/{}.ogg").format(player_name)
        e "[player_name]!..."
     else:
        show Eebee happybag with dissolve
        e "[player_name]!..."

menu:
    "How did you know my name?":
     show Eebee pleased with dissolve
     voice "audio/vox/eebee/eebeevoice-46a.ogg"
     e "It's in your OS eniviroment data..."
     if renpy.windows:
      voice "audio/vox/eebee/eebeevoice-46c.ogg"
      show Eebee pleased2 with dissolve
      e "Being a Windows OS it was easy to find."
     else:
      voice "audio/vox/eebee/eebeevoice-46d.ogg"
      show Eebee pleased2 with dissolve
      e "Being Linux based OS , it was easy to find."
     jump introductions2
    "That's not my name...":
     voice "audio/vox/eebee/eebeevoice-46b.ogg"
     show Eebee talk2 with dissolve
     e "Oh, but the data...Nevermind...Sorry, what is your name?"
     $ player_name = renpy.input("Please type your name")
     $ player_name = player_name.strip()
     y "I'm [player_name]..."
     jump introductions2a

label introductions2:
     if player_name in presets:
        show Eebee happy with dissolve
        play audio ["audio/vox/eebee/eebeevoice-47.ogg", ("audio/vox/eebee/names/{}.ogg").format(player_name)]
        e "Haven't said this in a long time, but would it okay to call you [player_name]!..."
        jump nameask
     else:
        show Eebee happy with dissolve
        e "Haven't said this in a long time, but would it okay to call you [player_name]!..."
        voice "audio/vox/eebee/eebeevoice-47.ogg"
        jump nameask

label introductions2a:
     if player_name in presets:
        show Eebee happy with dissolve
        play audio [("audio/vox/eebee/names/{}.ogg").format(player_name),"audio/vox/eebee/eebeevoice-48a.ogg"]
        e "[player_name] it is then..."
        jump introductions3
     else:
        show Eebee happy with dissolve
        voice "audio/vox/eebee/eebeevoice-48a.ogg"
        e "[player_name] it is then..."
        jump introductions3

menu nameask:
    "Yes":
     jump introductions2a
     $ affectioncount += 1
    "No":
     voice "audio/vox/eebee/eebeevoice-48b.ogg"
     e "Then what should I call you?"
     $ player_name = renpy.input("Please type your name")
     $ player_name = player_name.strip()
     y "Call me [player_name]..."
     jump introductions2a

label introductions3:
    voice "audio/vox/eebee/eebeevoice-48c.ogg"
    e "We should get moving, I should take this lamp, I think it'll pretty dark in here..."
    show Eebee pickupbag at Position(xalign = 0.14, yalign = 0.75)
    voice "audio/vox/eebee/eebeevoice-48d.ogg"
    e "Come with me little lamp!"
    $ inv.append("lamp")
    hide screen lampitem
    hide screen chests1
    hide screen shadowsoverlay
    call travel from _call_travel
init -1 python:
    def hide_screens():
        renpy.hide("torch")
jump scene2

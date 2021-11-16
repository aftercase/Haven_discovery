define config.developer = "True"
define config.layers = ['underlay', 'master', 'transient','itemmap', 'screen1', 'snow1','screens', 'torch', 'ui', 'overlay']
define res = 0

# The game starts here.

label start:
    python:
        with open( os.path.join( renpy.config.gamedir, "testfile.txt"), 'w') as f:
            f.write( '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&((((##(((#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@(%&/@(((((((((((((#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@***/@((((((((((((((((#&**@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@/(***%(((((((((((((((((((#*@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@*@***/((((((((((((((((((((#&@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@*@***%(((((((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@****/(((((((((((((((((((((@@&@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@%***/@(((((((((((((((((%####@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#&@#*.,%*/#@@@&%/**&,,@&#####@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#@/%#  (%(***..,*&,  @%(&@@##@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#@%#  &%@&**,...(.  @@@%.&@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*&@@@@@&**....(@@@@@@#,@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@##@.&@@@@******.*(@@@@#.&@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#&%&#   *****.,#(**  ,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#%#%##@/***(#%%&.***@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@####%##@***%@@@@@#**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@########&#####%************@@(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@&####%###%###**************@(%(@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@(&#####%###/**************@(((/@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@%%##%&#####***************@(## @@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@/(#((###@***************/@(((( @@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@#&((((((@**************/%((#(@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@(%(((((#%*****/&%@******@((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@&@@@@@%((#&@******(#/@******%(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@####@@@@@////@******(#/@*******@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@########@////%/******%@/@*******@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@######@////@*******%@/@*******/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@#///(%*******%@/@********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@////@********&@/@********#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@////@********&@/@*********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@///@*********@//@*********&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@&//@*********@//@*********/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@/*********@@&@**********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/******#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
label start2:
    #introduction#
    "This is a demo"
    "A lot of things are missing from this version"
    "Not to mention filled with bugs, typo's and other misdeeds."
    "This demo is to showcase my progress and to gather feedback from playtesters."

menu:
    "Preview battle system":
        call battle_2
        # call battle_3
    "Preview VN":
        jump start3

label start3:
    stop music
    show text "Welcome to Haven"
    with Pause(2.0)
    show text "User:|"
    with Pause(1.0)
    show text "User: s|"
    with Pause(0.2)
    show text "User: su|"
    with Pause(0.2)
    show text "User: sub|"
    with Pause(0.2)
    show text "User: subj|"
    with Pause(0.2)
    show text "User: subje|"
    with Pause(0.2)
    show text "User: subjec|"
    with Pause(0.2)
    show text "User: subject|"
    with Pause(0.2)
    show text "User: subject2|"
    with Pause(0.2)
    show text "User: subject21|"
    with Pause(0.2)
    show text "User: subject216|"
    with Pause(2.0)
    show text "Password: |"
    with Pause(0.2)
    show text "Password: *|"
    with Pause(0.2)
    show text "Password: **|"
    with Pause(0.2)
    show text "Password: ***|"
    with Pause(0.2)
    show text "Password: ****|"
    with Pause(0.2)
    show text "Password: *****|"
    with Pause(0.2)
    show text "Password: ******|"
    with Pause(0.2)
    show text "Password: *******|"
    with Pause(0.2)
    show text "Password: ********|"
    with Pause(1.0)
    show text "Loading"
    with Pause(3.0)
    play music "audio/music/Havenintro.ogg"
    show text "Please Wait -"
    with Pause(0.2)
    show text "Please Wait \\"
    with Pause(0.2)
    show text "Please Wait |"
    with Pause(0.2)
    show text "Please Wait /"
    with Pause(0.2)
    show text "Please Wait -"
    with Pause(0.2)
    show text "Please Wait \\"
    with Pause(0.2)
    show text "Please Wait |"
    with Pause(0.2)
    show text "Please Wait /"
    with Pause(0.2)
    show text "Please Wait \\"
    with Pause(0.2)
    show text "Please Wait -"
    with Pause(0.2)
    show text "Please Wait \\"
    with Pause(0.2)
    show text "Please Wait |"
    with Pause(0.2)
    show text "Please Wait /"
    with Pause(0.2)
    show text "Please Wait -"
    with Pause(0.2)
    show text "Please Wait \\"
    with Pause(0.2)
    show text "Please Wait |"
    with Pause(0.2)
    show text "Please Wait /"
    with Pause(0.2)
    show text "Please Wait \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching -"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching -"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching -"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching -"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching -"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching -"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Searching -"
    with Pause(0.2)
    show text "Searching \\"
    with Pause(0.2)
    show text "Searching |"
    with Pause(0.2)
    show text "Searching /"
    with Pause(0.2)
    show text "Assistant Found"
    stop music fadeout 3.0
    with Pause(3.2)

    play music "audio/music/campsite.ogg" fadein 3.0
    scene bg scene1
    show screen player_ui(_layer="ui")
    show screen shotgunitem(_layer="itemmap")
    show screen bagitem(_layer="itemmap")
    show screen snowforeground
    show snow
    show glitch dream at Position(xalign=0.50, yalign=0.2)
    show Eebee tether
    e "..."
    show Eebee neutraltether with dissolve
    play voice "audio/vox/eebee/eebeevoice-00.ogg"
    e "For the love of CAIMEO..."
    show Eebee looktether with dissolve
    play voice "audio/vox/eebee/eebeevoice-01.ogg"
    e "At least my stuff is down the bottom..."

menu:
    "...":
        show Eebee wondertether with dissolve
        voice "audio/vox/eebee/eebeevoice-02.ogg"
        e "huh?..."
        show Eebee wavether with dissolve
        voice "audio/vox/eebee/eebeevoice-03.ogg"
        e "Hey! Device owner!"
        voice "audio/vox/eebee/eebeevoice-04.ogg"
        e "Over here!"
        voice "audio/vox/eebee/eebeevoice-05.ogg"
        e "Give me second, I'll get down..."
        show Eebee looktether with dissolve
        voice "audio/vox/eebee/eebeevoice-06.ogg"
        e "Come on you stupid tether!"
        show Eebee fall

    "Hello?":
        show Eebee wondertether with dissolve
        voice "audio/vox/eebee/eebeevoice-07.ogg"
        e "huh?..."
        show Eebee wavether with dissolve
        voice "audio/vox/eebee/eebeevoice-08.ogg"
        e "Hello!"
        voice "audio/vox/eebee/eebeevoice-09.ogg"
        e "Give a me second, I'll get down..."
        show Eebee looktether with dissolve
        voice "audio/vox/eebee/eebeevoice-10.ogg"
        e "Or try to..."
        show Eebee wondertether with dissolve
        voice "audio/vox/eebee/eebeevoice-11.ogg"
        e "Unless maybe I could delete the..."
        show Eebee fall

label begin:
    voice "audio/vox/eebee/eebeevoice-12.ogg"
    $ eebee.cur_hp -= 10
    e "Ow!"
    show Eebee snowed at Position(xalign=0.25, yalign=0.8) with dissolve
    voice "audio/vox/eebee/eebeevoice-13.ogg"
    e "I'm okay, deleting it...Was a stupid idea..."
    show Eebee dazed at Position(xalign=0.25, yalign=0.7) with dissolve
    voice "audio/vox/eebee/eebeevoice-14.ogg"
    e "...ugh"
    show Eebee shakehead
    e "..."
    show Eebee huh at Position(xalign=0.25, yalign=0.7) with dissolve
    voice "audio/vox/eebee/eebeevoice-15.ogg"
    e "What are you doing all the way out here?"
    show Eebee huh2 at Position(xalign=0.25, yalign=0.7) with dissolve
    voice "audio/vox/eebee/eebeevoice-16.ogg"
    e "Or being in Haven for that matter..."
menu:
    "I have no idea, this program just logged me in and found you.":
        voice "audio/vox/eebee/eebeevoice-17.ogg"
        e "...Found me?"
        show Eebee happy at Position(xalign=0.25, yalign=0.7) with dissolve
        voice "audio/vox/eebee/eebeevoice-18.ogg"
        e "That must mean you are my new device owner!"
        show Eebee happy2 at Position(xalign=0.25, yalign=0.7) with dissolve
        voice "audio/vox/eebee/eebeevoice-19.ogg"
        e "Oh! this is so exciting! You're the first one to connect in years!"
        show Eebee happy at Position(xalign=0.25, yalign=0.7) with dissolve
        voice "audio/vox/eebee/eebeevoice-20.ogg"
        e "Let me connect to your application..."
        show Eebee pleased with dissolve
        voice "audio/vox/eebee/eebeevoice-21.ogg"
        e "There."

#Pick up tutorial section##
label tutorial:
    if "shotgun" in inv:
        show Eebee happy2 at Position(xalign=0.5, yalign=0.8) with dissolve
        voice "audio/vox/eebee/eebeevoice-22.ogg"
        e "I think that is everything!"
        jump leavetutorial
    elif bagfound:
        voice "audio/vox/eebee/eebeevoice-23.ogg"
        e "Now my shotgun!"
        call screen blockcontinue
    else:
        show Eebee huh2 at Position(xalign=0.25, yalign=0.7) with dissolve
        voice "audio/vox/eebee/eebeevoice-24.ogg"
        e "Hmm...I still need my bags to connect you to my inventory..."
        $ bagactive = True
        show Eebee happy at Position(xalign=0.25, yalign=0.7) with dissolve
        call screen blockcontinue

label shotgunpick:
    show Eebee pickupbag at Position(xalign=0.5, yalign=0.8) with dissolve
    $ inv.append("shotgun")
    voice "audio/vox/eebee/eebeevoice-25.ogg"
    e "There's my little boom stick!..."
    jump tutorial

label bagpick:
    show Eebee pickup at Position(xalign=0.12, yalign=0.75) with dissolve
    show screen inventory(_layer="ui")
    show screen itemdisplay(_layer="ui")
    $ bagfound = True
    voice "audio/vox/eebee/eebeevoice-26.ogg"
    e "There they are!"
    show Eebee happybag at Position(xalign=0.25, yalign=0.7) with dissolve
    jump tutorial


label leavetutorial:
    voice "audio/vox/eebee/eebeevoice-27.ogg"
    e "Right...Now to intro-"
    show Eebee lookdown at Position(xalign=0.5, yalign=0.8) with vpunch
    e "..."
    show Eebee lookupworried at Position(xalign=0.5, yalign=0.8) with dissolve
    e "..."
    show Eebee panicked at Position(xalign=0.5, yalign=0.85) with vpunch
    voice "audio/vox/eebee/eebeevoice-28.ogg"
    e "Ahh!"
    hide Eebee
    pause 2
    jump scene1


pause
pause
return

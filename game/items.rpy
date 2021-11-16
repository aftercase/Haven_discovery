#Items

label cubetip:
   jump expression renpy.random.choice(["lamp1", "lamp2", "lamp3","lamp4","lamp5"])
   label cube:
    voice "audio/vox/eebee/items/eebeevoice-item3.ogg"
    e "That's my lamp, light the way little lamp!"
    return
   label cube1:
    voice "audio/vox/eebee/items/eebeevoice-item3b.ogg"
    e "It's a lamp. It makes dark things light."
    return
   label cube2:
    voice "audio/vox/eebee/items/eebeevoice-item3c.ogg"
    e "To be technical, all it does is makes obscured code readable."
    return
   label cube3:
    voice "audio/vox/eebee/items/eebeevoice-item3d.ogg"
    e "This little lamp of mine..."
    return
   label cube4:
    voice "audio/vox/eebee/items/eebeevoice-item3e.ogg"
    e "I would do shadow puppets if Havens light system were coded properly..."
    return


label shotguntip:
    ## aim away from the face ##
    jump expression renpy.random.choice(["shotgun1", "shotgun2", "shotgun3","shotgun4","shotgun5"])
    label shotgun1:
     voice "audio/vox/eebee/items/eebeevoice-item1.ogg"
     e "That's my shotgun"
     return
    label shotgun2:
     voice "audio/vox/eebee/items/eebeevoice-item1a.ogg"
     e "It's a stick that goes boom!"
     return
    label shotgun3:
     voice "audio/vox/eebee/items/eebeevoice-item1b.ogg"
     e "Aim away from face. That's what the notes in the programming say..."
     return
    label shotgun4:
     voice "audio/vox/eebee/items/eebeevoice-item1c.ogg"
     e "Never understood why these things have a trigger graphic...They're fired by an event listener..."
     return
    label shotgun5:
     voice "audio/vox/eebee/items/eebeevoice-item1d.ogg"
     e "Shotgun, for all your troubles in Haven."
     return

label lamptip:
   jump expression renpy.random.choice(["lamp1", "lamp2", "lamp3","lamp4","lamp5"])
   label lamp1:
    voice "audio/vox/eebee/items/eebeevoice-item3.ogg"
    e "That's my lamp, light the way little lamp!"
    return
   label lamp2:
    voice "audio/vox/eebee/items/eebeevoice-item3b.ogg"
    e "It's a lamp. It makes dark things light."
    return
   label lamp3:
    voice "audio/vox/eebee/items/eebeevoice-item3c.ogg"
    e "To be technical, all it does is makes obscured code readable."
    return
   label lamp4:
    voice "audio/vox/eebee/items/eebeevoice-item3d.ogg"
    e "This little lamp of mine..."
    return
   label lamp5:
    voice "audio/vox/eebee/items/eebeevoice-item3e.ogg"
    e "I would do shadow puppets if Havens light system were coded properly..."
    return

label medipacktip:
$ healthcount = eebee.cur_hp
with Pause(0.1)
if healthcount <= 99:
    if "medipack" in inv:
        voice "audio/vox/eebee/items/eebeevoice-item2.ogg"
        e "Thank you, A small memory leak can cause all sorts of problems."
        $ eebee.cur_hp = 100
        $ affectioncount += 5
        $ inv.remove("medipack")
    return
else:
    voice "audio/vox/eebee/items/eebeevoice-item2.ogg"
    e "That's a medipack, I don't need it right now"
    return
## in world items ##

screen chests1:
    vbox:
        at Position(xalign = 0.01, yalign = 0.90)
        if not lighton:
            add "images/items/chest/var1/chestdark.png"
        else:
            imagebutton:
             idle "images/items/chest/var1/chestclosed.png"
             hover (im.MatrixColor("images/items/chest/var1/chestclosed.png", im.matrix.brightness(0.25)))
             clicked "images/items/chest/var1/chestopen.png" action Jump("chestopen1")


label bookshow1:
    hide screen bookitem1
    show book1read1 at Position(yalign = 0.90)
    pause
    $ bookcount += 1
    hide book1read1

screen bookitem1:
    imagebutton:
       idle "images/items/book1.png" at Position(xalign = 0.5, yalign = 0.78)
       hover (im.MatrixColor("images/items/book1.png", im.matrix.brightness(0.25)))
       action Call("bookshow1")

screen shotgunitem:
    vbox:
        at Position(xalign = 0.5, yalign = 0.8)
        if "shotgun" in inv:
           pass
        elif bagfound:
            imagebutton:
             idle "images/items/weapons/shotty.png"
             hover (im.MatrixColor("images/items/weapons/shotty.png", im.matrix.brightness(0.25)))
             action Jump("shotgunpick")
        else:
            imagebutton:
             idle "images/items/weapons/shotty.png"

screen lampitem:
    vbox:
        at Position(xalign = 0.25, yalign = 0.70)
        if lighton:
         imagebutton:
          idle "images/items/lamp/lamp-on.png"
        else:
         imagebutton:
          idle "images/items/lamp/lamp-off.png"
          hover (im.MatrixColor("images/items/lamp/lamp-off.png", im.matrix.brightness(0.25)))
          clicked "images/items/lamp/lamp-on.png" action Jump("lampon")

screen bagitem:
    vbox:
     at Position(xalign = 0.12, yalign = 0.75)
     if bagfound:
      pass
     elif bagactive:
      imagebutton:
       idle "images/items/weapons/bags.png"
       hover (im.MatrixColor("images/items/weapons/bags.png", im.matrix.brightness(0.25)))
       action (Jump("bagpick"), Return("Flashlight"))
     else:
      imagebutton:
                idle "images/items/weapons/bags.png"

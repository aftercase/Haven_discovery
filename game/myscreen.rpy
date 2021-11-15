screen shadowsoverlay:
    add "images/lightingmaps/cave.png"
    
screen darkoverlay:
    add "images/lightingmaps/cavedark.png"

screen blockcontinue:
    modal False

screen debug:
    pass

screen flashlight_layer:
    add Flashlight()

screen snowforeground:
    add "images/snowforegrond.png" xalign 0.5 yalign 0.95


label travel:
    scene bg white with pixellate
    show text "{color=#000}Traveling..."
    show eebee walkcyc
    pause(5)
    return

label travel2:
    scene bg white with pixellate
    show text "{color=#000}Traveling..."
    show eebee walkcyc
    show oleka walkcyc
    pause(5)
    return

label travel3:
    scene bg white with pixellate
    show text "{color=#000}Traveling..."
    show eebee walkcyc at Position (xalign = 0.50, yalign = 0.95)
    show oleka walkcyc at Position (xalign = 0.40, yalign = 0.95)
    show blazer flycyc at Position (xalign = 0.40, yalign = 0.25)
    show blazer attack
    pause(5)
    return

screen player_ui: 
    $ healthcount = eebee.cur_hp
    add "gui/stat.png" xalign 1.1 ypos 0.00
    text "[healthcount]" xpos 0.95 ypos 0.010
    add "gui/life_icon.png" xpos 0.93 ypos 0.015
    text "[bookcount]" xpos 0.90 ypos 0.010
    add "gui/boop_icon.png" xpos 0.885 ypos 0.015
    text "[cryptocount]" xpos 0.86 ypos 0.010
    add "gui/coin_icon.png" xpos 0.84 ypos 0.015
    add "gui/opinion_icon.png" xpos 0.67 ypos 0.015
    bar value VariableValue("affectioncount", 100):
      xpos 0.70 ypos 0.010
      xmaximum 250
      ymaximum 20
      left_bar Frame("gui/barfull.png", 20, 0)
      right_bar Frame("gui/barempy.png", 20, 0)
    text "-debug-" xpos 0.50 ypos 0.015

screen inventory:
    vbox: 
        xalign 1.0 ypos 0.058
        add "gui/vstat.png"
    add "gui/inventory.png" xpos 0.94 ypos 0.08
    add "gui/inventory.png" xpos 0.94 ypos 0.19
    add "gui/inventory.png" xpos 0.94 ypos 0.31
    add "gui/inventory.png" xpos 0.94 ypos 0.43
    add "gui/inventory.png" xpos 0.94 ypos 0.55
    add "gui/inventory.png" xpos 0.94 ypos 0.67
    add "gui/inventory.png" xpos 0.94 ypos 0.79

screen itemdisplay:   
    vbox:
     spacing 22
     at Position(xanchor = 0.0,xpos = 0.94, yanchor = 0.0, ypos = 0.08)
     for itemn in inv:
      imagebutton:
       idle ("images/items/item_{}.png").format(itemn)
       hover ("images/items/item_glow_{}.png").format(itemn)
       clicked Call(("{}tip").format(itemn))

screen cavelighting:
    add "images/lightingmaps/cave.png"
    pass

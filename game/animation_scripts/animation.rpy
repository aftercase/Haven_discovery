init -1 python:
    def play_shoot(trans, st, at):
        renpy.play("audio/sfx/shotgun.ogg", channel="sound")
    def play_spear(trans, st, at):
        renpy.play("audio/sfx/spear.ogg", channel="sound")
    def play_bite(trans, st, at):
        renpy.play("audio/sfx/bite.ogg", channel="sound")
    def play_bite2(trans, st, at):
        renpy.play("audio/sfx/bite2.ogg", channel="sound")
    def play_snaikedie(trans, st, at):
        renpy.play("audio/sfx/snaikedie.ogg", channel="sound")
    def play_crush(trans, st, at):
        renpy.play("audio/sfx/crush.ogg", channel="sound")
    def play_rocket(trans, st, at):
        renpy.play("audio/sfx/rocket.ogg", channel="sound")

image glitch dream:
    "images/dreams/glitch/dream_0001.png"
    0.1
    "images/dreams/glitch/dream_0002.png"
    0.1
    "images/dreams/glitch/dream_0003.png"
    0.1
    "images/dreams/glitch/dream_0004.png"
    0.1
    "images/dreams/glitch/dream_0005.png"
    0.1
    "images/dreams/glitch/dream_0006.png"
    0.1
    "images/dreams/glitch/dream_0007.png"
    0.1
    "images/dreams/glitch/dream_0008.png"
    0.1
    "images/dreams/glitch/dream_0009.png"
    0.1
    "images/dreams/glitch/dream_0010.png"
    0.1
    "images/dreams/glitch/dream_0011.png"
    0.1
    "images/dreams/glitch/dream_0012.png"
    0.1
    "images/dreams/glitch/dream_0013.png"
    0.1
    "images/dreams/glitch/dream_0014.png"
    0.1
    "images/dreams/glitch/dream_0015.png"
    0.1
    "images/dreams/glitch/dream_0016.png"
    0.1
    "images/dreams/glitch/dream_0017.png"
    0.1
    "images/dreams/glitch/dream_0018.png"
    0.1
    "images/dreams/glitch/dream_0019.png"
    0.1
    "images/dreams/glitch/dream_0020.png"
    0.1
    repeat
    
image ponipede hurt:
    "images/mobs/ponipede/hurt/ponipede_0001.png"
    0.1
    "images/mobs/ponipede/hurt/ponipede_0002.png"
    0.1
    "images/mobs/ponipede/hurt/ponipede_0003.png"
    0.1
    "images/mobs/ponipede/hurt/ponipede_0004.png"
    0.1
    "images/mobs/ponipede/hurt/ponipede_0005.png"
    0.1
    "images/mobs/ponipede/hurt/ponipede_0006.png"
    0.1
    "images/mobs/ponipede/hurt/ponipede_0007.png"
    0.1
    "images/mobs/ponipede/hurt/ponipede_0008.png"
    0.1
    "images/mobs/ponipede/hurt/ponipede_0009.png"
    0.1

image ponipede idle:
    "images/mobs/ponipede/idle/ponipede_0001.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0002.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0003.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0004.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0005.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0006.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0007.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0008.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0009.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0010.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0012.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0013.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0014.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0015.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0016.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0017.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0018.png"
    0.1
    "images/mobs/ponipede/idle/ponipede_0019.png"
    0.1
    repeat
    
image ponipede fight:
    "images/mobs/ponipede/attack/ponipede_0001.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0002.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0003.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0004.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0005.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0006.png"
    0.1
    function play_crush
    "images/mobs/ponipede/attack/ponipede_0007.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0008.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0009.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0010.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0012.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0013.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0014.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0015.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0016.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0017.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0018.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0019.png"
    0.1
    "images/mobs/ponipede/attack/ponipede_0001.png"
    0.1
    
image snaike death:
    function play_snaikedie
    "images/mobs/snaike/snaikedeath0001.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0002.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0003.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0004.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0005.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0006.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0007.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0008.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0009.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikedeath0010.png"
    xalign 0.93 yalign 0.8
    0.1

image snaike hurt:
    "images/mobs/snaike/snaikehurt0001.png"
    xalign 0.93 yalign 0.8
    1.0
    "images/mobs/snaike/snaikehurt0002.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikehurt0003.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikehurt0004.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikehurt0005.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikehurt0006.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaikehurt0001.png"
    xalign 0.93 yalign 0.8
    1.0


image snaike fight:
    "images/mobs/snaike/snaike0001.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0002.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0003.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0004.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0005.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0006.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0007.png"
    xalign 0.93 yalign 0.8
    0.1
    function play_bite2
    "images/mobs/snaike/snaike0008.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0001.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0002.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0003.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0004.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0005.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0006.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0007.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0008.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0009.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0010.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0011.png"
    xalign 0.93 yalign 0.8
    0.1
    function play_bite
    "images/mobs/snaike/snaike0012.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0013.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0014.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0015.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0016.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0017.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0018.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0019.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0020.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0021.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0022.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0023.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0024.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0025.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0026.png"
    xalign 0.93 yalign 0.8
    0.1
    "images/mobs/snaike/snaike0027.png"
    xalign 0.93 yalign 0.8
    2.0

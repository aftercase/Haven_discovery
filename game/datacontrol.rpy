init python:
    import os
    player_name = os.environ.get('username')
    osu = os.environ.get ('osname')

    e = Character(_("Eebee"), color="#00CC00")
    i = Character(_("Inventory"), color="#cccccc")
    o = Character(_("oleka"), color="#00CC00")
    b = Character(_("Blazer"), color="#00CC00")

    class Options:
        def __init__(self, bpos=(0.0, 0.0), fpos=(0.0, 0.0), zoom=(1.0, 1.0)):
            self.fpos = fpos
            self.cpos = bpos
            self.bpos = bpos
            self.zoom = zoom

        def getpos(self, stance):
            return (self.fpos if (stance == 'front') else self.bpos)

    class Member:
        def __init__(self, name, max_hp, cur_hp, min_dmg, max_dmg, options=Options()):
            self.name = name
            self.max_hp = max_hp
            self.cur_hp = cur_hp
            self.min_dmg = min_dmg
            self.max_dmg = max_dmg
            self.options = options

        def setopt(self, bpos=(0.0, 0.0), fpos=(0.0, 0.0), zoom=(1.0, 1.0)):
            self.options = Options(bpos, fpos, zoom)

        def update(self, anim, time=0.5):
            x, y = self.options.cpos
            pos = Position(xalign=x, yalign=y)
            xzoom, yzoom = self.options.zoom
            tfms = Transform(xzoom=xzoom, yzoom=yzoom)
            trans = [Dissolve(time)]
            mem.display(anim, pos, tfms, trans)

        def display(self, anim, pos, tfms, trans):
            renpy.show(anim, at_list=[pos, tfms])
            for tran in trans:
                renpy.with_statement(tran)

        def whoami(self):
            return self.name.lower().replace('3', 'e').replace('0', 'o')

        def show(self, anim_name, time=0.5):
            who = self.whoami()
            anim = '%s %s' % (who, anim_name)
            self.update(anim, time)

        def hide(self):
            renpy.hide('%s %s' % (self.name, 'disabled')) # Show character's turn is consumed

        def fainted(self):
            return (False if self.cur_hp > 0 else True)

        def say(self, msg):
            self.char(msg)

    class Party(Member):
        def __init__(self, char, *args):
            super(Party, self).__init__(*args)
            self.char = char

        def idle(self):
            anim_name = 'idle50' if self.cur_hp <= 50 else 'idle100'
            who = self.name.lower()
            if (who == 'eebee'):
                anim_name = 'idle100'
            anim = '%s %s' % (who, anim_name)
            return anim

        def to(self, stance, anim=''):
            anim = self.idle()
            self.options.cpos = self.options.getpos(stance)
            self.update(anim)

    # Define all possible party members here
    eebee  = Party(e, "Eebee", 100, 100, 3, 5)
    oleka  = Party(o, "Oleka", 100, 60, 5, 6)
    blazer = Party(b, "Blazer", 100, 49, 10, 15)

    inv = []

python:
    if affectioncount <= 0:
     affectioncount = 0
    if olekaaffection <= 0:
     olekaaffection = 0
## Misc ##

# AI Choice Check - Things AI decides themselves
default forgiveplayer = False

# Story checks
default lighton = False
default bagactive = False
default bagfound = False
default gunfound = False
default okelajoined = True
default blazerjoined = True
default bookcount = 0
default cryptocount = 0
default affectioncount = 5
default olekaaffection = 5
#Manual data checks- will recode once a better way is found
default check1 = False
default check2 = False
default check3 = False
default check4 = False
default check5 = False
default check6 = False
default check7 = False
default check8 = False

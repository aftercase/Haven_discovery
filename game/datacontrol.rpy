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
            self._affection = 0

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

        def get_affection(self):
            return self._affection

        # Use this method to change character's affection
        def set_affection(self, change):
            self._affection += change
            if (self._affection > 100):
                self._affection = 100
            elif (self._affection < 0):
                self._affection = 0


    class Inventory:
        def __init__(self):
            self.items = {}
            self.busy = False   # Not 100% sure this is needed but I've run into some issues after removing it

        def add_item(self, item):
            if not self.busy:
                self.busy = True
                if item not in self.items:
                    self.items.__setitem__(item, 1)
                else:
                    self.items[item] += 1
                self.busy = False

        def use_item(self, item):
            if not self.busy:
                self.busy = True
                # The second check prevents bugs in case some code elsewhere didn't remove used item from dict
                if (item in self.items) and (self.items[item] > 0):
                    self.items[item] -= 1
                    if self.items[item] == 0:
                        self.items.pop(item)
                self.busy = False

    # Define all possible party members here
    eebee  = Party(e, "Eebee", 100, 100, 3, 5)
    oleka  = Party(o, "Oleka", 100, 60, 5, 6)
    blazer = Party(b, "Blazer", 100, 49, 10, 15)

    inv = Inventory()

    _await = False
    def update():
        # If we're already waiting, then stop waiting
        if (_await==True):
            renpy.dynamic(_await=False)
        else: # If we're not waiting, then begin waiting
            renpy.dynamic(_await=True)

    def block(): # Blocks for user input
        while True:
            renpy.dynamic(_await=True) # Dynamically update _await
            if (_await == False): # If we're told to stop waiting, then quit
                break
            else: # Keep waiting for user input
                renpy.pause(1)

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
#Manual data checks- will recode once a better way is found
default check1 = False
default check2 = False
default check3 = False
default check4 = False
default check5 = False
default check6 = False
default check7 = False
default check8 = False

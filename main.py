"""
Title: Go Home
Creators: Jaydah
Description: Skeleton avoids humans trying to get home
"""
#basic game layout & skeleton design + features 
info.set_life(1)
info.start_countdown(60)
scene.set_background_color(9)
game.splash("Get to the castle")
skeleton = sprites.create(img("""
    . . . . 1 1 1 1 1 . . . . . . .
    . . . . 1 f 1 f 1 . . . . . . .
    . . . . 1 1 1 1 1 . . . . . . .
    . . . . 1 b 1 b 1 . . . . . . .
    . . . . 1 b 1 b 1 . . . . . . .
    . . 1 1 1 1 1 1 1 1 1 . . . . .
    . . 1 b . b b b . b 1 . . . . .
    . . 1 1 . 1 1 1 . 1 1 . . . . .
    . . 1 1 . 1 1 1 . 1 1 . . . . .
    . . . . . 1 1 1 . . . . . . . .
    . . . . 1 b b b 1 . . . . . . .
    . . . . 1 b . b 1 . . . . . . .
    . . . . 1 1 . 1 1 . . . . . . .
    . . . . 1 1 . 1 1 . . . . . . .
    . . . . 1 1 . 1 1 . . . . . . .
    . . . . 1 1 . 1 1 . . . . . . .
"""), SpriteKind.player)
skeleton.set_position(10, 153)
controller.move_sprite(skeleton, 60, 0)
scene.camera_follow_sprite(skeleton)
scene.set_tile_map(img("""
    .................999ffff.....................ffffffff...c.................ffffffff.....................ffff9999..............9..........................................................................
    .................999ffff.....................ffffffff...c.................ffffffff.....................ffff9999..........11..9..........................................................................
    .................999ffff.....................ffffffff..3c..............b..ffffffff....................cffff9999.........1111.9..........................................................................
    .................999ffff.....................ffffffff.................ccccffffffff.....................ffff9999.11...........9..........................................................................
    .................999ffff.....................ffffffff....ca..c.c..........ffffffff..............c..cc..ffff99991111..........9..........................................................................
    ......1...1....1.999ffff.....................ffffffff....ccccc...c..c.....ffffffff...........c.........ffff9999..............9..........................................................................
    ..1...11.11...11.999ffff.....................ffffffff.....................ffffffff..............c......ffff9999..............9..........................................................................
    .1111...11111....999ffff.......c.ccc.........ffffffff...............c.....ffffffff......c..c..c........ffff9999..............9..........................................................................
    .................999ffff.....................ffffffff.....................ffffffff..............c......ffff9999..............9..........................................................................
    ...............b.999ffff.....c...............ffffffff..............c......ffffffff....c................ffff9999.a............9..........................................................................
    77777777777777777777ffff..................b..ffffffff.....................ffffffff..................b..ffff777737777777777777777777.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff..3cc....ca..c...cc..ffffffffcccc....c..a.c.......ffffffff..3cccc..ca.c.ccccc..ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff.........ccccc.......ffffffff........cccccc.......ffffffff.........cccc........ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff.....................ffffffff.....................ffffffff.....................ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff.....................ffffffff.....................ffffffff.....................ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeee222222222222222222222222222222222222222222222222222222222222222222222222222222222222222eeeeeeeeeeeeeeeeeeeeeeee.....................................................................
"""))

# set up castle/house
house = sprites.create(img("""
    ...cccccc.......cccccc...
    ...cccccc.......cccccc...
    ...cccccc.......cccccc...
    ...f.................f...
    ...f.................f...
    ...f.................f...
    ..fff...............fff..
    .fffff.............fffff.
    fffffff...........fffffff
    ccccccc...........ccccccc
    ccccccc...........ccccccc
    ccccccc...........ccccccc
    ccccccc...........ccccccc
    ccccccc...........ccccccc
    ccccccc...........ccccccc
    ccccccc...........ccccccc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    ccfffffcccccccccccfffffcc
    cfffffffcccccccccfffffffc
    cfffffffcccccccccfffffffc
    cfffffffcccccccccfffffffc
    cfffffffcccccccccfffffffc
    cfffffffcccccccccfffffffc
    ccfffffcccccccccccfffffcc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    ccccccccccccccccccccccccc
    cccccccccfffffffccccccccc
    cccccccccfcccccfccccccccc
    cccccccccfcccccfccccccccc
    cccccccccfccccffccccccccc
    cccccccccfcccccfccccccccc
    cccccccccfcccccfccccccccc
"""), SpriteKind.food)
house.set_position(2000, 140)
def on_overlap2(sprite, otherSprite):
    game.over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap2)

#set up coins 
coinLocations = [
    tiles.get_tile_location(34,6),
    tiles.get_tile_location(73,11),
    tiles.get_tile_location(57,3),
    tiles.get_tile_location(88,6),
    tiles.get_tile_location(66,4)
]
#coin design 
for i in range(len(coinLocations)):
    coin = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . c c c c c . . . . . .
        . . . . c c c c c c c . . . . .
        . . . . c c f c f c c . . . . .
        . . . . c c c f c c c . . . . .
        . . . . c c f c f c c . . . . .
        . . . . c c c c c c c . . . . .
        . . . . . c c c c c . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), SpriteKind.projectile)
    tiles.place_on_tile(coin, coinLocations[i])
#what happens between skeleton & coins 
def on_overlap3(sprite, otherSprite):
    info.change_score_by(1)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_overlap3)
 
#tilemap design
scene.set_tile(7, img("""
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    6 7 7 7 6 6 7 7 7 6 6 7 6 7 7 6
    e 6 7 6 e e 6 7 7 6 e 6 6 7 6 e
    e e 6 e e e e 6 7 6 e e e 6 e e
    e e e e e e e e 6 e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
"""), True)
scene.set_tile(11, img("""
    . . . . . . . . . . . . . . . .
    . . . . c c c c c c c . . . . .
    . . . c f c c f c f c c . . . .
    . . c f c f f c f c f c c . . .
    . c f c f f c c c c c f c c . .
    . c c c f c c f c f f c f c . .
    . c f c c c f c c c c c c c . .
    . c c f c f c f c f c f f c . .
    . c c c f c c c c c f c c c . .
    . c f c c f f c f c f c f c . .
    . c c f c c c c c f c c c c . .
    . . c c f c f f c c f c c . . .
    . . . c c f c c f c f c . . . .
    . . . . c c c c c c c . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), True)
scene.set_tile(9, img("""
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
"""), True)
scene.set_tile(3, img("""
    c c c c c c c c c c c c c c c c
    c c a a a a a a a a a a a a c c
    c a c c c c c c c c c c c c a c
    c a c c a a a a a a a a c c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c c a a a a a a a a c c a c
    c a c c c c c c c c c c c c a c
    c c a a a a a a a a a a a a c c
    c c c c c c c c c c c c c c c c
"""), True)
scene.set_tile(12, img("""
    c c c c c c c c c c c c c c c c
    c c a a a a a a a a a a a a c c
    c a c c c c c c c c c c c c a c
    c a c c a a a a a a a a a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c a c c c c c c c c a c a c
    c a c c a a a a a a a a c c a c
    c a c c c c c c c c c c c c a c
    c c a a a a a a a a a a a a c c
    c c c c c c c c c c c c c c c c
"""), True)
scene.set_tile(2, img("""
    5 5 2 2 2 2 5 4 5 4 4 5 5 5 5 5
    5 2 2 2 5 5 4 5 2 5 4 4 4 5 4 4
    2 2 2 5 4 4 4 2 2 2 5 5 4 4 4 4
    5 5 5 4 4 5 2 2 2 2 5 4 2 2 2 5
    4 4 4 4 5 5 2 2 2 2 5 4 2 2 2 5
    2 2 2 5 4 5 2 5 5 5 5 4 2 2 2 5
    2 2 2 5 5 4 5 5 4 4 4 4 2 2 5 4
    2 2 2 2 2 5 4 4 4 5 5 5 2 5 4 4
    2 2 2 2 2 2 4 2 2 2 5 5 5 5 4 5
    5 4 4 5 5 2 4 5 2 2 5 4 4 4 4 5
    4 5 4 4 5 2 4 5 2 2 5 4 5 5 5 2
    2 4 2 2 4 5 2 4 5 5 4 5 2 2 2 2
    2 2 4 2 5 4 2 4 4 4 4 5 2 2 2 2
    2 2 4 2 4 2 2 4 2 2 4 5 5 2 2 2
    2 4 2 2 5 4 2 4 2 2 4 4 5 2 2 2
    4 5 2 2 2 5 4 2 2 2 2 4 5 2 2 2
"""), True)
scene.set_tile(10, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
scene.set_tile(15, img("""
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
    b b b b b b b b b b b b b b b b
"""), True)


#human/enemy 
locations = [
    tiles.get_tile_location(34, 11),
    tiles.get_tile_location(64, 11),
    tiles.get_tile_location(92, 11),
    tiles.get_tile_location(58, 4),
    
#setting up the enemy/human + location 
]
for i in range(len(locations)):
    human = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . 5 5 5 5 5 . . . . . . .
        . . . . 5 d d d 5 . . . . . . .
        . . . . d f d f d . . . . . . .
        . . . . d d d d d . . . . . . .
        . . f f f f f f f f f . . . . .
        . . d d f f f f f d d . . . . .
        . . d d f f f f f d d . . . . .
        . . d d f f f f f d d . . . . .
        . . d d f f f f f d d . . . . .
        . . . . 8 9 8 9 8 . . . . . . .
        . . . . 9 8 8 8 9 . . . . . . .
        . . . . 8 8 8 8 8 . . . . . . .
        . . . . 8 8 . 8 8 . . . . . . .
        . . . . 9 9 . 9 9 . . . . . . .
        . . . . d d . d d . . . . . . .
    """), SpriteKind.enemy)
    human.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
    # human.set_position(520, 184)
    human.vx = -25
    # scene.place_on_random_tile(human, 10)
    tiles.place_on_tile(human, locations[i])

#jumping
doublejump = True 
skeleton.ay = 200
def jump():
    global doublejump
    if doublejump:
        skeleton.vy = -100
        doublejump = skeleton.is_hitting_tile(CollisionDirection.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, jump)
#jumping
def on_update():
    # skeleton.say(str(skeleton.x))
    global doublejump
    if skeleton.is_hitting_tile(CollisionDirection.BOTTOM):
        doublejump = True
game.on_update(on_update)

#spawning skeleton for rach level 
def teleportation(sprite):
    if skeleton.x < 400:
        skeleton.set_position(420, 160)
        scene.set_background_color(15)
    if 1500 < skeleton.x < 2000:
        skeleton.set_position(1781, 150)
        scene.set_background_color(9)
    if 850 < skeleton.x < 1600:
        skeleton.set_position(1350, 140)
    if 450 < skeleton.x < 850:
        skeleton.set_position(884, 25)   
scene.on_hit_tile(SpriteKind.player, 11, teleportation)

def on_overlap(sprite, otherSprite):
    game.over()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)

#lava + skeleton = respawn (lose)
def Lava(sprite):
    game.over(False)
scene.on_hit_tile(SpriteKind.player, 2, Lava)

#win 
def castle(sprite):
    game.over(True)
scene.on_hit_tile(SpriteKind.player, 4, castle)


"""
Title: Go Home
Creators: Emily and Jaydah
Description: Skeleton avoids humans trying to get home
"""
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
Castle = sprites.create(img("""
    ................................................
    ................................................
    ................................................
    ................................................
    ................................................
    .....a......................................a...
    ....aaa....................................aaa..
    ....aaa....................................aaa..
    ...aaaaa..................................aaaaa.
    ...aaaaa..................................aaaaa.
    ..aaaaaaa................................aaaaaaa
    ..aaaaaaa................................aaaaaaa
    .ccccccccc..............................cccccccc
    ....ccc....................................ccc..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbb..
    ....bbbbbbbbbfffbbbbbbbbbbbbbbbbbbbfffbbbbbbbb..
    ....bbbbbbbbf1f1fbbbbbbbbbbbbbbbbbf1f1fbbbbbbb..
    ....bbbbbbbf11f11fbbbbbbbbbbbbbbbf11f11fbbbbbb..
    ....bbbbbbbf11f11fbbbbbbbbbbbbbbbf11f11fbbbbbb..
    ....bbbbbbbf11f11fbbbbbbbbbbbbbbbf11f11fbbbbbb..
    ....bbbbbbbfffffffbbbbbbbbbbbbbbbfffffffbbbbbb..
    ....bbbbbbbf11f11fbbbbbbbbbbbbbbbf11f11fbbbbbb..
    ....bbbbbbbf11f11fbbbbbbbbbbbbbbbf11f11fbbbbbb..
    ....bbbbbbbf11f11fbbbbbbbbbbbbbbbf11f11fbbbbbb..
    ....bbbbbbbfffffffbbbbbbbbbbbbbbbfffffffbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbbfe4e4fbbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbbf4e4e4efbbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbbfe4e4e4e4fbbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbbf4e4e4e4e4efbbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbfe4e4e4e4e4e4fbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbfe4e444e4e4e4fbbbbbbbbbbbbbb..
    ....bbbbbbbbbbbbbbfe4e444e4e4e4fbbbbbbbbbbbbbb..
    ....ccccccccccccbbfe4e444e4e4e4fbccccccccccccc..
    ....ccacccccccccbbfe4e4e4e4e444fbccccaacccccac..
    ....cacaccaccaccbbfe4e4e4e4e444fbcacaacaccaccc..
    ....cccccccaacccbbfe4e4e4e4e444fbccccaacccaacc..
    ....caaaacccacacbbfe4e4e4e4e4e4fbccaaaaacccaac..
    ....ccccccccccccbbfe4e4e4e444e4fbccccccccccccc..
"""), SpriteKind.food)
Castle.set_position(2000, 140)
scene.set_tile_map(img("""
    .................999ffff.....................ffffffff...c.................ffffffff..................c..ffff9999..............9..........................................................................
    .................999ffff.....................ffffffff...c.................ffffffff................ccc..ffff9999..........11..9..........................................................................
    .................999ffff.....................ffffffff..3...............b..ffffffff.....................ffff9999.........1111.9..........................................................................
    .................999ffff.....................ffffffff............ccc..ccccffffffff............ccc......ffff9999.11...........9..........................................................................
    .................999ffff.....................ffffffff....ca..c............ffffffff.......ca.c..........ffff99991111..........9..........................................................................
    ......1...1....1.999ffff.....................ffffffff....ccccc.c..........ffffffff....c..cccc..........ffff9999..............9..........................................................................
    ..1...11.11...11.999ffff.....................ffffffff..........cc.........ffffffff.............ca.c....ffff9999..............9..........................................................................
    .1111...11111....999ffff.....................ffffffff.............c.......ffffffff.....c.......cccc....ffff9999..............9..........................................................................
    .................999ffff.......ccc...........ffffffff.......c.............ffffffff.....................ffff9999..............9..........................................................................
    ...............b.999ffff.....................ffffffff..............cc.....ffffffff....cc..........cc...ffff9999..............9..........................................................................
    77777777777777777777ffff...........c......b.cffffffff.....c...........c...ffffffff........ca.c.........ffff777737777777777777777777.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff..3cccc.ca...c.cccc..ffffffffcccc...c...ac.....c..ffffffff.c3c....cccc.cc......ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff........ccccc........ffffffff........ccccc.......cffffffff................cc..bffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff.....................ffffffff.....................ffffffff...................ccffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff............3........ffffffff...............cc..ccffffffff.....................ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeee222222222222222222222222222222222222222222222222222222222222222222222222222222222222222eeeeeeeeeeeeeeeeeeeeeeee.....................................................................
"""))
scene.set_tile(7, img("""
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
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
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c c c c c c c c c c c c c c c
"""), True)
scene.set_tile(12, img("""
    c c c c c c c c c c c c c c c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c b c b c b c b c b c b c b c
    c b c b c b c b c b c b c b c c
    c c c c c c c c c c c c c c c c
"""), True)
scene.set_tile(2, img("""
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
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
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
"""), True)

locations = [
    tiles.get_tile_location(33, 11),
    tiles.get_tile_location(64, 11),
    tiles.get_tile_location(58, 4),
    tiles.get_tile_location(90, 4),
    tiles.get_tile_location(91, 10),
    tiles.get_tile_location(96, 6)
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
    human.vx = -15
    # scene.place_on_random_tile(human, 10)
    tiles.place_on_tile(human, locations[i])
#jumping
doublejump = True 
skeleton.ay = 250
def jump():
    global doublejump
    if doublejump:
        skeleton.vy = -100
        doublejump = skeleton.is_hitting_tile(CollisionDirection.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, jump)

def on_update():
    #skeleton.say(str(skeleton.y))
    global doublejump
    if skeleton.is_hitting_tile(CollisionDirection.BOTTOM):
        doublejump = True
game.on_update(on_update)

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

def Lava(sprite):
    game.over(False)
scene.on_hit_tile(SpriteKind.player, 2, Lava)

def on_overlap2(sprite, otherSprite):
    game.over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap2)


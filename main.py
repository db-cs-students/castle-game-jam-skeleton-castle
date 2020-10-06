"""
Title: Go Home
Creators: Emily and Jaydah
Description: Skeleton avoids humans trying to get home
"""
#setup/sprites

scene.set_background_color(9)

game.splash("Get to the castle")

info.set_score(0)

skeleton = sprites.create(img("""
    . . 1 1 1 1 1 . . . . . . . . .
    . . 1 f 1 f 1 . . . . . . . . .
    . . 1 1 1 1 1 . . . . . . . . .
    . . 1 b 1 b 1 . . . . . . . . .
    . . 1 b 1 b 1 . . . . . . . . .
    1 1 1 1 1 1 1 1 1 . . . . . . .
    1 b . b b b . b 1 . . . . . . .
    1 1 . 1 1 1 . 1 1 . . . . . . .
    1 1 . 1 1 1 . 1 1 . . . . . . .
    . . . 1 1 1 . . . . . . . . . .
    . . 1 b b b 1 . . . . . . . . .
    . . 1 b . b 1 . . . . . . . . .
    . . 1 1 . 1 1 . . . . . . . . .
    . . 1 1 . 1 1 . . . . . . . . .
    . . 1 1 . 1 1 . . . . . . . . .
    . . 1 1 . 1 1 . . . . . . . . .
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
    ....b7b77bb777bbbbfe4e4e4e4e4e4fbbb7bb77b777b7..
    ....77775777b77bbbfe4e444e4e4e4fbb7b777577b7577.
    ....775777757777bbfe4e444e4e4e4fb777577777757b..
    ....ccccc777ccccbbfe4e444e4e4e4fbcccccc77ccccc..
    ....ccacccccccccbbfe4e4e4e4e444fbccccaacccccac..
    ....cacaccaccaccbbfe4e4e4e4e444fbcacaacaccaccc..
    ....cccccccaacccbbfe4e4e4e4e444fbccccaacccaacc..
    ....caaaacccacacbbfe4e4e4e4e4e4fbccaaaaacccaac..
    ....ccccccccccccbbfe4e4e4e444e4fbccccccccccccc..
"""), SpriteKind.food)

Castle.set_position(2000, 140)

#tilemap

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

#coins

coinLocations = [
    tiles.get_tile_location(32, 7),
    tiles.get_tile_location(73, 13),
    tiles.get_tile_location(99, 0)
]

for i in range(len(coinLocations)):
    coin = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . 5 5 5 5 5 5 5 4 . . . .
        . . . 5 5 5 5 5 5 5 5 5 4 . . .
        . . . 5 5 5 5 4 5 5 5 5 4 . . .
        . . . 5 5 5 4 4 5 5 5 5 4 . . .
        . . . 5 5 5 5 4 5 5 5 5 4 . . .
        . . . 5 5 5 5 4 5 5 5 5 4 . . .
        . . . 5 5 5 4 4 4 5 5 5 4 . . .
        . . . 5 5 5 5 5 5 5 5 5 4 . . .
        . . . . 5 5 5 5 5 5 5 4 . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), SpriteKind.projectile)
    tiles.place_on_tile(coin, coinLocations[i])

def on_overlap3(sprite, otherSprite):
    info.change_score_by(1)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_overlap3)

#human locations

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
    human.vx = -15
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
    global doublejump
    if skeleton.is_hitting_tile(CollisionDirection.BOTTOM):
        doublejump = True
game.on_update(on_update)

#moving between levels 

def teleportation(sprite):
    if skeleton.x < 400:
        skeleton.set_position(420, 160)
        scene.set_background_color(15)
        game.splash("Don't let the humans catch you!")
    if 1500 < skeleton.x < 2000:
        skeleton.set_position(1781, 150)
        scene.set_background_color(9)
    if 850 < skeleton.x < 1600:
        skeleton.set_position(1350, 140)
    if 450 < skeleton.x < 850:
        skeleton.set_position(884, 25)   
scene.on_hit_tile(SpriteKind.player, 11, teleportation)

#win/lose

def on_overlap(sprite, otherSprite):
    game.over()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)

def Lava(sprite):
    game.over(False)
scene.on_hit_tile(SpriteKind.player, 2, Lava)

def on_overlap2(sprite, otherSprite):
    game.over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap2)

# moving left/right

def on_event_pressed():
    skeleton.set_image(img("""
        . . . . . . 1 1 1 . . . . . . .
        . . . . . . 1 1 f . . . . . . .
        . . . . . . 1 1 1 . . . . . . .
        . . . . . . . b 1 . . . . . . .
        . . . . . . . b . . . . . . . .
        . . . . . . 1 1 . . . . . . . .
        . . . . . . 1 b 1 . . . . . . .
        . . . . . . 1 b 1 1 . . . . . .
        . . . . . . 1 1 . . . . . . . .
        . . . . . . b b . . . . . . . .
        . . . . . . 1 1 1 . . . . . . .
        . . . . . . 1 . 1 . . . . . . .
        . . . . . . 1 . 1 . . . . . . .
        . . . . . . 1 . 1 . . . . . . .
        . . . . . . 1 . 1 . . . . . . .
        . . . . . . 1 . 1 . . . . . . .
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

def on_event_released():
    skeleton.set_image(img("""
        . . 1 1 1 1 1 . . . . . . . . .
        . . 1 f 1 f 1 . . . . . . . . .
        . . 1 1 1 1 1 . . . . . . . . .
        . . 1 b 1 b 1 . . . . . . . . .
        . . 1 b 1 b 1 . . . . . . . . .
        1 1 1 1 1 1 1 1 1 . . . . . . .
        1 b . b b b . b 1 . . . . . . .
        1 1 . 1 1 1 . 1 1 . . . . . . .
        1 1 . 1 1 1 . 1 1 . . . . . . .
        . . . 1 1 1 . . . . . . . . . .
        . . 1 b b b 1 . . . . . . . . .
        . . 1 b . b 1 . . . . . . . . .
        . . 1 1 . 1 1 . . . . . . . . .
        . . 1 1 . 1 1 . . . . . . . . .
        . . 1 1 . 1 1 . . . . . . . . .
        . . 1 1 . 1 1 . . . . . . . . .
    """))
controller.right.on_event(ControllerButtonEvent.RELEASED, on_event_released)

def on_event_pressed2():
    skeleton.set_image(img("""
        . . . . . . . 1 1 1 . . . . . .
        . . . . . . . f 1 1 . . . . . .
        . . . . . . . 1 1 1 . . . . . .
        . . . . . . . 1 b . . . . . . .
        . . . . . . . . b . . . . . . .
        . . . . . . . . 1 1 . . . . . .
        . . . . . . . 1 b 1 . . . . . .
        . . . . . . 1 1 b 1 . . . . . .
        . . . . . . . . 1 1 . . . . . .
        . . . . . . . . b b . . . . . .
        . . . . . . . 1 1 1 . . . . . .
        . . . . . . . 1 . 1 . . . . . .
        . . . . . . . 1 . 1 . . . . . .
        . . . . . . . 1 . 1 . . . . . .
        . . . . . . . 1 . 1 . . . . . .
        . . . . . . . 1 . 1 . . . . . .
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_event_pressed2)

def on_event_released2():
    skeleton.set_image(img("""
        . . 1 1 1 1 1 . . . . . . . . .
        . . 1 f 1 f 1 . . . . . . . . .
        . . 1 1 1 1 1 . . . . . . . . .
        . . 1 b 1 b 1 . . . . . . . . .
        . . 1 b 1 b 1 . . . . . . . . .
        1 1 1 1 1 1 1 1 1 . . . . . . .
        1 b . b b b . b 1 . . . . . . .
        1 1 . 1 1 1 . 1 1 . . . . . . .
        1 1 . 1 1 1 . 1 1 . . . . . . .
        . . . 1 1 1 . . . . . . . . . .
        . . 1 b b b 1 . . . . . . . . .
        . . 1 b . b 1 . . . . . . . . .
        . . 1 1 . 1 1 . . . . . . . . .
        . . 1 1 . 1 1 . . . . . . . . .
        . . 1 1 . 1 1 . . . . . . . . .
        . . 1 1 . 1 1 . . . . . . . . .
    """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_event_released2)

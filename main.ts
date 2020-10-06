let human: Sprite;
/** 
Title: Go Home
Creators: Emily and Jaydah
Description: Skeleton avoids humans trying to get home

 */
scene.setBackgroundColor(9)
game.splash("Get to the castle")
let skeleton = sprites.create(img`
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
`, SpriteKind.Player)
skeleton.setPosition(10, 153)
controller.moveSprite(skeleton, 60, 0)
scene.cameraFollowSprite(skeleton)
scene.setTileMap(img`
    .................999ffff.....................ffffffff...c.................ffffffff.....................ffff9999..............9..........................................................................
    .................999ffff.....................ffffffff...c.................ffffffff.....................ffff9999..........11..9..........................................................................
    .................999ffff.....................ffffffff..3ca..c..........b..ffffffff.....................ffff9999.........1111.9..........................................................................
    .................999ffff.....................ffffffff....cccc....ccc..ccccffffffff.....................ffff9999.11...........9..........................................................................
    .................999ffff.....................ffffffff.........c...........ffffffff.....................ffff99991111..........9..........................................................................
    ......1...1....1.999ffff.....................ffffffff..........c..........ffffffff.....................ffff9999..............9..........................................................................
    ..1...11.11...11.999ffff.....................ffffffff..........cc.........ffffffff.....................ffff9999..............9..........................................................................
    .1111...11111....999ffff.....................ffffffff.............c.......ffffffff......c..c..c........ffff9999..............9..........................................................................
    .................999ffff.......ccc...........ffffffff.......c.............ffffffff..............c......ffff9999.............49..........................................................................
    ...............b.999ffff.....................ffffffff..............cc.....ffffffff....c................ffff9999.............49..........................................................................
    77777777777777777777ffff...........c......b.cffffffff.....c...........c...ffffffff..................b.cffff777737777777777777777777.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff..3cccc.ca...c.cccc..ffffffffcccc...c...ac.....c..ffffffff..3cccc.c.a.c.ccccc..ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff........ccccc........ffffffff........ccccc.......cffffffff........ccccc........ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff.....................ffffffff.....................ffffffff.....................ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff............3........ffffffff...............cc..ccffffffff.....................ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeee222222222222222222222222222222222222222222222222222222222222222222222222222222222222222eeeeeeeeeeeeeeeeeeeeeeee.....................................................................
`)
scene.setTile(7, img`
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
`, true)
scene.setTile(11, img`
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
`, true)
scene.setTile(9, img`
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
`, true)
scene.setTile(3, img`
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
`, true)
scene.setTile(12, img`
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
`, true)
scene.setTile(2, img`
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
`, true)
scene.setTile(10, img`
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
`)
scene.setTile(4, img`
    ..........bb.....................................bb.........
    .........bbbb...................................bbbb........
    ........bbbbbb.................................bbbbbb.......
    ........bbbbbb.................................bbbbbb.......
    ........cccccc.................................cccccc.......
    ........cccccc.................................cccccc.......
    ........cccccc.................................cccccc.......
    ........cccccc.................................cccccc.......
    ........cccccc.................................cccccc.......
    ........cccccc.................................cccccc.......
    ........ccccccccccccccccccccccccccccccccccccccccccccc.......
    ........ccccccccccccccccccccccccccccccccccccccccccccc.......
    ........ccccccccccccccccccccccccccccccccccccccccccccc.......
    ........ccccccccccccccccccccccccccccccccccccccccccccc.......
    ........ccccccccccccccccccccccccccccccccccccccccccccc.......
    ........ccccccccccccccccccccccccccccccccccccccccccccc.......
    ........ccccccccccccccccccccccccccccccccccccccccccccc.......
    ........ccbbbbbbbbbcccccccccccccccccccccccbbbbbbbbbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbcccccccbcccccccccccccccccccccccbcccccccbcc.......
    ........ccbbbbbbbbbcccccccccccccccccccccccbbbbbbbbbcc.......
    ........cccccccccccccccccccccbbbbbbcccccccccccccccccc.......
    ........cccccccccccccccccccccbbbbbbcccccccccccccccccc.......
    ........cccccccccccccccccccccbbbbbbcccccccccccccccccc.......
    ........cccccccccccccccccccccbbbbbbcccccccccccccccccc.......
    ........cccccccccccccccccccccbbbbcbcccccccccccccccccc.......
    ........cccccccccccccccccccccbbbbbbcccccccccccccccccc.......
    ........cccccccccccccccccccccbbbbbbcccccccccccccccccc.......
    ........cccccccccccccccccccccbbbbbbcccccccccccccccccc.......
    ........cccccccccccccccccccccbbbbbbcccccccccccccccccc.......
`, true)
scene.setTile(15, img`
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
`, true)
let locations = [tiles.getTileLocation(33, 11), tiles.getTileLocation(64, 11), tiles.getTileLocation(92, 11), tiles.getTileLocation(57, 2)]
for (let i = 0; i < locations.length; i++) {
    human = sprites.create(img`
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
    `, SpriteKind.Enemy)
    human.setFlag(SpriteFlag.BounceOnWall, true)
    //  human.set_position(520, 184)
    human.vx = -10
    //  scene.place_on_random_tile(human, 10)
    tiles.placeOnTile(human, locations[i])
}
// jumping
let doublejump = true
skeleton.ay = 200
controller.A.onEvent(ControllerButtonEvent.Pressed, function jump() {
    
    if (doublejump) {
        skeleton.vy = -100
        doublejump = skeleton.isHittingTile(CollisionDirection.Bottom)
    }
    
})
game.onUpdate(function on_update() {
    //  skeleton.say(str(skeleton.x))
    
    if (skeleton.isHittingTile(CollisionDirection.Bottom)) {
        doublejump = true
    }
    
})
scene.onHitTile(SpriteKind.Player, 11, function teleportation(sprite: Sprite) {
    if (skeleton.x < 400) {
        skeleton.setPosition(420, 160)
        scene.setBackgroundColor(15)
    }
    
    if (1500 < skeleton.x && skeleton.x < 2000) {
        skeleton.setPosition(1781, 150)
        scene.setBackgroundColor(9)
    }
    
    if (850 < skeleton.x && skeleton.x < 1600) {
        skeleton.setPosition(1350, 140)
    }
    
    if (450 < skeleton.x && skeleton.x < 850) {
        skeleton.setPosition(884, 25)
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap(sprite: Sprite, otherSprite: Sprite) {
    game.over()
})
scene.onHitTile(SpriteKind.Player, 2, function Lava(sprite: Sprite) {
    game.over(false)
})
scene.onHitTile(SpriteKind.Player, 4, function castle(sprite: Sprite) {
    game.over(true)
})

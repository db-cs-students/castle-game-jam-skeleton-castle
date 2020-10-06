let i: number;
let coin: Sprite;
let human: Sprite;
/** 
Title: Go Home
Creators: Emily and Jaydah
Description: Skeleton avoids humans trying to get home

 */
// setup/sprites
scene.setBackgroundColor(9)
game.splash("Get to the castle")
info.setScore(0)
let skeleton = sprites.create(img`
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
`, SpriteKind.Player)
skeleton.setPosition(10, 153)
controller.moveSprite(skeleton, 60, 0)
scene.cameraFollowSprite(skeleton)
let Castle = sprites.create(img`
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
`, SpriteKind.Food)
Castle.setPosition(2000, 140)
// tilemap
scene.setTileMap(img`
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
// coins
let coinLocations = [tiles.getTileLocation(32, 7), tiles.getTileLocation(73, 13), tiles.getTileLocation(99, 0)]
for (i = 0; i < coinLocations.length; i++) {
    coin = sprites.create(img`
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
    `, SpriteKind.Projectile)
    tiles.placeOnTile(coin, coinLocations[i])
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_overlap3(sprite: Sprite, otherSprite: Sprite) {
    info.changeScoreBy(1)
    otherSprite.destroy()
})
// human locations
let locations = [tiles.getTileLocation(33, 11), tiles.getTileLocation(64, 11), tiles.getTileLocation(58, 4), tiles.getTileLocation(90, 4), tiles.getTileLocation(91, 10), tiles.getTileLocation(96, 6)]
for (i = 0; i < locations.length; i++) {
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
    human.vx = -15
    tiles.placeOnTile(human, locations[i])
}
// jumping
let doublejump = true
skeleton.ay = 250
controller.A.onEvent(ControllerButtonEvent.Pressed, function jump() {
    
    if (doublejump) {
        skeleton.vy = -100
        doublejump = skeleton.isHittingTile(CollisionDirection.Bottom)
    }
    
})
game.onUpdate(function on_update() {
    
    if (skeleton.isHittingTile(CollisionDirection.Bottom)) {
        doublejump = true
    }
    
})
// moving between levels 
scene.onHitTile(SpriteKind.Player, 11, function teleportation(sprite: Sprite) {
    if (skeleton.x < 400) {
        skeleton.setPosition(420, 160)
        scene.setBackgroundColor(15)
        game.splash("Don't let the humans catch you!")
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
// win/lose
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap(sprite: Sprite, otherSprite: Sprite) {
    game.over()
})
scene.onHitTile(SpriteKind.Player, 2, function Lava(sprite: Sprite) {
    game.over(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    game.over(true)
})
//  moving left/right
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed() {
    skeleton.setImage(img`
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
    `)
})
controller.right.onEvent(ControllerButtonEvent.Released, function on_event_released() {
    skeleton.setImage(img`
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
    `)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed2() {
    skeleton.setImage(img`
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
    `)
})
controller.left.onEvent(ControllerButtonEvent.Released, function on_event_released2() {
    skeleton.setImage(img`
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
    `)
})

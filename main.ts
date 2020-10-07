let i: number;
let coin: Sprite;
let human: Sprite;
/** 
Title: Go Home
Creators: Emily and Jaydah
Description: Skeleton avoids humans trying to get home

 */
// basic game layout & skeleton design + features 
info.setLife(1)
info.startCountdown(60)
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
    .................999ffff.....................ffffffff..3c..........c...b..ffffffff....................cffff9999.........1111.9..........................................................................
    .................999ffff.....................ffffffff.................ccccffffffff.....................ffff9999.11...........9..........................................................................
    .................999ffff.....................ffffffff....ca..c.c..........ffffffff..............c..cc..ffff99991111..........9..........................................................................
    ......1...1....1.999ffff.....................ffffffff....ccccc............ffffffff...........c.........ffff9999..............9..........................................................................
    ..1...11.11...11.999ffff.....................ffffffff............c........ffffffff..............c......ffff9999..............9..........................................................................
    .1111...11111....999ffff.......c.ccc.........ffffffff...............cc....ffffffff......c..c..c........ffff9999..............9..........................................................................
    .................999ffff.....................ffffffff.....................ffffffff..............c......ffff9999..............9..........................................................................
    ...............b.999ffff.....c...............ffffffff..............c......ffffffff....c................ffff9999.a............9..........................................................................
    77777777777777777777ffff..................b..ffffffff.....................ffffffff..................b..ffff777737777777777777777777.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff..3cc....ca..c...cc..ffffffffcccc....c..a.c.......ffffffff..3cccc..ca.c.ccccc..ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff.........ccccc.......ffffffff........cccccc.......ffffffff.........cccc........ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff.....................ffffffff.....................ffffffff.....................ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeeeffff.....................ffffffff.....................ffffffff.....................ffffeeeeeeeeeeeeeeeeeeeeeeee.....................................................................
    eeeeeeeeeeeeeeeeeeee222222222222222222222222222222222222222222222222222222222222222222222222222222222222222eeeeeeeeeeeeeeeeeeeeeeee.....................................................................
`)
//  set up castle/house
let house = sprites.create(img`
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
`, SpriteKind.Food)
house.setPosition(2000, 140)
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    game.over(true)
})
// set up coins 
let coinLocations = [tiles.getTileLocation(34, 6), tiles.getTileLocation(73, 11), tiles.getTileLocation(57, 3), tiles.getTileLocation(88, 6), tiles.getTileLocation(66, 4)]
// coin design 
for (i = 0; i < coinLocations.length; i++) {
    coin = sprites.create(img`
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
    `, SpriteKind.Projectile)
    tiles.placeOnTile(coin, coinLocations[i])
}
// what happens between skeleton & coins 
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_overlap3(sprite: Sprite, otherSprite: Sprite) {
    info.changeScoreBy(1)
    otherSprite.destroy()
})
// tilemap design
scene.setTile(7, img`
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
`, true)
scene.setTile(12, img`
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
`, true)
scene.setTile(2, img`
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
`, true)
// human/enemy 
let locations = [tiles.getTileLocation(34, 11), tiles.getTileLocation(64, 11), tiles.getTileLocation(92, 11), tiles.getTileLocation(58, 4)]
// setting up the enemy/human + location 
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
    //  human.set_position(520, 184)
    human.vx = -25
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
// jumping
game.onUpdate(function on_update() {
    //  skeleton.say(str(skeleton.x))
    
    if (skeleton.isHittingTile(CollisionDirection.Bottom)) {
        doublejump = true
    }
    
})
// spawning skeleton for rach level 
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
// lava + skeleton = respawn (lose)
scene.onHitTile(SpriteKind.Player, 2, function Lava(sprite: Sprite) {
    game.over(false)
})
// win 
scene.onHitTile(SpriteKind.Player, 4, function castle(sprite: Sprite) {
    game.over(true)
})

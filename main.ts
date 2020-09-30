/** 
Title: Go Home
Creators: Emily and Jaydah
Description: Skeleton avoids humans trying to get home

 */
scene.setBackgroundColor(9)
let human = sprites.create(img`
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . 3 3 3 3 3 3 3 3 3 3 3 . .
    . . . 3 . . . . . . . . . 3 . .
    . . . 3 . . . . . . . . . 3 . .
    . . . 3 . . . . . . . . . 3 . .
    . . . 3 . . . . . . . . . 3 . .
    . . . 3 . . . . . . . . . 3 . .
    . . . 3 . . . . . . . . . 3 . .
    . . . 3 . . . . . . . . . 3 . .
    . . . 3 . . . . . . . . . 3 . .
    . . . 3 3 3 3 3 3 3 3 3 3 3 . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
`)
let skeleton = sprites.create(img`
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . 1 1 1 1 1 1 1 1 1 1 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 . . . . . . . . . 1 . .
    . . . 1 1 1 1 1 1 1 1 1 1 1 . .
    . . . . . . . . . . . . . . . .
`)
skeleton.setPosition(10, 153)
controller.moveSprite(skeleton, 60, 0)
scene.cameraFollowSprite(skeleton)
scene.setTileMap(img`
    ................f......................f............................
    ................f......................f............................
    ................f......................f............................
    ................f......................f............................
    ................f......................f............................
    ................f......................f............................
    ................f......................f............................
    ................f......................f............................
    ................f......................f..........................4.
    ...............bf......................f..........................4.
    7777777777777777f.....................5f7777777777777777777777777777
    eeeeeeeeeeeeeeeef.......accc.......ccccfeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeef.ccccc......ccccc.....feeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeef......................feeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeef......................feeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeef2222222222222222222222feeeeeeeeeeeeeeeeeeeeeeeeeeee
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
// jumping
let doublejump = true
skeleton.ay = 100
controller.A.onEvent(ControllerButtonEvent.Pressed, function jump() {
    
    if (doublejump) {
        skeleton.vy = -50
        doublejump = skeleton.isHittingTile(CollisionDirection.Bottom)
    }
    
})
game.onUpdate(function on_update() {
    
    if (skeleton.isHittingTile(CollisionDirection.Bottom)) {
        doublejump = true
    }
    
})

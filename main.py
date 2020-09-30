"""
Title: Go Home
Creators: Emily and Jaydah
Description: Skeleton avoids humans trying to get home
"""
scene.set_background_color(9)
human = sprites.create(img("""
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
"""))
skeleton = sprites.create(img("""
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
"""))
skeleton.set_position(10, 153)
controller.move_sprite(skeleton, 60, 0)
scene.camera_follow_sprite(skeleton)
scene.set_tile_map(img("""
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

#jumping
doublejump = True 
skeleton.ay = 100
def jump():
    global doublejump
    if doublejump:
        skeleton.vy = -50
        doublejump = skeleton.is_hitting_tile(CollisionDirection.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, jump)

def on_update():
    global doublejump
    if skeleton.is_hitting_tile(CollisionDirection.BOTTOM):
        doublejump = True
game.on_update(on_update)
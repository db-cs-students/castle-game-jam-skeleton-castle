"""
Title: Go Home
Creators: Emily and Jaydah
Description: Skeleton avoids humans trying to get home
"""
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

"""
def move_sprite_right():
    skeleton.vx = 10
controller.A.on_event(ControllerButtonEvent.PRESSED, move_sprite_right)
"""
import numpy as np


def paint_fill(screen, pixel_color, target_color, pixel_loc):
    if (
        (pixel_loc[0] * pixel_loc[1]) < 0
        or pixel_loc[0] >= screen.shape[0]
        or pixel_loc[1] >= screen.shape[1]
    ):
        return screen

    if screen[pixel_loc] != pixel_color:
        return screen
    else:
        screen[pixel_loc] = target_color
        screen = paint_fill(
            screen, pixel_color, target_color, (pixel_loc[0] - 1, pixel_loc[1])
        )
        screen = paint_fill(
            screen, pixel_color, target_color, (pixel_loc[0] + 1, pixel_loc[1])
        )
        screen = paint_fill(
            screen, pixel_color, target_color, (pixel_loc[0], pixel_loc[1] - 1)
        )
        screen = paint_fill(
            screen, pixel_color, target_color, (pixel_loc[0], pixel_loc[1] + 1)
        )

        return screen


n = 8
screen = np.random.randint(0, 3, size=(n, n))
updated = np.zeros((n, n))
print(screen)

loc = (np.random.randint(0, n), np.random.randint(0, n))
print(loc, screen[loc])
print(paint_fill(screen, pixel_color=screen[loc], target_color=5, pixel_loc=loc))

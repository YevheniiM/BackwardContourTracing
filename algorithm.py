from pixel import Pixel


def process_image(image):
    """
    Transform the 2D array of pixels to 2D array with the
    Pixel objects.

    :param image: actual image
    :return: the 2D array with the Pixel objects

    """
    pixels = image.load()
    my_image = [[] for _ in range(image.size[0])]

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            my_image[i].append(Pixel(i, j, pixels[i, j]))

    return my_image


def find_contour(image, difference=10):
    """
    A function that looks for a picture contour.

    :param image:
    :param difference:
    :return: the contour of the image

    """
    contour = []
    pixels = process_image(image)

    def is_same_color(a, b):
        return abs(a - b) < difference

    bg_color = find_background(pixels)

    def find_neighbour(pix, start_dir, clockwise=True):
        return find_nearest(pixels, pix, start_dir, is_same_color, bg_color, clockwise)

    while True:
        start_pixel = find_start_pixel(pixels, image.size, is_same_color, bg_color)
        if not start_pixel:
            return []
        active = start_pixel
        pixel_cw, _ = find_neighbour(active, 0, clockwise=True)
        pixel_ccw, _ = find_neighbour(active, 0, clockwise=False)
        if pixel_cw != pixel_ccw:
            break
        active.value = bg_color

    end_pixel = start_pixel
    contour.append(end_pixel)
    contour.append(pixel_cw)
    active = pixel_cw

    came_from = 0
    while True:
        pixel, direction = find_neighbour(active, came_from)

        if (not pixel) or (pixel == end_pixel):
            break

        came_from = (direction + 4) % 8
        if pixel not in contour:
            contour.append(pixel)
            active = pixel
        else:
            contour.remove(active)
            active.value = bg_color
            active = contour[-1]

    return contour


def find_nearest(pixels, pix, start_pixel, is_same_color, bg, clockwise):
    """
    A function that seeks the closest neighboring pixel to the given one.

    :param pixels: list
    :param pix: active pixel
    :param start_pixel: Pixel
    :param is_same_color: the function to compare two colors
    :param bg: the color of background
    :param clockwise: bool

    """
    my_range = range(0, 8) if clockwise else range(7, -1, -1)
    for i in my_range:
        p = (start_pixel + 2 + i) % 8
        x = pix.x + Pixel.neighbors.get(p)[0]
        y = pix.y + Pixel.neighbors.get(p)[1]

        try:
            next_pixel = pixels[x][y]
            if not is_same_color(next_pixel.value, bg):
                if is_same_color(pix.value, next_pixel.value):
                    return next_pixel, p
        except:
            continue

    return None, None


def find_background(pixels):
    """
    The function finds background color of the image according to the
    three pixels on the top of it.

    :param pixels: all the pixels in the picture
    :return: (int) - the average color of background

    """
    bg_pixels = pixels[0][0], pixels[0][len(pixels[0]) // 2], pixels[0][len(pixels[0]) - 1]
    return (bg_pixels[0].value + bg_pixels[1].value + bg_pixels[2].value) // 3


def find_start_pixel(pixels, size, is_same, bg):
    """
    The function finds the pixel from which the algorithm
    should start its work.

    :param pixels: all the pixels in the image
    :param size: size of image
    :param is_same: the function which compares two values
     according to the difference
    :param bg: background color
    :return: (Pixel) - the start pixel

    """
    for i in range(size[0]):
        for j in range(size[1]):
            pixel = pixels[i][j]
            if not is_same(pixel.value, bg):
                return pixel

from algorithm import *
from time import time
from PIL import Image, ImageDraw


def print_in_console(image):
    """
    The function prints all the pixel in the image to console.

    :param image: the image to print in console
    :return: None

    """
    size = image.size
    pixels = image.load()

    for i in range(size[0]):
        for j in range(size[1]):
            print(pixels[i, j], end=" " * (4 - len(str(pixels[i, j]))))
        print()


def run_test_for_all_pics():
    """
    The function runs the algorithm for all our test pictures with
    appropriate differences between pixels.

    :return: None

    """
    differences = [120, 90, 60, 90, 10, 60, 10, 79, 150, 15]
    for i in range(1, 11):
        start = time()

        name_of_image = str(i)
        image_path = "./Pictures/{}.jpg".format(name_of_image)
        image_without_contour = Image.open(image_path).convert('L')
        my_contour = find_contour(image_without_contour, difference=differences[i-1])

        xy_contour = []
        for pixel in my_contour:
            xy_contour.append((pixel.x, pixel.y))

        _image = Image.open(image_path)
        pdraw = ImageDraw.Draw(_image)
        pdraw.line(xy_contour, fill='blue', width=2)

        print("The {0} picture takes {1} to be processed".format(i, time() - start))


def main():
    """
    The main function that represents the work of the backward contour algorithm.
    :return: None

    """
    run_test_for_all_pics()


if __name__ == '__main__':
    main()

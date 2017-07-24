from skimage import color
from skimage.filters import roberts
from skimage.io import imread, imsave
from skimage.transform import swirl


def apply_edge_filter(file_name):
    image = imread(file_name, as_grey=True)
    edge_roberts = roberts(image)

    imsave(file_name, edge_roberts)

    return file_name


def apply_red_tint_filter(file_name):
    image = imread(file_name, as_grey=True)

    rgb_image = color.gray2rgb(image)

    red_multiplier = [1, 0, 0]

    imsave(file_name, red_multiplier * rgb_image)

    return file_name


def apply_swirl_filter(file_name):
    image = imread(file_name, as_grey=True)

    swirled_image = swirl(image, rotation=0, strength=10, radius=120)

    imsave(file_name, swirled_image)

    return file_name

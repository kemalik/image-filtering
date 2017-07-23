from skimage.filters import roberts
from skimage.io import imread, imsave


def apply_edge_filter(file_name):
    image = imread(file_name, as_grey=True)
    edge_roberts = roberts(image)

    imsave(file_name, edge_roberts)

    return file_name

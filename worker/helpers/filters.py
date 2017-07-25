from skimage import color
from skimage.filters import roberts
from skimage.io import imread, imsave
from skimage.transform import swirl

from helpers.constants import FILE_EXTENSION_SIZE


class FilterApply(object):
    def __init__(self, file_path, filter_type) -> None:
        self.file_path = file_path
        self.filter_type = filter_type
        self.filtered_image = None

        self.result_file_path = file_path[:FILE_EXTENSION_SIZE] + '_filtered' + file_path[FILE_EXTENSION_SIZE:]
        self.image = None

    def save_image(self):
        imsave(self.result_file_path, self.filtered_image)

    def read_image(self):
        self.image = imread(self.file_path, as_grey=True)

    def apply_filter(self):
        self.read_image()

        if self.filter_type == 'edge':
            self.filtered_image = roberts(self.image)

        elif self.filter_type == 'red_tint':
            rgb_image = color.gray2rgb(self.image)
            red_multiplier = [1, 0, 0]
            self.filtered_image = red_multiplier * rgb_image

        elif self.filter_type == 'swirl':
            self.filtered_image = swirl(self.image, rotation=0, strength=10, radius=120)

        else:
            return None

        self.save_image()
        return self.result_file_path

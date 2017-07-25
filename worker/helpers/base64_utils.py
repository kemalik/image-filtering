import base64

from helpers.constants import BASE64_FILE_EXTENSION


class Base64Util(object):
    def __init__(self, base_64_text) -> None:
        self.base_64_text = base_64_text

    def clear_base64(self, base64_img):
        return base64_img.split('base64,')[-1].replace(' ', '+')

    def convert_image_to_base64(self, file_path):
        with open(file_path, 'rb') as f:
            code = base64.b64encode(f.read())

            return '{extension},{code}'.format(code=code.decode('utf8'), extension=BASE64_FILE_EXTENSION)

    def decode_base64(self):
        cleaned_base64_image = self.clear_base64(self.base_64_text)

        return base64.b64decode(cleaned_base64_image)

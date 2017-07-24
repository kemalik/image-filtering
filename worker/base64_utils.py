import base64


def clear_base64(base64_img):
    return base64_img.split('base64,')[-1].replace(' ', '+')


def convert_to_base64(image):
    with open(image, 'rb') as f:
        code = base64.b64encode(f.read())
        return 'data:image/png;base64,{code}'.format(code=code.decode('utf8'))
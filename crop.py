from PIL import Image

def crop_captcha(image_path):
    # 画像をロード
    img = Image.open(image_path)
    
    # この値は画像によって調整する必要があります。
    # 左上のx座標、左上のy座標、右下のx座標、右下のy座標
    captcha_box = (200, 1160, 863, 1720)  # これは例です。
    
    # キャプチャ領域を切り出す
    captcha_img = img.crop(captcha_box)
    
    # 切り出した画像を保存
    cropped_path = 'captcha.png'
    captcha_img.save(cropped_path)

    # # Instrauction 箇所を切り出す
    # instruction_box = (250, 1790, 850, 1850)
    # instruction_img = img.crop(instruction_box)
    # instruction_path = 'instruction.png'
    # instruction_img.save(instruction_path)

    # captcha instruction を切り出す
    captcha_instruction_box = (400, 1930, 700, 2000)
    captcha_instruction_img = img.crop(captcha_instruction_box)
    captcha_instruction_path = 'captcha_instruction.png'
    captcha_instruction_img.save(captcha_instruction_path)

    
    return cropped_path


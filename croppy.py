from PIL import Image

def crop(image_path, output_path, x1, y1, x2, y2):
    # 画像をロード
    img = Image.open(image_path)
    

    # 画像をを切り出す
    crop_location = (x1, y1, x2, y2)
    cropped_img = img.crop(crop_location)
    cropped_img.save(output_path)

    # 画像を開く
    img = Image.open(output_path)
    # 画像を表示
    img.show()
    
    return True


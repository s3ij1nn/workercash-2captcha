import cv2
import numpy as np

def check_image_contains(subimage_path, main_image_path):
    # メイン画像とサブ画像を読み込む
    main_img = cv2.imread(main_image_path, cv2.IMREAD_GRAYSCALE)
    sub_img = cv2.imread(subimage_path, cv2.IMREAD_GRAYSCALE)

    # テンプレートマッチングを使用してサブ画像をメイン画像内で探す
    result = cv2.matchTemplate(main_img, sub_img, cv2.TM_CCOEFF_NORMED)
    
    # しきい値の設定
    threshold = 0.8
    loc = np.where(result >= threshold)
    
    # 一致する領域が見つかったかチェック
    if len(loc[0]) > 0:
        # print("Image contains the subimage.")
        return True
    else:
        # print("Image does not contain the subimage.")
        return False



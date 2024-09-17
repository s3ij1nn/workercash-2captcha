from twocaptcha import TwoCaptcha
import os

def solve_captcha(api_key, captcha_image_path, instruction_image_path, instruction_text):
    # 2Captchaのソルバーを初期化
    solver = TwoCaptcha(api_key, defaultTimeout=20, pollingInterval=5, extendedResponse=True)
    
    # キャプチャ画像を読み込む
    try:
        # 2Captcha APIにリクエストを送信し、解答を取得
        result = solver.coordinates(
            captcha_image_path,
            hintImg=instruction_image_path,
            hintText=instruction_text,
            lang='en'
        )
        print("Captcha Solved: ", result)
        return result['code']
    except Exception as e:
        print("Error solving captcha: ", e)
        return None

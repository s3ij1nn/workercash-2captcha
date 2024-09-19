from screenshot import take_screenshot
from is_captcha_displayed import check_image_contains
from crop import crop_captcha
from captcha import solve_captcha
from click import click
import time

# VNCサーバーの情報
vnc_host = '192.168.10.118'  # droidVNCが動作している端末のIPアドレス
vnc_port = 5900  # VNCのポート
vnc_password = 'w'  # VNC接続に必要なパスワード
screenshot_filename = 'screenshot.png'  # 保存するスクリーンショットのファイル名

# 画像パス
subimage_path = 'instruction.png'
next_button = 'next.png'

# captcha Information

api_key = 'YOUR_2CAPTCHA_API_KEY'
captcha_image_path = 'captcha.png'
instruction_image_path = 'captcha_instruction.png'
instruction_text = "Click on the icons in the following sequence"

# 位置情報ベースライン
x = 200
y = 1160

# next button tap time
next_button_tap_time = 0


while True:
    # スクリーンショットを撮る
    take_screenshot(vnc_host, vnc_port, vnc_password, screenshot_filename)

    # 関数を実行
    contains = check_image_contains(subimage_path, screenshot_filename)

    # キャプチャが表示されているかチェック
    if contains:
        print("Captcha is displayed.")

        # キャプチャを切り出す
        cropped_path = crop_captcha(screenshot_filename)

        # キャプチャを解決する
        location = solve_captcha(api_key, captcha_image_path, instruction_image_path, instruction_text)

        # キャプチャ解決に失敗した場合
        if location == None:
            print("Failed to solve captcha.")
            time.sleep(20)
            continue
        
        # location が3つの座標を持っていることを確認
        if len(location) != 3:
            print("Invalid location.")
            time.sleep(20)
            continue

        # クリックする
        for loc in location:
            click_x = x + int(loc['x'])
            click_y = y + int(loc['y'])
            click(vnc_host, vnc_port, vnc_password, click_x, click_y)

        time.sleep(10)

    # Next Button が表示されたまま固まる場合があるため
    # Next Button が表示されたらクリックする
    # 連続タップを行わないようにタップした時刻を記録する
    contains = check_image_contains(next_button, screenshot_filename)
    if contains:
        click_x = 400
        click_y = 2250
        if time.time() - next_button_tap_time > 10:
            click(vnc_host, vnc_port, vnc_password, click_x, click_y)
            next_button_tap_time = time.time()
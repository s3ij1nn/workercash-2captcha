import subprocess

def take_screenshot(vnc_host, vnc_port, vnc_password, screenshot_filename):
    # vncdoコマンドを使用してスクリーンショットを撮る
    command = [
        'vncdo', '-s', f'{vnc_host}::{vnc_port}', '-p', vnc_password, 'capture', screenshot_filename
    ]

    # コマンドを実行
    subprocess.run(command)
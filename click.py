import subprocess

def click(vnc_host, vnc_port, vnc_password, x, y):
    # vncdoコマンドを使用してクリックする
    # 座標 `x`, `y` を文字列に変換してコマンドに含める
    command = [
        'vncdo', '-s', f'{vnc_host}::{vnc_port}', '-p', vnc_password, 'mousemove', str(x), str(y), 'click', '1'
    ]

    # コマンドを実行
    subprocess.run(command, check=True)


"""
〇requierements
pip install pyminizip
〇reference
https://qiita.com/kawa-Kotaro/items/460977f050bf0e2828f2

"""
from datetime import datetime
import pyminizip
import string
import secrets
import os
from pathlib import Path


def generate_password(size: int = 12) -> str:

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # 記号を含める場合
    chars += "%&$|><,+-#():_~^[]*{},;@`"
    return ''.join(secrets.choice(chars) for x in range(size))


def compress_file_with_password(input_file_dir: str, input_fname: str,
                                level: int = 9):
    """
    compress a file with password

    Args:
        target_fname (str): [description]
        output_dir (str): [description]

    Returns:
        [type]: [description]
    """
    password = generate_password()
    # ファイル名から拡張子除去してzipファイルの名前を作成
    output_fname = Path(input_fname).stem+".zip"
    output_fname = os.path.join(input_file_dir, output_fname)

    pyminizip.compress(os.path.join(input_file_dir, input_fname), "\\",
                       output_fname, password, level)

    print(password)
    return password, output_fname

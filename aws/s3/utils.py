import boto3
from typing import Dict
BUCKET="lambda-scraper-test"
#VER_FNAME = "ver.yaml"
DATE_FORMAT="%Y-%m-%d %H:%M:%S"


def load_file_from_s3(s3_path:str)->None:
    """
    s3からファイルを取得して/tmp/以下に保存
    Parameters
    ----------
    s3_path : str
        [description]

    Returns
    -------
    [type]
        [description]
    """    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET)
    file_path=f"/tmp/{s3_path}"
    bucket.download_file(s3_path,file_path)
    return file_path
    
def upload_file_to_s3(local_path:str,s3_path:str)->None:
    """
    local_pathのファイルをs3にupload

    Parameters
    ----------
    local_path : str
        [description]
    s3_path : [type]
        [description]
    """    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET)
    bucket.upload_file(local_path, s3_path)

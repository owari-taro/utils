microsoft_securityアップデートのエクセルファイルを整形するためのコード
# how to use?

## (1)excelファイルを[ダウンロード](https://msrc.microsoft.com/update-guide/ja-jp)

![image](https://github.com/owari-taro/utils/blob/master/miscellaneous/microsoft_security_update/images/screen_shot.png)
![image](https://github.com/owari-taro/utils/blob/master/miscellaneous/microsoft_security_update/images/screen_shot(2).png)
※xlsx形式を選択。(csvとxlsx形式でなぜだか微妙に各セルの値が違うため)

## (2)python実行
ダウンロードしてきたxlsxのパスを↓のようにしてして実行する。
```
pip install openpyxl
#下記を実行するとOUTPUTフォルダに、xlsxの内容を整形したcsvが出力される
python summarize.py {xlsx_fname}
```

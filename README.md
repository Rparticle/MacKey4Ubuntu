# MacKey4Ubuntu

Mac用の英字キーボードでUbuntuを使うためのPythonスクリプトです


moozさんが作成した[xkeysnail](https://qiita.com/mooz@github/items/c5f25f27847333dd0b37)を使用してます。


### xkeysnailインストール

`sudo apt install python3-pip`

`sudo pip3 install xkeysnail`


### 実行方法

`sudo xkeysnail MacKey4Ubuntu.py`


### 内容

普段自分が使ってるキーマップと一致させてます。

Cmd -> Ctrl

Opt -> Super （左だけ）

Caps -> Alt

のリマッピングとCmd単推しで左右が変換、無変換キーが入力されます。

これに


fcitx設定>全体の設定>（右下の拡張オプションの表示）>入力メソッドをオン（オフ）に


でそれぞれ変換、無変換キーを割り当てて英かな設定完了です。


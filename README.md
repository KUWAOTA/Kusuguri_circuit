# くすぐってみ〜な
自分で自分をくすぐっているのにくすぐられるように感じるVR作品「くすぐってみ〜な」の通信部分のコードです。
## 受賞歴
* 国際学生対抗VRコンテスト SEED STAGE進出 (審査付き論文)
* ネットメディア掲載、テレビでの紹介などなど
## Youtube
[![](https://img.youtube.com/vi/OhA2OhtvwsU/0.jpg)](https://www.youtube.com/watch?v=OhA2OhtvwsU)
## NEWS
https://www.itmedia.co.jp/news/articles/2011/05/news067.html
## Article
http://conference.vrsj.org/ac2020/program/doc/3B3-11_PR0114.pdf
## 準備
* 「くすぐってみ〜な」のハードウェア・PCを用意
* tp-link HS105を用意し、wifiに接続
* pythonのインストール
* npmのインストール
* tplink-smarthome-apiのインストール
```
npm install -g tplink-smarthome-api
```
## Usage
### tp-link HS105(4つ)のIPアドレスを以下のコマンドで推定します。
```
tplink-smarthome-api search
```
実行結果は以下のようになります。

```
Searching...
startDiscovery({
  discoveryInterval: 2000,
  discoveryTimeout: 10000,
  breakoutChildren: true,
  broadcast: '255.255.255.255'
})
HS105(JP) plug IOT.SMARTPLUGSWITCH 192.168.179.15 9999 B095757AECFE 8006AAAC62CD28A5A538CED13C09B7F71CDC3939 left_deflate
HS105(JP) plug IOT.SMARTPLUGSWITCH 192.168.179.14 9999 B095757AED08 8006474E14566832C66EE1D6CD56242F1CDC7A88 left_expand
HS105(JP) plug IOT.SMARTPLUGSWITCH 192.168.179.16 9999 B095757AE68A 8006F8CA95EF20C9305A2F9A01FBCD9E1CDC591C right_expand
HS105(JP) plug IOT.SMARTPLUGSWITCH 192.168.179.17 9999 B095757AE4C7 8006B682AF6573229324F6788B2F95D31CDCC961 right_deflate
```
それぞれの名前は以下のように対応しています。
* left_expand:左手側を膨ませる部分のリレー
* left_deflate:右手側を縮ませる部分のリレー
* right_expand:左手側を膨ませる部分のリレー
* right_deflate:右手側を縮ませる部分のリレー
### IPアドレスの反映
`socket-hardware/server.py`の`main`関数を書き換えます。
`Relay_IPs`を以下のように設定しなおします。<br>((left_expand -> left_deflate), (right_expand, right_deflate))の順です。
```
def main():
    Relay_IPs = [['192.168.179.14','192.168.179.15'],['192.168.179.16','192.168.179.17']]
```
### サーバーを立てる
`python socket-hardware/server.py`を実行します。<br>
サーバーを立てておけばPC本体のUnityファイルを実行すればデバイスが映像に合わせて動きます。

## ディレクトリ説明
### socket-hardware
担当者:宇野<br>
スマートプラグに電源on-off信号を送る部分です。<br>
Unityからくすぐり開始信号を受け取けとるためにサーバーを立ててます。
### ??
担当者:福田
## 企業の方向け
### 宇野の役割
ハードウェアの設計・PCとの通信
### 技術的な工夫
自分で自分をくすぐれない理由は、自分の手の動きだと、肌に伝わる刺激を脳が推測してしまうからです。この推測を崩すハードウェアシステムにしました。
色んなデバイスを作っては試したり、くすぐりボイスを採用したりしてなんとか実現しました。
最終的には、デバイスをランダムに膨らんだり縮んだりさせて、本来くすぐられる皮膚の位置や力を変更し、くすぐったさを実現しました。
## Author 
* 作成者:宇野, 福田
* 所属:奈良先端科学技術大学 先端科学技術研究科 先端科学技術領域 サイバネティクスリアリティ工学研究室 <br>(https://carelab.info/ja/about/)
* E-mail
宇野(unosyukatsu@gmail.com)


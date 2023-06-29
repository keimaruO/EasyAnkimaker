# EasyAnkimaker

推しの声で英単語を覚れるように問題を超効率的に作るツールです(現在はホロライブのメンバーのみがフル対応)

Ankiっていう暗記カードアプリとYouTube再生可能にAnkiの拡張機能を利用します

さらにそれをホロメン歴代配信の発話検索使って問題の単語を喋ってるシーンを効率的に探し、問題を効率的に作れるようにしました。

だいたい1問1分ぐらい？のペースで作れます



# 導入方法
# Ankiに拡張機能をいれる

まずはじめにAnkiの拡張機能を入れてもらいます
https://ankiweb.net/shared/info/2055492159

導入方法(動画)
https://www.youtube.com/watch?v=N0dBJWcWZLM
　※15秒のところまででOK
 
動画は英語ですが問題なくいけると思います。

# ブラウザに拡張機能をいれる

次にブラウザの拡張機能をいれてもらいます

[Firefox](https://addons.mozilla.org/en-US/firefox/addon/youtube2anki/)

[Chrome](https://chrome.google.com/webstore/detail/youtube2anki/boebbbjmbikafafhoelhdjeocceddngi)

　※　僕はFifefoxで説明しますがChromeでも拡張機能の起動方法が違う以外は同じようにできるはず


# ブラウザに拡張機能をいれる

無事追加できたらこの[リンク](https://youtu.be/UmkmzlzpEC0)を開いて下さい　※この動画で説明していきます



YouTubeを開いて右下の・・・を押して、字幕を表示させます。　※英語表記なのでShow transcriptってなってます

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/e2651483-49e1-484e-a213-fd6e05ab1acd)

次に、青い時間表記が表示されている場合は右上にある︙を押して非表示にして下さい

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/cfd7fd83-aa4b-4486-8349-2f4025e52b04)

次に拡張機能を起動させます。ブラウザの右上にある拡張機能のパズルのアイコンを押してYouTube2Ankiを起動します

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/8ea09c61-58ab-4a6d-86ba-ab51727eb073)

この画面が出たら、Noneを押してから一番上のをクリックして下さい
次に、下にあるExportを押して下さい

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/c7e5fa46-71e4-4bc0-880e-c939a667e160)

次に、上のSendを押します。するとAnkiに追加されます

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/80f5c796-30fe-4667-977e-ceade503e3a6)

このように追加されてるはずです。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/37340b90-2396-463d-811e-b516bde6fe3f)


クリックして、開始を押すとしっかり機能してるはず

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/d4f4e207-84f4-405e-b38e-a3767d103803)

# 編集する

次に、左下にある編集を押すとこの編集画面になるはず

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/79a52487-88e5-4f35-a0ac-d0ec97654980)

左上のフィールドを押すとこの画面になる

初期はこう

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/91e7a44f-3eb7-4ae3-abc7-79797413a3c4)

編集後はこう

画像と同じになるように削除したり、answerを追加してください。 ※下のオプションは何もいじらなくておｋ

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/5c3ced53-aa40-42d4-91dd-04342d375bde)

同じようにできたら、保存して戻るを押して画像のようになってればOK ※ここで画像と同じようにテキストを追加してください

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/836cd753-b6c6-41f6-b122-6b2721080e94)

次に、左上にあるカードを押して下さい。

表面のテンプレート、裏面のテンプレート、書式をすべて下記のをコピペして上書きしちゃって下さい。


表面のテンプレート

                  <span></span>
                  <br>

                  {{text}}
                  <br>
                  <br>
                  <br>
                  <iframe
                      width="560"
                      height="315"
                      src="https://www.youtube.com/embed/{{id}}?start={{time}}&end={{nextTime}}&autoplay=1"
                      frameborder=0
                        autoplay=1
                  />

                  <br>
                  <span>{{time}} - {{nextTime}}</span>
                  <br>
                  <span></span>


裏面のテンプレート

                  <br>
                  <span></span>
                  {{answer}}
                  <br>
                    

書式


              .card {
                font-family: futura-pt,sans-serif,sans-serif;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: #e9e9e9;
              }

              span {
                font-size: 0.9rem;
                color: #3c3c3c;
              }

            
最終的にこうなってればおｋ

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/b7c98c10-c4af-4a31-8691-fdb6f566c9b2)
![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/ea932fdf-66a9-4978-b4b0-fe1eb0461bd9)
![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/69da11d3-e590-4600-ac18-635423c58d45)



# シーンの探し方
# インストールするもの

[Visual Studio Code](https://miya-system-works.com/blog/detail/vscode-install/)　※インストール方法が書いてあるサイトです

[VScodeの拡張機能](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)　※Visual Studio Codeのインストール後にこの拡張機能を入れておいて下さい。

[Python](https://prog-8.com/docs/python-env-win)　※インストール方法が書いてあるサイトです

[ホロメンの字幕モデル](https://huggingface.co/datasets/keimaru/JP_Holo_Subtitles_Seconds_Format_for_Anki/tree/main/)　※全員分DLしないでおk。推しのやつだけでおｋ



次に、このプロジェクトをわかりやすいとこにダウンロードします。　※下の画像は現在のページの上部にあります

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/3f85add1-39de-4941-9da0-a5cbee71ebba)

解凍してね☆

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/74c91129-307c-4f71-bc7b-ad8790eae033)

次に、Visual studio codeを起動してフォルダごとドラッグ・アンド・ドロップしてください。

![Animation](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/07aa3a41-e9e6-4c92-bf99-f53041c59032)

次に、先程ダウンロードしてきたフォルダのパス入力欄にcmdと入力してエンターを押します

![Animation](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/14fc297c-38ff-4496-9233-de9f4408690a)

次に、コマンドライン(↑で出した黒い画面)に⬇にあるコマンドを貼り付けて、Enterを押して下さい。インストールが始まりま、数分かかる～

```
pip install -r requirements.txt
```


こんな感じでSuccessfully installedと表示されたらインストールが終わりました。閉じておｋ

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/db254916-28da-46d9-b44e-ced5c2ed0085)


次に、もう一度Visual Studio Codeの画面にもどり、EasyAnkimaker.pyを選択して▷を押します。これで字幕検索アプリが起動します

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/dfab8166-dfd3-4754-997d-8d59e9d579fb)

Browseで先程ダウンロードした推しのモデルを選択します。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/062ff87b-3441-4adb-ad51-409728a783e6)


次に、検索のやり方ですが少し特殊です。下のアプリを改変して作っているからです。少し読めばどうゆう仕組みか分かるはず、多分！

[ホロメンの配信で思い出せそうで思い出せないシーンを自分が覚えてる単語を複数個入力すればその該当シーンがでてくる確率がぐーんと上がるプログラム](https://github.com/keimaruO/YTSceneSearch)


ま、基本は３つ同じ単語を入れて検索すれば求めているシーン出るはず。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/0dc8c9cf-e5e9-42ea-bfcd-666337fc5a3a)

単語によってはめっちゃ検索結果がたくさん出ると思います。

```
より結果を絞りたい場合はより求めている状況の単語をいれるというのでしょうか、、表現が難しいのですが、、、

例がムズイですが、仮に、「牛乳」と嬉しそ発言しているシーンがほしいとします。

キーワード1 牛乳
キーワード2 美味しい
キーワード3 風呂

これで、[風呂]に関係する話を前後でしていてかつ、[牛乳]の発言していて、[美味しい]と言っているシーンがでる確率があがります。※でない場合もある

これにより、もしスパチャ読みなどで[牛乳]っていう名前の人がいてもそのシーンは除外される確率があがり

ゲーム内で牛乳になにか悲しい出来事があった場合(?)に除外できるはず。悲しい時に美味しいとは言わないはず。ｼﾗﾝｹﾄﾞ (´･ω･｀)



簡単な仕組みを説明すると

YouTubeの自動字幕をすべて結合してあるファイルがあります。
⬇
そこでキーワード1を入力して検索する。
⬇
もちろんそのキーワード1がある場合はヒットしますよね？
⬇
そのヒットした単語を中心として上下数十行の範囲をキーワード2で検索する
```

<sub>もっかい書きますが、１つ前に貼ったURL(ホロメンの配信で思い出せそうで思い出せない...のやつ)をみるともうちょい仕組みわかって理解深まるかも、コツも書いあるから検索上手になるかも。<sub/>


# Anki用に形式変換

画像のように検索でたとします。3行です。それをコピーします。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/c408a913-5b2f-45bd-80d8-3c307ac1b896)

そしてinput.txtに貼り付けます。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/87d1ff8b-97ec-427e-bce5-eb99196bda2d)

FormatToAnki.pyを選択し実行します。すると一瞬でoutput.txtが更新されるはず

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/a01f03c6-8334-418a-b55a-163607bcbd40)


output.txtを開くとAnkiでインポートできるように形式変換されてます。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/34354533-d687-4f90-9c43-64ee0ab1c23f)


Ankiでインポートのやり方、画像の場所にインポートがあります。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/f41b6392-691b-434e-b3f0-433cfe5102cb)




そして先程変換したoutput.txtを選択します。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/27d5c8a2-97fb-466d-8da3-d45f1b23e17e)

ここでどこに追加するかなどインポートのオプションを調整できます。デッキで選択しところに追加されます～

ま、テストなので何も考えずそのままインポート押しておｋ

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/d1cd8b2b-68ff-4af8-bdf1-99fd795225f0)

これでoutput.txtの内容が追加されて、機能するはず～

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/48235251-7d5e-4082-b2af-2ee46ed88d94)

こんな感じ

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/45d63a11-2037-4461-aa69-77d0d4bd3c64)

で、開始から終了する範囲は100%完璧じゃないと思うので、気になる場合は編集から秒数調整して下さい！　

※ちな秒数形式で再生時間わかりにくいです！ワイも人間が扱いやすい形式にしたかった、youtube仕様みたいでむりだた

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/3fd9c8e0-869c-49ec-b264-9280ac426637)

基本いじるのは上の4つになるはず

問題と答えはどこから持ってくるかは人それぞれ目的違うと思うので、各々勉強にあった問題を参照してほしいです～

もし「英語勉強したい！」ってワイみたいなあんま目的がないけど意欲ある人がいるなら、絶対にコレやるといいよ！ってのはもちろん無いですが

Googleが調査したインターネット上で使われる英単語の頻出単語ランキングってのを利用するのもありっちゃあり。

スラングとかr18とか変なのも多いしウェブの頻出単語順ってのが見てておもろいと感じた

ワイが使ってるやつ載せときます。　https://github.com/keimaruO/EN-JP

答えに関しては

> 　[英辞郎](https://eow.alc.co.jp/search?q=apple)

日本語で書いてる辞書サイト　これAnkiの答えのとこにコピペしたりとか工夫！



> [Thesaurus.com](https://www.thesaurus.com/browse/apple)

類義語見れる英語で書いてあるサイト　関連性持たせて記憶定着させたり



> [Urban Dictionary](https://www.urbandictionary.com/define.php?term=Apple)

Wikipediaみたいに誰でも編集できるサイト　意味わからんアッホみたいなｗ例文見て笑ったり



> [Dictionary.com](https://www.dictionary.com/browse/apple)

英語で書いてある普通の辞書サイト　




> [ちょいデブ親父の英文法](https://choidebu.com/bunpou/jhs1/)

まじでわかりやすく中学英語の文法を説明してるサイト




#　参考、元になったやつ


https://blog.boxofmanga.com/youtube-subtitles-into-anki-flashcards/

ホロ字幕検索アプリ　https://github.com/keimaruO/YTSceneSearch　※ま、これワイなんやけども、、

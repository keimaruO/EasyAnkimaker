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
　※　15秒のところまででOK
 
動画は英語ですが問題なくいけると思います。

# ブラウザに拡張機能をいれる

次にブラウザの拡張機能をいれてもらいます

Firefox https://addons.mozilla.org/en-US/firefox/addon/youtube2anki/

Chrome https://chrome.google.com/webstore/detail/youtube2anki/boebbbjmbikafafhoelhdjeocceddngi

　※　僕はFifefoxで説明しますがChromeでも拡張機能の起動方法が違う以外は同じようにできるはず

# ブラウザに拡張機能をいれる

無事追加できたら https://youtu.be/UmkmzlzpEC0 このリンクを開いて下さい　※この動画で説明していきます



YouTubeを開いて右下の・・・を押して、字幕を表面させます。　※英語表記なのでShow transcriptってなってます

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

# 編集を加える

次に、左下にある編集を押すとこの編集画面になるはず

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/79a52487-88e5-4f35-a0ac-d0ec97654980)

左上のフィールドを押すとこの画面になる

初期はこう

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/91e7a44f-3eb7-4ae3-abc7-79797413a3c4)

編集後はこう

画像と同じになるように削除したり並び替えたりanswerを追加してください。

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
            

# 該当シーンを探し方

インストールするもの

Visual Studio Code https://miya-system-works.com/blog/detail/vscode-install/

※メモ帳みたいなやつ、プログラムを実行するのに必要

このサイトでVisual Studio Codeの拡張機能を入れておいて下さい。

https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner

Python https://prog-8.com/docs/python-env-win

※プログラミング言語。プログラムを動かすのに必要

ホロメンのモデル https://huggingface.co/datasets/keimaru/JP_Holo_Subtitles_Seconds_Format_for_Anki/tree/main/

※全員分DLしないでおk。推しのやつだけでおｋ

次に、このプロジェクトをわかりやすいとこにダウンロードします。　※画像は現在のページの上部の部分です

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/3f85add1-39de-4941-9da0-a5cbee71ebba)

解凍してね☆

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/74c91129-307c-4f71-bc7b-ad8790eae033)

次に、Visual studio codeを起動してフォルダごとドラッグ・アンド・ドロップしてください。

![Animation](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/07aa3a41-e9e6-4c92-bf99-f53041c59032)

次に、先程ダウンロードしてきたフォルダのパス入力欄にcmdと入力してエンターを押します

![Animation](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/14fc297c-38ff-4496-9233-de9f4408690a)

下のをコピーして先程のコマンドラインに貼り付けてエンターを押して下さい。インストールが始まります、数分かかります。

```
pip install -r requirements.txt
```


こんな感じでSuccessfully installedと表示されたらインストールが終わりました。もう閉じておｋ

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/db254916-28da-46d9-b44e-ced5c2ed0085)


次に、もう一度Visual Studio Codeの画面にもどり、EasyAnkimaker.pyを選択して▷を押します。これで字幕検索アプリが起動します

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/dfab8166-dfd3-4754-997d-8d59e9d579fb)

Browseで先程ダウンロードした推しのモデルを選択します。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/062ff87b-3441-4adb-ad51-409728a783e6)

次に、検索のやり方ですが少し特殊です。下のを改変して作っているからです。少し読めばどうゆう仕組みか分かるはず、多分！

<sub>ホロメンの配信で思い出せそうで思い出せないシーンを自分が覚えてる単語を複数個入力すればその該当シーンがでてくる確率がぐーんと上がるプログラム</sub>

https://github.com/keimaruO/YTSceneSearch

ま、基本的に３つの同じ単語を入れて検索すれば求めているシーン出るはず。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/0dc8c9cf-e5e9-42ea-bfcd-666337fc5a3a)

単語によってはめっちゃ検索結果がたくさん出ると思います。絞りたい場合はより求めている状況の単語をいれるというのでしょうか、、表現が難しいのですが、簡単な仕組みとしては、YouTubeの自動字幕をすべて結合して、なにかワード検索を検索します。するともちろんそのワードがある場合はヒットしますよね？そのヒットした単語から一定の範囲を条件内でもう1つのワードを検索をする仕組みです。

１つ前に貼ったURL(ホロメンの配信で思い出せそうで思い出せない...のやつ)をみるとちょい仕組みわかって、コツも書いあるから検索上手になるかも。

# Anki用に形式変換

画像のように検索でたとします。3行です。それをコピーします。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/c408a913-5b2f-45bd-80d8-3c307ac1b896)

そしてinput.txtに貼り付けます。

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/87d1ff8b-97ec-427e-bce5-eb99196bda2d)

FormatToAnki.pyを実行します

![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/a01f03c6-8334-418a-b55a-163607bcbd40)





このサイトはAnki内でYouTube再生するための拡張機能の導入方法を説明しているサイトです。
https://blog.boxofmanga.com/youtube-subtitles-into-anki-flashcards/



https://github.com/keimaruO/YTSceneSearch この字幕検索アプリを応用してAnki用に効率的にアプリを作り替えました。

参考にしたサイト　すげー助かった
https://blog.boxofmanga.com/youtube-subtitles-into-anki-flashcards/

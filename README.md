![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/40d11228-aeb7-47d4-877d-f35b5eedea69)# EasyAnkimaker

推しの声で英単語を覚れるように問題を超効率的に作るツールです(現在はホロライブのメンバーのみ)

Ankiっていう暗記カードアプリとYouTube再生可能にAnkiの拡張機能を利用します

さらにそれをホロメン歴代配信の発話検索使って問題の単語を喋ってるシーンを効率的に探して、問題を効率的に作れるようにしました。1問1分ぐらい？



# 導入方法

このサイトはAnki内でYouTube再生するための拡張機能の導入方法を説明しているサイトです。
https://blog.boxofmanga.com/youtube-subtitles-into-anki-flashcards/

サイト内に拡張機能のリンクがあるのですが、探すのめんどいと思うので直接リンク貼っておきます
https://ankiweb.net/shared/info/2055492159

導入方法　(動画)
https://www.youtube.com/watch?v=N0dBJWcWZLM

解説動画は


Ankiに特化した変換済みsrtモデル https://huggingface.co/datasets/keimaru/JP_Holo_Subtitles_Seconds_Format_for_Anki/tree/main


https://github.com/keimaruO/YTSceneSearch この字幕検索アプリを応用してAnki用に効率的にアプリを作り替えました。

参考にしたサイト　すげー助かった
https://blog.boxofmanga.com/youtube-subtitles-into-anki-flashcards/

最終的にこうなればOKです
![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/597463e2-065d-4e16-8582-b716b465ce0b)
![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/3f5f9da8-ab67-4aec-8f8b-fa6ccd439785)
![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/24be1d1b-ed1d-4d90-b9e4-187c85753947)
![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/8521b513-873f-4302-be0f-66deabe1e1b5)
![image](https://github.com/keimaruO/EasyAnkimaker/assets/91080250/db7d16ba-d779-4bc5-be14-798d8348d0d3)


表面のテンプレート
                  <span></span>
                  <br>

                  {{question}}
                  <br>
                  <br>
                  <br>
                  <iframe
                      width="560"
                      height="315"
                      src="https://www.youtube.com/embed/{{id}}?start={{start}}&end={{end}}&autoplay=1"
                      frameborder=0
                        autoplay=1
                  />

                  <br>
                  <span>{{start}} - {{end}}</span>
                  <br>
                  <span></span>


裏面のテンプレート

                      {{FrontSide}}
                      <hr id=answer>
                    

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

                    

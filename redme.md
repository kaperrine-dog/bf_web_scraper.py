# BeautifulSoap Web調査ツール

# <span style="color: red; ">注意事項</span>

>Webスクレイピングの注意事項
>- [Webスクレイピングの注意事項一覧](https://qiita.com/nezuq/items/c5e827e1827e7cb29011)
>- [岡崎市立中央図書館事件](https://ja.wikipedia.org/wiki/%E5%B2%A1%E5%B4%8E%E5%B8%82%E7%AB%8B%E4%B8%AD%E5%A4%AE%E5%9B%B3%E6%9B%B8%E9%A4%A8%E4%BA%8B%E4%BB%B6)

スクレイピング自体は基本的には問題ありませんが、ターゲットサイトの利用規約で禁止されている場合や、高頻度でツールを使用し、サーバーに高負荷をかけた場合には罪に問われる可能性もありますのでご注意ください。

尚、本リポジトリはTor経由でのスクレイピングを推奨するものではありません。

## Torとは?

- [Tor.org](https://www.torproject.org/)

>[Tor - Wikipedia](https://ja.wikipedia.org/wiki/Tor)より
>Tor（トーア、英語: The Onion Router）とは、TCP/IPにおける接続経路の匿名化を実現するための規格、及びそのリファレンス実装であるソフトウェアの名称である。通常、ユーザはローカルにSOCKSプロキシ（オニオンプロキシ）を立て、そのプロキシ経由で通信を行うことになる。Torという名称はオリジナルのソフトウェア開発プロジェクトの名称である「The Onion Router」の頭文字を取ったものである。
>

簡単に説明すると、`Onion Routing`という技術を使って接続経路を秘匿化する技術です。玉ねぎの皮のように接続ノードを積み重ねていることが名前の由来らしいです。

# 使い方

1. 前提として`docker desktop`などの`docker`実行環境が必要です。

2. 任意のディレクトリに移動して`git clone`

3. テキストエディタで`scraper.py`を開いて`base_url`の部分にターゲットのURLを入力

下記実行

```bash:title=docker-compose
$ `docker-compose up -d`
```

キャッシュがない場合は自動でビルドが始まり、終わると取得が始まります。

4. 保存ディレクトリ
  下記ディレクトリに保存されます。
  `python/site-data/URL/...`

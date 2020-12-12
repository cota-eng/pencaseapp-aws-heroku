## アプリケーションの概要
文房具好きが集まって、自分の筆箱を写真・説明とともに載せ、共有することができるアプリケーション。

## アプリケーションの機能一覧
主に以下の通りである。

- メール認証によるサインアップ
- ログイン・ログアウト・パスワード再設定
- 記事投稿（ログインユーザーのみ）
- 記事閲覧（すべてのユーザー）
- 記事編集（投稿者のみの権限）
- 記事削除（投稿者のみの権限）
- 投稿に対するいいね機能（ログインユーザーのみ）
- 投稿に対するコメント機能（ログインユーザーのみ）
- 投稿に対するコメントの返信機能（ログインユーザーのみ）
- 公式ブログ (管理者の管理)
- マークダウン投稿（管理者の管理）
- 人気順での並び替え
- 新着順での並び替え
- ページネーション


## アプリケーション内で使用している技術一覧
- Django(Python)
- Bootstrap4(material design & responsive)
- AWS S3(static and media file are uploaded)
- Heroku(Paas)
- PostgresSQL(Heroku)
- Twitter Card
- pip(runtime.txt)
画像アップロード　pillow Imagekit　
ログイン django-allauth

## デプロイ
herokuを用いた。独自ドメインは取得していない。
静的ファイルと、投稿によりアップロードされるメディアファイルをAWSのS3に保管する。画像のキャッシュは2日としている。他のデータについては、herokuのPostgreSQLを用いている。
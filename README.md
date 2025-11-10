# tech-blog

技術ブログのリポジトリ

# 手順

[クイックスタート](https://gohugo.io/getting-started/quick-start/)にしたがってやる

```shell
cd site
# siteディレクトリにhugoの雛形を作成
hugo new site site
```

テーマを設定

- [このテーマ](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation)にする
- [ここ](https://themes.gohugo.io/tags/blog/)から選べる
- サンプルサイトは[ここ](https://adityatelange.github.io/hugo-PaperMod/)
- サンプルサイトのソースコードは[ここ](https://github.com/adityatelange/hugo-PaperMod/tree/exampleSite)

favicon を設定

- [icons8](https://icons8.jp/icons/set/favicon-%E3%83%97%E3%83%AA%E3%83%B3)で探す
- 「コピー」で URL をコピーできるので、それを hugo.yaml に記入する

# 記事作成手順

```shell
cd site
# ファイル作成
hugo new content content/posts/my-first-post.md
# ローカルで記事を確認
hugo server --buildDrafts --bind 127.0.0.1 --baseURL http://localhost
```

# テンプレート編集

`site/archetypes/default.md`を編集

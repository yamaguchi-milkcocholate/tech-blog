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

# 記事作成手順

```shell
cd site
# ファイル作成
hugo new content content/posts/my-first-post.md
```

# テンプレート編集

`site/archetypes/default.md`を編集

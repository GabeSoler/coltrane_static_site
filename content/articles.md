---
title: Article index
description: To direct to articles
template: coltrane/content.html
publish_date: 2024-07-24 19:26:02
---

{% directory_contents 'articles' as articles %}

{% for article in articles %}

[{{article.title}}](/{{article.slug}}/)

{% endfor %}

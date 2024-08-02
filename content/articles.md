---
title: Articles
description: To direct to articles
template: coltrane/content.html
publish_date: 2024-07-24 19:26:02
---

# Articles

Here you can find some reflections I wrote for this site, and also references to other works that are in different journals and books. 

### Areas of work:

{% directory_contents 'areas' order_by='order' as areas %}

{% for area in areas %}

- [{{area.title|title}}](/{{area.slug}}/)

{% endfor %}

### Reflections about my published work

{% directory_contents 'articles' order_by='order' as articles %}

{% for article in articles %}

- [{{article.title|title}}](/{{article.slug}}/)

{% endfor %}

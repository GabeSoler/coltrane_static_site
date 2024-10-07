---
title: Areas of Work
description: Describe my main areas of work
template: coltrane/group_nav.html
publish_date: 2024-07-24 19:26:02
---


### Areas of work:

{% directory_contents 'areas' order_by='order' as areas %}

{% for area in areas %}

- [{{area.title|title}}](/{{area.slug}}/)

{% endfor %}

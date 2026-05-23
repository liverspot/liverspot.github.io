---
layout: page
title: Authors
---

{% for person in site.authors %}

* <a href="{{ site.baseurl }}{{ person.url }}">{{ person.name }}</a>

{% endfor %}

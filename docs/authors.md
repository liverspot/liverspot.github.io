---
layout: page
title: Authors
permalink: /authors/
---

{% for person in site.authors -%}
* <a href="{{ site.baseurl }}{{ person.url }}">{{ person.name }}</a>
{% endfor %}

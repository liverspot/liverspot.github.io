---
layout: page
title: Authors
permalink: /authors/
styles:
  - shiftRight1
  - tableLayoutFixed1
  - tableGrid1
---

<style>
 

</style>


{% capture my_text -%}

{% assign source_count = 0 -%}
{% assign sources = site.authors | sort_natural: "full-name" -%}
|&nbsp;|&nbsp;|&nbsp;|
|--------|--------|--------|
{% for source in sources -%}
{% assign source_modulo = source_count | modulo: 3 -%}
{% if source_modulo == 0 -%}
{% assign left_source = source -%}
{% elsif  source_modulo == 1 -%}
{% assign middle_source = source -%}
{% else  -%}
{% assign right_source = source -%}
| <span style="float: right; "> [&darr;](#{{ left_source.id | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ left_source.url }}">{{left_source.name}}</a> | <span style="float: right; "> [&darr;](#{{ middle_source.id  | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ middle_source.url }}">{{middle_source.name}}</a> | <span style="float: right; "> [&darr;](#{{ right_source.id | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ right_source.url }}">{{right_source.name}}</a> |
{% endif -%}
{% assign source_count = source_count | plus: 1 -%}
{% endfor -%}
{% if source_modulo == 0 -%}
| <span style="float: right; "> [&darr;](#{{ left_source.id | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ left_source.url }}">{{left_source.name}}</a> |  |   |
{% elsif  source_modulo == 1 -%}
| <span style="float: right; "> [&darr;](#{{ left_source.id | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ left_source.url }}">{{left_source.name}}</a> | <span style="float: right; "> [&darr;](#{{ middle_source.id  | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ middle_source.url }}">{{middle_source.name}}</a> |  |
{% else  -%}
{% endif -%}
|========|========|========|
|&nbsp;|&nbsp;|&nbsp;|
{% endcapture -%}
{{ my_text | markdownify }}

<h2>Excerpts</h2>

{% capture my_text %}
{% for source in sources -%}
{% assign full_id = source.id | remove_first: '/' | replace: '/', '-' -%}
<span class='topic-arrow' ><a href="{{ site.baseurl }}{{ source.url }}">&rarr;</a></span>
<h3 id="{{full_id}}"><a href="{{ site.baseurl }}{{ source.url }}">{{source.name}}</a></h3>

{{source.excerpt }} 



{% endfor -%}

{% endcapture %}
{{ my_text | markdownify }}
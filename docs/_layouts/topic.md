---
layout: default
---
<h1>{{ page.name }}</h1>

{{ content }}

<p>Topic Entry: <a href="{{ site.baseurl }}/topics#{{page.slug}}">{{ page.name }}</a>
</p>


<h2>Stories</h2>

{% assign filtered_posts = site.posts | where_exp: "item", "item.tags contains page.slug" %}

<ul>
{% for post in filtered_posts -%}
<li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
---
layout: default
---
<style>

  a {
    overflow-wrap: break-word; 
  }


h3 {
  margin-top: 20px;
  border-top: 2px solid #2e6da4; 
  color: #2e6da4;
  break-after: avoid;
  page-break-after: avoid; /* Safari fallback */
}

h4 {
  color: #b81d3e;
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 18px;
  font-weight: 600;
  line-height: 24px;
}

h5 {
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 20px;
  font-weight: 500;
  line-height: 34px;
}

h6 {
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 16px;
  font-weight: 500;
  line-height: 28px;
}


</style>
<h1>{{ page.name }}</h1>

{{ content }}

<p>Topic Entry: <a href="{{ site.baseurl }}/topics#{{page.slug}}">{{ page.name }}</a>
</p>


<h3>Stories</h3>

{% assign filtered_posts = site.posts | where_exp: "item", "item.tags contains page.slug" %}

<ul>
{% for post in filtered_posts -%}
<li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
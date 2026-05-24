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

<h3>Stories</h3>

<ul>
{% for post in site.posts %}
{% if post.author == page.name %}
<li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
{% endif %}
{% endfor %}
</ul>

---
layout: page
title: Stories
---

<style>
  a {
    overflow-wrap: break-word; 
  }

h3 {
  border-top: 2px solid #2e6da4; 
  color: #2e6da4;
  break-after: avoid;
  page-break-after: avoid; /* Safari fallback */
}

  p, h4 { /*Shift contents of details right*/
    margin-left: 20px; 
  } 
  ul { 
    padding-inline-start: 20px; 
  }

table td, th {
    padding: 2px 15px; /* Or a small value like 2px */
}

</style>

| Story | Date  | Author |
|-------|-------|--------|
{% for post in site.posts -%}
{% assign full_id = post.id | remove_first: '/' | replace: '/', '-' -%}
{% assign author_name = 'Unknown' -%}
{% for person in site.authors -%}
{% if person.name == post.author -%}
{% assign author_name = person.name -%}
{% assign author_url = person.url -%}
{% endif -%}
{% endfor -%}
| [{{post.title}}]({{site.baseurl }}{{ post.url }}) &nbsp;  <span style="float: right; "> [&darr;](#{{full_id}})  </span> | {{post.date | date: "%Y-%m-%d" }} | [{{author_name}}]({{author_url}}) |
{% endfor -%}
|----|----|----|


{% for post in site.posts -%}
{% assign full_id = post.id | remove_first: '/' | replace: '/', '-' -%}
<div style="float:right"><a href="{{ site.baseurl }}{{ post.url }}">[More...]</a></div>
<h3 id="{{full_id}}">{{post.title}}</h3>

{{post.excerpt}} 
{% endfor -%}

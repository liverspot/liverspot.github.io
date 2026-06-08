---
layout: default
styles:
  - standard1
---
<style>


table td, th {
    padding: 2px 15px; /* Or a small value like 2px */
    vertical-align: top;
}


  p, h4 { /*Shift contents of details right*/
    margin-left: 20px; 
  } 
  ul { 
    padding-inline-start: 20px; 
  }

</style>

<h1>{{ page.name }}</h1>

{{ content }}

<h2>Stories</h2>
{% assign filtered_posts = site.posts | where_exp: "item", "item.author == page.name" %}

{% include story_list.html posts=filtered_posts %}

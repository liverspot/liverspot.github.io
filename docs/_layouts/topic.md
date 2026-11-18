---
layout: default
styles:
  - standard1
  - standard2
---
<style>



  p, h4 { /*Shift contents of details right*/
    margin-left: 20px; 
  }

</style>
<h1>{{ page.name }}</h1>

{{ content }}

<p><i>Topics Entry Link:</i> <a href="{{ site.baseurl }}/topics#{{page.slug}}">{{ page.name }}</a>
</p>

{% assign filtered_posts = site.posts | where_exp: "item", "item.tags contains page.slug" %}


{% include story_list.html posts=filtered_posts %}

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

<span class='topics-arrow' ><a href="{{ site.baseurl }}/topics#{{page.slug}}">&rarr; Topics</a></span>
<h1>{{ page.name }}</h1>

{{ content }}

{% assign filtered_posts = site.posts | where_exp: "item", "item.tags contains page.slug" %}

{% include story_list.html posts=filtered_posts %}

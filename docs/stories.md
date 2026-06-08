---
layout: page
title: Stories
permalink: /stories/
---

<style>

  table th {
    background-color: #2e6da4;
    color: white;
  }

  p, h4 { /*Shift contents of details right*/
    margin-left: 20px; 
  } 


</style>


{% assign filtered_posts = site.posts  %}
{% include story_list.html posts=filtered_posts %}


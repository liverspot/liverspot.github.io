---
layout: page
title: Stories
---

<style>
    .topic-arrow {
        float:right; 
        border-top: 2px solid #2e6da4;
        font-size:20px; 
        font-weight: bold;
        font-weight:700; 
        color: #2e6da4;
        background-color: #deedf4;
    }

a {
    overflow-wrap: break-word; 
  }

h2x {
    background-color: #deedf4;
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


{% assign filtered_posts = site.posts  %}
{% include story_list.html posts=filtered_posts %}


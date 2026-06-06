---
layout: page
title: Sources
permalink: /sources/
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

The following organizations have materials that are referenced within [Topics](/topics/). 

{% capture my_text %}
{% for source in site.sources -%}
{% assign full_id = source.id | remove_first: '/' | replace: '/', '-' -%}
<span class='topic-arrow' ><a href="{{ site.baseurl }}{{ source.url }}">&rarr;</a></span>
{% assign check_length = source.short-name.size -%}
{% assign check_short = source.name | slice: 0, check_length -%}
{% if check_short == source.short-name %}
<h3 id="{{full_id}}"><a href="{{ site.baseurl }}{{ source.url }}">{{source.name}}</a></h3>
{% else %}
<h3 id="{{full_id}}"><a href="{{ site.baseurl }}{{ source.url }}">{{ source.short-name }}: {{ source.name }}</a></h3>
{% endif %}

{{source.excerpt}}

{% assign filtered_citations = site.data.citations | where_exp: "item", "item.source == source.slug" -%}
{% assign citations_count = filtered_citations | size  -%}
{% assign citations_last = filtered_citations | size | minus: 1 -%}
{% assign first_citation = filtered_citations[0] -%}
{% assign last_citation = filtered_citations[citations_last] -%}
{% assign topic_name = "" -%}

{% if citations_count > 1 %}
There are a total of {{citations_count}} citations in topics from [{{first_citation.topic-name}}]({{first_citation.path}})  to  [{{last_citation.topic-name}}]({{last_citation.path}})
{% else %}
There is one citation in [{{first_citation.topic-name}}]({{first_citation.path}})
{% endif %}

{% endfor -%}

{% endcapture %}
{{ my_text | markdownify }}
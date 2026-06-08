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
    vertical-align: top;
}

table {
  table-layout: fixed;
  width: 100%; 
  border-collapse: collapse;
}


</style>

The following organizations have materials that are referenced within [Topics](/topics/). 

{% capture my_text -%}

{% assign source_count = 0 -%}
{% assign sources = site.sources | sort_natural: "full-name" -%}
|--------|--------|
{% for source in sources -%}
{% assign source_modulo = source_count | modulo: 3 -%}
{% if source_modulo == 0 -%}
{% assign left_source = source -%}
{% elsif  source_modulo == 1 -%}
{% assign middle_source = source -%}
{% else  -%}
{% assign right_source = source -%}
| <span style="float: right; "> [&darr;](#{{ left_source.id | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ left_source.url }}">{{left_source.full-name}}</a> | <span style="float: right; "> [&darr;](#{{ middle_source.id  | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ middle_source.url }}">{{middle_source.full-name}}</a> | <span style="float: right; "> [&darr;](#{{ right_source.id | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ right_source.url }}">{{right_source.full-name}}</a> |
{% endif -%}
{% assign source_count = source_count | plus: 1 -%}
{% endfor -%}
{% if source_modulo == 0 -%}
| <span style="float: right; "> [&darr;](#{{ left_source.id | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ left_source.url }}">{{left_source.full-name}}</a> |  |   |
{% elsif  source_modulo == 1 -%}
| <span style="float: right; "> [&darr;](#{{ left_source.id | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ left_source.url }}">{{left_source.full-name}}</a> | <span style="float: right; "> [&darr;](#{{ middle_source.id  | remove_first: '/' | replace: '/', '-' | slugify}})  </span> <a href="{{ site.baseurl }}{{ middle_source.url }}">{{middle_source.full-name}}</a> |  |
{% else  -%}
{% endif -%}

{% endcapture -%}
{{ my_text | markdownify }}

<h2>Excerpts</h2>

{% capture my_text %}
{% for source in sources -%}
{% assign full_id = source.id | remove_first: '/' | replace: '/', '-' -%}
<span class='topic-arrow' ><a href="{{ site.baseurl }}{{ source.url }}">&rarr;</a></span>
<h3 id="{{full_id}}"><a href="{{ site.baseurl }}{{ source.url }}">{{source.full-name}}</a></h3>

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
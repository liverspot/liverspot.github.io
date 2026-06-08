---
layout: default
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

h3 {
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

table td, th {
    padding: 2px 15px; /* Or a small value like 2px */
    vertical-align: top;
}

table {
  table-layout: fixed;
  width: 100%; 
  border-collapse: collapse;
}

  p, h4 { /*Shift contents of details right*/
    margin-left: 20px; 
  } 
  ul { 
    padding-inline-start: 20px; 
  }

</style>

<h1>{{ page.full-name }}</h1>

{{ content }}

{% assign filtered_citations = site.data.citations | where_exp: "item", "item.source == page.slug" -%}
{% assign citations_count = filtered_citations | size  -%}

{% if citations_count > 0 %}
<h2>Citations</h2>

{% assign citations_last = filtered_citations | size | minus: 1 -%}
{% assign first_citation = filtered_citations[0] -%}
{% assign last_citation = filtered_citations[citations_last] -%}
{% assign topic_name = "" -%}

{% capture my_text -%}

[//]: # ({% if citations_count > 1 %})

[//]: # (There are a total of {{citations_count}} citations in topics from [{{first_citation.topic-name}}]&#40;#{{first_citation.topic-slug}}&#41;  to  [{{last_citation.topic-name}}]&#40;#{{last_citation.topic-slug}}&#41;)

[//]: # ({% else %})

[//]: # (There is one citation in [{{first_citation.topic-name}}]&#40;#{{first_citation.topic-slug}}&#41;)

[//]: # ({% endif %})

|--------|--------|--------|
{% assign topic_count = 0 -%}
{% for citation in filtered_citations -%}
{% if topic_name == citation.topic-name -%}
{% continue -%}
{% endif -%}
{% assign topic_name = citation.topic-name -%}
{% assign topic_modulo = topic_count | modulo: 3 -%}
{% if topic_modulo == 0 -%}
{% assign left_citation = citation -%}
{% elsif  topic_modulo == 1 -%}
{% assign middle_citation = citation -%}
{% else  -%}
{% assign right_citation = citation -%}
| <span style="float: right; "> [&darr;](#{{ left_citation.topic-name | replace: "/", "" | slugify}})  </span> <a href="{{ left_citation.path }}">{{left_citation.topic-name}}&nbsp;</a> | <span style="float: right; "> [&darr;](#{{ middle_citation.topic-name | replace: "/", "" | slugify}})  </span> <a href="{{ middle_citation.path }}">{{middle_citation.topic-name}}&nbsp;</a> | <span style="float: right; "> [&darr;](#{{ right_citation.topic-name | replace: "/", "" | slugify}})  </span> <a href="{{ right_citation.path}}">{{right_citation.topic-name}}&nbsp;</a> |
{% endif -%}
{% assign topic_count = topic_count | plus: 1 -%}
{% endfor -%}
{% if topic_modulo == 0 -%}
| <span style="float: right; "> [&darr;](#{{ left_citation.topic-name | replace: "/", "" | slugify}})  </span> <a href="{{ left_citation.path }}">{{left_citation.topic-name}}&nbsp;</a> |  |  |
{% elsif  topic_modulo == 1 -%}
| <span style="float: right; "> [&darr;](#{{ left_citation.topic-name | replace: "/", "" | slugify}})  </span> <a href="{{ left_citation.path }}">{{left_citation.topic-name}}&nbsp;</a> | <span style="float: right; "> [&darr;](#{{ middle_citation.topic-name | replace: "/", "" | slugify}})  </span> <a href="{{ middle_citation.path }}">{{middle_citation.topic-name}}&nbsp;</a> |  |
{% else  -%}
{% endif -%}
{% endcapture -%}
{{ my_text | markdownify }}

{% assign topic_name = "" -%}

{% capture my_text %}

{% for citation in filtered_citations -%}
{% if citation.topic-name != topic_name -%}
{% if "" != topic_name -%}
</ul>
{% endif %}
<span class='topic-arrow' ><a href="{{ citation.path }}">&rarr;</a></span>
### [{{citation.topic-name}}]({{citation.path}})

<ul>
{% assign topic_name = citation.topic-name -%}
{% endif -%}
<li> {% if citation.description != "" -%} {{citation.description}} — {% endif -%}
<a href="{{citation.url}}">{{citation.url}}</a></li>
{% endfor -%}
</ul>


{% endcapture %}
{{ my_text | markdownify }}

{% endif %}
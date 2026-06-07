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
{% assign check_length = page.short-name.size -%}
{% assign check_short = page.name | slice: 0, check_length -%}
{% if check_short == page.short-name %}
<h1>{{ page.name }}</h1>
{% else %}
<h1>{{ page.short-name }}: {{ page.name }}</h1>
{% endif %}

{{ content }}

<h2>Citations</h2>

{% assign filtered_citations = site.data.citations | where_exp: "item", "item.source == page.slug" -%}
{% assign citations_count = filtered_citations | size  -%}
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
{% assign left_topic = topic_name -%}
{% elsif  topic_modulo == 1 -%}
{% assign middle_topic = topic_name -%}
{% else  -%}
{% assign right_topic = topic_name -%}
| <a href="#{{ left_topic | slugify }}">{{left_topic}}&nbsp;</a> | <a href="#{{ middle_topic | slugify }}">{{middle_topic}}&nbsp;</a> | <a href="#{{ right_topic | slugify }}">{{right_topic}}&nbsp;</a> |
{% endif -%}
{% assign topic_count = topic_count | plus: 1 -%}
{% endfor -%}
{% if topic_modulo == 0 -%}
| <a href="#{{ left_topic | slugify }}">{{left_topic}}&nbsp;</a> |  |  |
{% elsif  topic_modulo == 1 -%}
| <a href="#{{ left_topic | slugify }}">{{left_topic}}&nbsp;</a> | <a href="#{{ middle_topic | slugify }}">{{middle_topic}}&nbsp;</a> |  |
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
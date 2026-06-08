---
layout: default
styles:
  - standard1
  - standard2
---

<style>
h1 {
  margin-top: 20px;
  margin-bottom: 15px;
  font-size: 44px;
  font-weight: 400;
  line-height: 62px;
}

h2 {
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 36px;
  font-weight: 400;
  line-height: 50px;
}

 


</style>
<article class="post" itemscope itemtype="http://schema.org/BlogPosting">

  <header class="post-header">
    <h1 class="post-title" itemprop="name headline">{{ page.title | escape }}</h1>
    <p class="post-meta"><time datetime="{{ page.date | date_to_xmlschema }}" itemprop="datePublished">{{ page.date | date: "%b %-d, %Y" }}</time>
    {% if page.author %} • <span itemprop="author" itemscope itemtype="http://schema.org/Person"><span itemprop="name">
    {% for person in site.authors %}
    {% if person.name == page.author %}
    <a href="{{ site.baseurl }}{{ person.url }}">{{ page.author }}</a>
    {% endif %}
    {% endfor %}
    </span></span>
    {% endif %}
    {% if page.tags %}  
    {% for tag in page.tags %}
      • <a href="{{ site.baseurl }}/topic/{{ tag }}">{{ tag }}</a> 
    {% endfor %}
    {% endif %}
    </p>
  </header>

  <div class="post-content" itemprop="articleBody">
    {{ content }}
  </div>

</article>

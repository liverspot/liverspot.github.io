---
layout: page
title: About
permalink: /about/

---

LiverSpot is a community for people with a diseased liver, kidney, lung, heart, or other organ ("OrganSpot") and their caretakers, who want to provide knowledge and support to each other.

## Translation and Terminology

This site is written in American English with medical terminology commonly used in the United States.  The narrative and expository can be translated to other languages with various levels of success through Google Translate (see below) or browser capabilities, but the terminology translation is beyond these tools.   Apologies for any difficulties this cause.

Switch site from
<span class="notranslate">&nbsp;<a onclick="location.href='{{site.url}}{{page.url}}'" class="notranslate">EN</a>&nbsp;</span> 
to:
<span class="notranslate">
&nbsp;{% for item in site.languages -%}
<a onclick="location.href='https://liverspot-org.translate.goog{{page.url}}?_x_tr_sl=auto&_x_tr_tl={{item}}'" class="notranslate">{{item}}</a>
{% if forloop.last -%}
{% else -%}
•
{% endif -%}
{% endfor -%}
</span>

## Ability to Contribute

This site is hosted at GitHub, is built with Jekyll, and is currently deployed on GitHub Pages.  If you want to contribute content directly, just submit a pull request to the [repo](https://github.com/liverspot/liverspot.github.io).  The source files are in '/docs', and you can propose edits to the main 'Topics' page or add independent content to the Story pages.

## History

The concept of supporting organ transplant, pre-transplant, and (hopefully) no-transplant patients came from personal experience in how daunting it is to understand these potentially-terminal diseases and their treatments, and in working with others that are in similar situations.  

Although a patient's medical team is always the primary source of information, their time is limited and it is common for questions to come up outside appointments (with even less medical-team attention).  Further, each patient's team has solely a provider experience (normally) and they may also be limited in knowledge about other approaches.  We believe that by combining the knowledge, experience, and provider-team expertise from multiple patients, a better explanation and understanding can be provided to others.

## Website Updates

Summaries of website updates can be found at:

* <https://www.reddit.com/r/liverspot/?f=flair_name%3A%22LiverSpot%22>

Detailed information is in the [repo](https://github.com/liverspot/liverspot.github.io).
---
title: Shelf
layout: page
permalink: shelf
---

### Books
<ol>
{% for item in site.data.books %}
	{% if item.type == "book" %}
		{% if item.link %}
			<li><a href="{{ item.link }}"><u><b>{{ item.title }}</b></u></a>; <i>{{ item.author }}</i></li>
		{% else %}
			<li><b>{{ item.title }}</b>; <i>{{ item.author }}</i></li>
		{% endif %}
	{% endif %}
{% endfor %}
</ol>


### Articles
<ol>
{% for item in site.data.books %}
	{% if item.type == "article" %}
		<li><a href="{{ item.link }}"><u><b>{{ item.title }}</b></u></a>; <i>{{ item.author }}</i> <span class="span-class-archive">{{ item.tags }}</span></li>
	{% endif %}
{% endfor %}
</ol>
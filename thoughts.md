---
layout: homepage
title: Thoughts
permalink: /thoughts/
---

## Thoughts

<div class="thoughts-timeline">
  {% assign reflections = site.posts | sort: 'date' | reverse %}
  {% for reflection in reflections %}
  <article class="thought-entry">
    <time datetime="{{ reflection.date | date_to_xmlschema }}">{{ reflection.date | date: "%B %-d, %Y" }}</time>
    <div class="thought-entry-content">{{ reflection.content }}</div>
  </article>
  {% else %}
  <p class="thoughts-empty">No reflections yet.</p>
  {% endfor %}
</div>

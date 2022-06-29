
This plugin adds next_article (newer) and prev_article (older) variables to the article's context.

Also adds next_article_in_category and prev_article_in_category.


 <ul>
 {% if article.prev_article %}
     <li>
         <a href="{{ SITEURL }}/{{ article.prev_article.url}}">
             {{ article.prev_article.title }}
         </a>
     </li>
 {% endif %}
 {% if article.next_article %}
     <li>
         <a href="{{ SITEURL }}/{{ article.next_article.url}}">
             {{ article.next_article.title }}
         </a>
     </li>
 {% endif %}
</ul>
<ul>
 {% if article.prev_article_in_category %}
     <li>
         <a href="{{ SITEURL }}/{{ article.prev_article_in_category.url}}">
             {{ article.prev_article_in_category.title }}
         </a>
     </li>
 {% endif %}
 {% if article.next_article_in_category %}
     <li>
         <a href="{{ SITEURL }}/{{ article.next_article_in_category.url}}">
             {{ article.next_article_in_category.title }}
         </a>
     </li>
 {% endif %}
 </ul>

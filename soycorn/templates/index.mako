<%inherit file="/show.mako"/>

<%def name="body()">
${h.literal(c.content)}
<h2>Top News</h2>
<br/>


<br/><a href="news/${c.firstlink[0][0]}"> ${c.firstlink[0][1]}</a><br/>

%for a in c.article:
<br/><a href="news/${a[0]}"> ${a[1]}</a><br/>
%endfor
<br/><br/>
</%def>
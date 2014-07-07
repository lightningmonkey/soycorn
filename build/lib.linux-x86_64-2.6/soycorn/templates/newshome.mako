<%inherit file="/show.mako"/>

<%def name="body()">
<h2>Top News</h2>
<ul>
% for a in c.article:
	%if len(a) < 2:
		</ul>
		<h4>${a[0]}</h4>
		<ul>
	%else:
		<li><a href="news/${a[0]}"> ${a[1]}</a></li>
	%endif
%endfor
</ul>
<br/>
</%def>
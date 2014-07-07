<%inherit file="/show.mako"/>

<%def name="body()">
<div id="photogallery">
<h2>Photo Gallery Page ${c.title}</h2>
<table>
<tr>
<td align="left"><a href=${c.back}><< Back</a></td> <td></td> <td align=right><a href=${c.forward}>Forward >></a></td>
</tr>
%for row in c.range:
<tr>
%for p in row:
<td><a href=/images/${p[0]}.jpg><img width=200 src=/images/${p[0]}sm.jpg></a>${p[1]}</td>
%endfor
</tr>
%endfor
</table>
</div>
</%def>


<%def name="javapics()">

</%def>
<%inherit file="/show.mako"/>

<%def name="body()">
<a href="../News">Back</a><br/>
<h5>${h.literal(c.date)}</h5>
<h3>${h.literal(c.header)}</h3>
${h.literal(c.content)}
</%def>




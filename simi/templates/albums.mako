# -*- coding: utf-8 -*-

${h.stylesheet_link_tag("styles")}
<h1>Pictures</h1>

<ul>
% for a in c.albums:
	<li>
		<a href='view_album?dir=${a.get_url_name().decode("utf-8")}'>${a.get_split_name()[1].decode("utf-8")}</a>
		<small>${a.get_split_name()[0]}</small>
	</li>
% endfor


</ul>


# -*- coding: utf-8 -*-
<html>
 <head>
	<title>Simipics - ${c.title}</title>
	<meta name="viewport" content="width=480;" />
	${h.stylesheet_link_tag("styles")}
	${self.rss_links()}
 </head>

<%def name="rss_links()">
</%def>
<%def name="album_nav()">
</%def>




<h1>${c.title}
% if c.subtitle:
	&nbsp;/&nbsp;<small>${c.subtitle}</small>

% endif
</h1>


% if c.error_message:
	<div class="error">
		${c.error_message}
	</div>

% endif

${self.body()}


${self.album_nav()} 
% if c.show_nav: 
	<div class="albumdata">
		${self.main_nav()} 
		<br/>
		<hr/>
		<a href="albums">Home</a>
	</div>
% endif


<div class="albumdata">
	<%def name="main_nav()">
	</%def>
</div>

</html>

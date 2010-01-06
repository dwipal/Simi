# -*- coding: utf-8 -*-

<meta name="viewport" content="width=480;" />


<%def name="album_nav()">
</%def>

${h.stylesheet_link_tag("styles")}
<title>${c.title}</title>

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


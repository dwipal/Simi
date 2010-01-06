# -*- coding: utf-8 -*-


<%inherit file="/base.mako" />
<link rel="alternate"	type="application/rss+xml" title="simipic: ${c.title}" href="${c.albumdir.get_album_feed_url()}">

<div class="imageview">	
	% for p in c.pics:
	<div class="imageSingle">
		<a href="${p.get_preview_url()}"><img src="${p.get_thumb_url()}"></img></a>
	</div>
	% endfor
</div>


<div class="albumdata">

% if c.sub_albums:
<h2>Sub-albums..</h2>
	% for a in c.sub_albums:
		<li>
			<a href='view_album?dir=${a.get_url_name().decode("utf-8")}'>${a.get_split_name()[1].decode("utf-8")}</a>
			<small>${a.get_split_name()[0]}</small>
		</li>
	% endfor
	<br/>
% endif

</div>

<div class="albumdata">

<a href="${c.albumdir.get_album_zip_url()}">Download full album</a>

</div>


<%def name="main_nav()">
	Back to album: <a href="${c.albumdir.get_album_url()}">${c.albumdir.get_dir_name()}</a>
</%def>

<%def name="rss_links()">
	<link rel="alternate"	type="application/rss+xml" title="Flickr: Your Photostream RSS feed" href="http://api.flickr.com/services/feeds/photos_public.gne?id=54183610@N00&amp;lang=en-us&amp;format=rss_200">
</%def>

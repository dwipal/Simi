# -*- coding: utf-8 -*-

<%inherit file="/base.mako" />
<%namespace name="exif" file="/exif.mako"/>

<%
idx=c.albumcontext.get_browse_index()
l=len(c.albumcontext.get_images())
offset=3
thumbs_rg=range((0,idx-offset)[idx-offset>0], (l,idx+offset+1)[idx+offset+1<l])
%>

<%
i_prev=(idx,idx-1)[idx>0]
i_next=(idx,idx+1)[idx<len(c.albumcontext.get_images())-1]
p_prev=c.albumcontext.get_images()[i_prev]
p_next=c.albumcontext.get_images()[i_next]

%>

<div class="albumdata">
<a href="${p_prev.get_preview_url()}">Prev</a> | 
<a href="${p_next.get_preview_url()}">Next</a>
</div>


<div class="imageview" style="height: 600px;">
	<a href="${p_next.get_preview_url()}">
		<img src="${c.pic.get_image_url()}"></img>
	</a>
</div>

<div class="imageview imagenav">

% for r in thumbs_rg:
<%	p=c.albumcontext.get_images()[r] %>

% if r==idx:
	<<<
% endif
	<a href="${p.get_preview_url()}"><img src="${p.get_thumb_url()}"></img></a>
% if r==idx:
	>>>
% endif
% endfor

</div>


${exif.print_exif()} 
<a href="${c.pic.get_original_image_url()}">Download original image</img></a>

<script type="text/javascript">
	request = new XMLHttpRequest();
	request.open("GET", "${p_next.get_preview_url()}", false);
	request.send(null);
</script>

<script type="text/javascript">
	var hasScrolled=false;
	

	$(window).load(function() {
		$(document).keydown(function(e) {
			if(e.which == 37) {
				parent.location="${p_prev.get_preview_url()}";
			} else if(e.which == 39) {
				parent.location="${p_next.get_preview_url()}";

			} else if(e.which == 38) {
				if(hasScrolled==false) {
					parent.location="${c.albumdir.get_album_url()}";
				}
			}
		});

		$(document).scroll(function(e) {
			self.hasScrolled = true;
		});
	}
	);



</script>

<%def name="album_nav()">
	<hr/>
	Back to album: <a href="${c.albumdir.get_album_url()}">${c.albumdir.get_dir_name()}</a>
</%def>


<%def name="rss_links()">
	<link rel="alternate"	type="application/rss+xml" title="${c.title}" href="${c.albumdir.get_album_feed_url()}">
</%def>

<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:flickr="urn:flickr:" >
	<channel>
		<title>${c.title}</title>
		<link>${c.albumdir.get_album_url()}</link>
		<description>${c.title} ${c.subtitle}</description>
		<pubDate></pubDate>
		<lastBuildDate></lastBuildDate>
		<generator>http://simipic.dyndns.org/</generator>

		%for p in c.pics:

		<item>
			<title></title>
			<link>${p.get_preview_url()}</link>
			<description></description>
			<pubDate>Mon, 31 Aug 2009 00:21:25 -0700</pubDate>
			<media:title></media:title>
			<media:content url="${p.get_image_url()}" type="image/jpeg"/>
			<media:thumbnail url="${p.get_thumb_url()}"/>

		</item>

		%endfor
	</channel>
</rss>





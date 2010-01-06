<%def name="print_exif()">

<script language="javascript">
	function makeVisible(id) {
		document.getElementById(id).style.display='inline';
	}

</script>

<div class="albumdetails">


<%
map=c.pic.get_exif_data_map()
%>

% if map:
Taken with <b>${map.get("Camera model", "")}</b> ( L ${map.get("Focal length", "")} | T ${map.get("Exposure time", "")} | ${map.get("Aperture", "")} | Flash: ${map.get("Flash", "")} | ISO: ${map.get("ISO speed", "")} )  
<a href="javascript:makeVisible('albumdatadetails');" >More..</a>
% else:
EXIF data not available.
%endif


<div style="display: none;" id="albumdatadetails">
<pre>
${c.pic.get_exif_data_dump()}
</pre>
<small>Resize Time: ${c.pic.resize_time}, EXIF Time: ${c.pic.exif_time}, Servlet Time: ${c.total_servlet_time}</small>
<br/>
</div>
</div>

</%def>

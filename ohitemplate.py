from string import Template

ohipage = Template("""<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>Oral History Interview Transcripts in Physics, Astronomy, and Geophysics &mdash; The Niels Bohr Library &amp; Archives at the American Institute of Physics</title>

<link href="nbl.css" rel="stylesheet" type="text/css">

<script type="text/javascript" src="http://www.aip.org/history/nbl/scripts/rollovers.js"></script>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
<script type="text/javascript" src="http://www.aip.org/history/js/jquery.listnav.pack-2.1.js"></script>

<script type="text/javascript">
	$$(function(){
		$$('#ohiList').listnav({
			includeNums: false,
			flagDisabled: true,
			showCounts: false
		});
	});
</script>

<!-- GOOGLE ANALYTICS CODE -->
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-2326461-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>

</head>

<body onload="MM_preloadImages('../nbl/images/button_fb_on.jpg','../nbl/images/button_news_on.jpg')">
<div id="wrapper">

<!--HEADER AREA CONTAINING LOGO-->
<div id="header-library"></div>


<!--HORIZONTAL NAVIGATION AREA-->
<div id="hnav"> 
	<div>
  	<!--#include file="../nbl/includes/hnav.html" -->
  	</div>
</div>



<div id="main"><!--MAIN AREA BELOW HEADER AND HORIZONTAL NAV-->

<!--LEFT NAV-->
	<div id="leftnav">
			<ul>
  <li> <a href="../nbl/index.html">Library Home</a></li>
  <li> <a href="../nbl/about.html">About Us</a></li>
  <li> <a href="../nbl/catalogs.html">Online Catalogs</a></li>
  <li> <a href="../nbl/findingaids.html">Archival Finding Aids</a></li>
  <li> <a href="../nbl/oralhistory.html" class="current">Oral Histories</a></li>
  	<ul id="subnav">
		<li><a href="../nbl/ohiproject.html">About the Project</a></li>
		<li><a href="#nogo" class="subcurrent">Read Transcripts Online</a></li>
		<li><a href="../nbl/ohifeedback.html">Feedback Form</a></li>
	</ul>
  <li> <a href="../nbl/collections.html">Collections</a></li>
  <li> <a href="../nbl/contact.html">Contact Us</a></li>
  <li> <a href="../nbl/sitemap.html">Site Map</a></li>
</ul>

<div>&nbsp;<img src="http://www.aip.org/history/nbl/images/formicon_small.gif" width="17" height="17" alt="Access form link image" style="vertical-align:text-bottom" /> <a href="http://www.aip.org/history/nbl/accessform.html">Access form</a></div>

<a href="http://www.facebook.com/pages/College-Park-MD/Center-for-History-of-PhysicsNiels-Bohr-Library-Archives/9563338557" title="Find us on Facebook!" target="_blank" onmouseover="MM_swapImage('button_fb','','../nbl/images/button_fb_on.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="../nbl/images/button_fb_off.jpg" alt="Button image linking to Facebook fan page" name="button_fb" width="130" height="30" border="0" id="button_fb" /></a>
<a href="http://www.aip.org/history/newsletter/request.html" title="Sign up for our newsletter!" onmouseover="MM_swapImage('button_news','','../nbl/images/button_news_on.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="../nbl/images/button_news_off.jpg" alt="Button image linking to newsletter signup page" name="button_news" width="130" height="30" border="0" id="button_news" /></a>

<!-- AddThis Button BEGIN -->
<script type="text/javascript">var addthis_pub="chpnbl";</script>
<a href="http://www.addthis.com/bookmark.php?v=20" onmouseover="return addthis_open(this, '', '[URL]', '[TITLE]')" onmouseout="addthis_close()" onclick="return addthis_sendto()"><img src="http://s7.addthis.com/static/btn/lg-share-en.gif" width="125" height="16" alt="Bookmark and Share" style="border:0"/></a><script type="text/javascript" src="http://s7.addthis.com/js/200/addthis_widget.js"></script>
<!-- AddThis Button END -->
			
	</div>
<!--END LEFT NAV-->
	
<!--CONTENT AREA NEXT TO LEFT NAV-->	
	<div id="content"> 
    
    <h1>Read Oral History Transcripts Online</h1>
                        <p>This is not a complete list of the oral history interviews held at the Niels Bohr Library &amp; Archives. You can do a comprehensive search of all oral histories, other archival materials, and resources held at other institutions in the <a href="http://www.aip.org/history/icos/">International Catalog of Sources</a>. This list was created on ${date}.</p>
                        
<!-- Google CSE Search Box Begins -->
<form action="/history/ohilist/search_results.html" id="ohisearch">
	
 	<label>Search transcripts</label>
	<input name="q" id="q" type="text" />
	<input type="submit" value="Search" alt="Search" name="sa" id="sa" />
 
</form>
<!-- Google CSE Search Box Ends -->


${body}

                    </div>
<!--END CONTENT AREA NEXT TO LEFT NAV-->


</div><!--END MAIN AREA BELOW HEADER AND HORIZONTAL NAV-->

<!--FOOTER-->
<div id="footer">
	<div>
	<!--#include file="../nbl/includes/footer.html" -->
	</div>
</div>
<!--END FOOTER-->

</div><!--END WRAPPER-->
</body>
</html>""")

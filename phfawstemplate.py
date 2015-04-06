# phfawstemplate.py - Chip Calhoun - used by phfaws.py

from string import Template

browsepage = Template("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
   <head>
      <title>Browse the Physics History Finding Aids</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <link href="nbl.css" rel="stylesheet" type="text/css"/>
      <meta name="keywords" content="Encoded Archival Description, EAD, finding aids, physics history, physics archives, physics manuscripts, Nobel Prize"/>
      <meta name="description" content="Home page for the Physics History Finding Aids, which consists of a group of nine universities and the American Institute of Physics.  Consists of EAD-encoded archival finding aids of famous physicists."/>      <script type="text/JavaScript">
            <!--
            function MM_jumpMenu(targ,selObj,restore){ //v3.0
            eval(targ+".location='"+selObj.options[selObj.selectedIndex].value+"'");
            if (restore) selObj.selectedIndex=0;
            }
            //-->
          </script>
   </head>
   <body>
      <div id="wrapper">

                    <!--HEADER AREA CONTAINING LOGO-->
          <div id="header-findingaids">&nbsp;
          </div>
          <!--HORIZONTAL NAVIGATION AREA-->
          <div id="hnav">
            <div>
               <!--#include virtual="/history/nbl/includes/hnav.html" -->
            </div>
         </div>
         <div id="main">
<!--MAIN AREA BELOW HEADER AND HORIZONTAL NAV-->


<!--LEFT NAV-->
	<div id="leftnav">
			<ul>
  <li><a href="../nbl/index.html">Library Home</a></li>
  <li><a href="../nbl/about.html">About Us</a></li>
  <li><a href="../nbl/catalogs.html">Online Catalogs</a></li>
  <li><a href="../nbl/findingaids.html" class="current">Archival Finding Aids</a></li>
    <ul id="subnav">
		<li><a href="../../eadsearch/index.jsp">Search Finding Aids</a></li>
		<li><a href="#nogo" class="subcurrent">Browse Finding Aids</a></li>
		<li><a href="../nbl/findingaids_help.html">Finding Aids Help</a></li>
		<li><a href="../nbl/findingaids_feedback.html">Feedback</a></li>
	</ul>
  <li><a href="../nbl/oralhistory.html">Oral Histories</a></li>
  <li><a href="../nbl/collections.html">Collections</a></li>
  <li><a href="../nbl/contact.html">Contact Us</a></li>
  <li><a href="../nbl/sitemap.html"> Site Map</a></li>
</ul>		

<a href="http://www.facebook.com/pages/College-Park-MD/Center-for-History-of-PhysicsNiels-Bohr-Library-Archives/9563338557" title="Find us on Facebook!" target="_blank" onmouseover="MM_swapImage('button_fb','','../nbl/images/button_fb_on.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="../nbl/images/button_fb_off.jpg" alt="Button image linking to Facebook fan page" name="button_fb" width="130" height="30" border="0" id="button_fb" /></a>
<a href="/history/newsletter/request.html" title="Sign up for our newsletter!" onmouseover="MM_swapImage('button_news','','../nbl/images/button_news_on.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="../nbl/images/button_news_off.jpg" alt="Button image linking to newsletter signup page" name="button_news" width="130" height="30" border="0" id="button_news" /></a>

<!-- AddThis Button BEGIN -->
<script type="text/javascript">var addthis_pub="chpnbl";</script>
<a href="http://www.addthis.com/bookmark.php?v=20" onmouseover="return addthis_open(this, '', '[URL]', '[TITLE]')" onmouseout="addthis_close()" onclick="return addthis_sendto()"><img src="http://s7.addthis.com/static/btn/lg-share-en.gif" width="125" height="16" alt="Bookmark and Share" style="border:0"/></a><script type="text/javascript" src="http://s7.addthis.com/js/200/addthis_widget.js"></script>
<!-- AddThis Button END -->
				
	</div>
<!--END LEFT NAV-->

<!--CONTENT AREA NEXT TO LEFT NAV-->
<div id="content">
               <h1>Browse the Physics History Finding Aids</h1>
               <a name="#top" style="display: none;">&nbsp;</a>
               <p>Jump to contributing institution:</p>
               <form name="form1">
                  <select name="institutions" size="1" onchange="MM_jumpMenu('parent',this,'0')">
                     <option value="#" selected="selected">Select Institution</option>
${browsedropdown}
                  </select>
               </form>
               <p>Hint: To search for a term inside a finding aid, use your browser's search function, usually Ctrl-F, to find the term on the page.<!--RECORDS-->
                </p>
${browsecontent}
               <div id="jumpto"/>
                <!--TIME STAMP-->
</div>
<!--END CONTENT AREA NEXT TO LEFT NAV-->
</div>
<!--END MAIN AREA BELOW HEADER AND HORIZONTAL NAV-->
<!--FOOTER-->
<div id="footer">
            <div>
               <a href="http://www.aip.org/aip/copyright.html">Copyright &copy; <script language="JavaScript">
<!--Hide from old browsers
var year=""; mydate = new Date(); myyear= mydate.getFullYear(); year = myyear; document.write(year);
// End hiding-->
</script></a> | <a href="http://www.aip.org/">American Institute of Physics</a> | <a href="http://www.aip.org/aip/privacy.html">Privacy Policy</a>
            </div>
         </div>
<!--END FOOTER-->
</div>
<!--END WRAPPER-->
</body>
</html>""")





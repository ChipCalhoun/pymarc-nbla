# mptemplates.py - mark a. matienzo - used by mirrorpages.py

from string import Template

htmltemplate = Template('''<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="charset=utf-8" />
        <title>${creator} ${title}</title>
        <style type="text/css">
            .overlay { position: absolute; left: 0; top: 0; width: 100%; max-width: 100% !important; height: 100%; max-height: 100% !important; background-color: #eec; font-weight: bold; text-align: center; color: #000; }
            .valign { margin-left: -16.67%; position: absolute; top: 50%; left: 50%; } 
            td { font-weight: bold; color: #000; }
            body { color: #eee; background-color: #fff; }
        </style>
    </head>
    <script language="javascript"><!-- Begin
        redirURL = "${jsurl}";
        redirTime = "1";
        function redirTimer() { self.setTimeout( "self.location.href = redirURL ;", redirTime) ; } 
        // End -->
    </script>
    <meta name="robots" content="nofollow"/>
    <meta name="googlebot" content="nofollow"/>
    <body onLoad="redirTimer()">
        <div class="overlay">
            <div class="valign">
            If you are not immediately redirected, please click <a href="${url}" rel="nofollow">here</a>
            </div>
        </div>
        ${recordbody}
    </body>
</html>''')

indextop = Template('''<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="charset=utf-8" />
        <title>${title}</title>
        <style type="text/css">
        .floater { float: left; padding: 3px; }
        </style>
    </head>
    <body style="text-align: center;">
        <p>This page contains links to catalog records of the Niels Bohr Library at the Center for History at the American Institute of Physics, including the International Catalog of Sources for History of Physics and Allied Sciences (ICOS). <br/> You can search or browse the catalog from our <a href="http://aip.org/history/">home page</a>.</p>''')

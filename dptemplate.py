from string import Template

dppage = Template("""<?xml version="1.0" encoding="iso-8859-1" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
    <head>
        <title>Documentation Preserved Report - ${subtitle}</title>
    </head>
    <body>
        <hr/>
        <h2>Documentation Preserved - ${subtitle}</h2>
        <hr/>
${collections}
    </body>
</html>""")

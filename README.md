PySitemap
=========

A Python library for generating a sitemap



Latest Version
--------------
The latest version of this project (without the image or mobile extensions) can be found at http://github.com/vitalvas/pysitemap.

The latest version of my fork is available at https://github.com/midnightdev/pysitemap


Installation 
------------
To get the full extension, you need to download the source.

To install pysitemap without the image or video extensions, use pip.

* Option 1 : Install via pip ::

```
pip install pysitemap
```


* Option 2 : If you have downloaded the source ::

```
python setup.py install
```

Documentation
-------------

#### Basic use

```python
from pysitemap import SiteMap
from datetime import datetime

site = SiteMap()
site.add(
	loc='http://example.com/webhp', 
	lastmod=datetime.now(), 
	changefreq='weekly',
	priority=0.5
)

print site.to_string()
```


#### Image Extension

```python
from pysitemap import SiteMap
from datetime import datetime

image_site = SiteMap(domain='http://example.com')
image_site.add(
    loc='http://example.com/webhp',
    image_loc='http://example.com/webhp/my_image.png',
    caption='This is a caption',
    geo_location='London, England',
    image_title='Awesome Image',
    license='http://example.com/license.txt'
)

print image_site.to_string()
```

How to produce a Sitemap for a mobile site:

#### Mobile Extension

```python
mobile_site = SiteMap(domain='http://m.example.com', mobile=True)
```


Reporting Bugs
--------------
Please report the bugs at github issue tracker.
https://github.com/vitalvas/pysitemap/issues


Author
------
VitalVas <source@vitalvas.com>
Vitaliy Vasilenko

* http://github.com/vitalvas
* http://www.vitalvas.com

Extension Author
------
dblarons <aaron.h.smith@vanderbilt.edu>
Aaron Smith

* http://github.com/midnightdev
* http://www.aaronhsmith.com


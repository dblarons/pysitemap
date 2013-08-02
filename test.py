#!/usr/bin/env python

from pysitemap import SiteMap
from datetime import datetime

site = SiteMap(domain='http://example.com')
site.add(
    loc='http://example.com/webhp',
    lastmod=datetime.now(),
    changefreq='weekly'
)

print site.to_string()

# Site with images

image_site = SiteMap(domain='http://example.com')
image_site.add(
    loc='http://example.com/webhp',
    lastmod=datetime.now(),
    changefreq='weekly',
    priority=0.8,
    image_loc='http://example.com/webhp/my_image.png',
    caption='This is a caption',
    geo_location='London, England',
    image_title='Awesome Image',
    license='http://example.com/license.txt'
)

print image_site.to_string()

# Mobile site

mobile_site = SiteMap(domain='http://m.example.com', mobile=True)
mobile_site.add(
    loc='http://m.example.com/webhp',
    lastmod=datetime.now(),
    image_loc='http://m.example.com/webhp/my_image.png'
)

print mobile_site.to_string()

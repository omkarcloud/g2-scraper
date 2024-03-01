from botasaurus import *
from botasaurus.sitemap import Sitemap, Filters, Extractors

links = (
    Sitemap("https://www.g2.com/sitemaps/sitemap_index.xml.gz")
    .filter(Filters.first_segment_equals("products"))
    .extract(Extractors.extract_link_upto_second_segment())
    .links()
)
bt.write_json(links, "products")
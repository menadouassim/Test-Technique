# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from urllib.parse import urlparse


class HackernewsPipeline:
    def process_item(self, item , spider):

        # Validate the link field

        link=item.get("source")
        
        if not link :
            item["source"]="Lien non disponible"
        else:
            link = link.strip()
            parsed_url = urlparse(link)

            if parsed_url.scheme not in ("http", "https"):
                raise DropItem(f"Invalid URL: {link}")
            
            item["source"] = link

        # transform the points field
        points = item.get("Nbr_up_votes")
        if points is not None:
            try:
                item["Nbr_up_votes"] = int(str(points).split()[0])
            except (ValueError, IndexError):
                item["Nbr_up_votes"] = 0
        else:
            item["Nbr_up_votes"] = 0
        return item

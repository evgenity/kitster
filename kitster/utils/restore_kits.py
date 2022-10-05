from kits.models import Author, Kit, Product, Tag
import yaml


kit_files = ['AtlasTuneKit.markdown', 'atlastunesoft.markdown', 'sketch-arch.markdown', 'sketch-base.markdown', 'video-streaming.markdown',	'watercolor.markdown']

for kit_file in kit_files:
	stream = open("../_kits/" + kit_file, "r")
	docs = yaml.load_all(stream, yaml.FullLoader)

	doc = next(docs)
	print(doc['author'])
	a = Author.objects.get(name=doc['author'])
	print(doc.keys())
	t = Tag.objects.get(pk=1)
	kit = Kit(pub_date=doc['date'] ,
			tag=t,
		title=doc['title'] or "default",
		author=a,
		cover= 'static'+doc['cover'][7:] or "default",
		hero_cover='static/images/1500x500.png',
		description=doc['description'] or "default")
	kit.save()
	for p in doc['products']:
		product = Product(kit=kit,
			 name=p['product_title'] or "default",
			 description=p['product_description'] or "default",
			 img_url='static'+p['img_url'][7:] or "default" ,
		 	yandex_market_link=p['yandex_market_link'] or "default")	
		product.save()
#./manage.py shell < myscript.py
#exec(open('myscript.py').read())
from kits.models import Author
import yaml

for maker_file in ['atlastune.md']:
	stream = open("../_makers/" + maker_file, "r")
	docs = yaml.load_all(stream, yaml.FullLoader)

	doc = next(docs)
	print(doc['name'])
	print(doc['author-profile'])
	print('static' + doc['cover'][7:])
	print('static' + doc['author-avatar'][7:])

	author = Author(name=doc['name'], social_link=doc['author-profile'], avatar='static' + doc['author-avatar'][7:],hero_cover='static' + doc['cover'][7:],pro=True)
	author.save()
# for t in tagsut:
# 	tag = Tag(name=t['name'], class_addon=t['class'])
# 	tag.save()
#./manage.py shell < myscript.py
#exec(open('myscript.py').read())
from kits.models import Tag
tags = [{'name': '🔥 Все', 'class': 'category-all'}, {'name': '✏️ Рисунок', 'class': 'category-drawing'}, {'name': '🎥 Видео','class': 'category-video'}, {'name': '🎙 Подкасты', 'class': 'categoy-podcast'}, {'name': '🍽 Кулинария', 'class': 'category-cooking'}, {'name': '📚 Книги', 'class': 'category-books'}, {'name': '🎮 Гейминг', 'class': 'category-gaming'}, {'name': '🎼 Музыка', 'class': 'category-music'}]
for t in tags:
	tag = Tag(name=t['name'], class_addon=t['class'])
	tag.save()
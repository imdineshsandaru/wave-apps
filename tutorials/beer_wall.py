import time
from h2o_wave import site, ui

page = site['/beer']

beer_card = page.add('wall', ui.markdown_card(
    box='1 1 4 2',
    title='99 Bottles of Beer',
    content='',
    data=dict(before='99', after='98')
))

beer_card.content = """={{before}} bottles of beer on the wall, {{before}} bottles of beer.

Take one down, pass it around, {{after}} bottles of beer on the wall...
"""

for i in range(99, 0, -1):
    beer_card.data.before=str(i)
    beer_card.data.after=str(i-1)
    page.save()
    time.sleep(1)

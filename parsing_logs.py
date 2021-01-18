def get_value_from_list(obgect_list, separator, key):
    """Функция находит значение ключа key из списка object_list
    по разделителю separator
    :param object_list: список строк
    :param separator: разделитель
    :param key: искомый ключ"""
    
    value = None
    
    for obgect in obgect_list:
        words = obgect.split(separator)
        if words[0] == key:
            value = words[1]
            break
    
    return value



log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

split_logs = log.split('\n')

goods_and_price = []
for log in split_logs:
    parametry = log.split(';')
    
    goods_and_price_list = {
        'product':'',
        'price': 0,
    }
    goods = get_value_from_list(parametry, ':', 'item')
    goods_price = get_value_from_list(parametry, ':', 'item_cost')
    
    goods_and_price_list['product'] = goods
    goods_and_price_list['price'] = goods_price
    goods_and_price.append(goods_and_price_list)


inexpensive_goods = []

for product in goods_and_price:
    if int(product['price']) < 13000:
        if product['product'] not in inexpensive_goods:
            inexpensive_goods.append(product['product'])

print(inexpensive_goods)


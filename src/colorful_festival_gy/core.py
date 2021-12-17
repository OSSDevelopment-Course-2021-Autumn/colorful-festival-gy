from typing import List, Set
from lunarcalendar.basefestival import Festival
from lunarcalendar.festival import festivals
from stringcolor import cs
from date_string import DateString

__favorite_festival__ : Set[str] = set()

__en_festivals__ = [
    'New Year\'s Day', 'Valentine\'s Day',
    'Mother\'s Day', 'Halloween', 
    'Thanksgiving Day', 'Christmas Eve',
    'Christmas Day', 'Easter'
]

__cn_festivals__ = [
    'LaBa Festival', 'New Year\'s Eve', 
    'Ching Ming Festival',
    'XiaoNian', 'New Year', 'PoWu Festival',
    'Lantern Festival', 'Dragono Head Festival',
    'Dragon Boat Festival', 'Qixi Festival',
    'Ghost Festival', 'Mid-Autumn Festival',
    'Double Ninth Festival', 'HanYi Festival',
    'Dong Festival'
]

def set_favorite_festival(fest: str) -> None:
    __favorite_festival__.add(fest)

def get_favorite_festival() -> List[str]:
    return list(__favorite_festival__)

def cancel_favorite_festival(fest: str) -> None:
    __favorite_festival__.remove(fest)

def __print_festivals__(fests: List[Festival], year: int) -> None:
    for fest in fests:
        color = ''
        if fest.get_lang('en') in __favorite_festival__ or any([i in __favorite_festival__ for i in fest.get_lang_list('zh')]):
            color = 'cyan'
        elif fest.get_lang('en') in __en_festivals__:
            color = 'blue'
        elif fest.get_lang('en') in __cn_festivals__:
            color = 'red'
        print(cs(fest.get_lang('zh') + ' ' + str(fest(year)), color))

def year_festivals(year: int) -> None:
    f = sorted(festivals, key=lambda x: x(year))
    __print_festivals__(f, year)

def next_festivals(date: str) -> None:
    ds = DateString(date)
    year = ds.year
    f = sorted(festivals, key=lambda x: x(year))
    __print_festivals__([i for i in festivals if DateString(i(year)) - ds > 0][:10], year)
    
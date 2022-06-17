import datetime

import numpy as np

from .utils import *
from .client import HZDataClient
from .hz_finance_service import *


def get_all_trade_days():
    """
    获取所有交易日

    :return 包含所有交易日的 numpy.ndarray, 每个元素为一个 datetime.date 类型.
    """
    data = HZDataClient.instance().get_all_trade_days()
    if str(data.dtype) != "object":
        data = data.astype(datetime.datetime)
    return data


def get_trade_days(start_date=None, end_date=None, count=None):
    """
    获取指定日期范围内的所有交易日

    :return numpy.ndarray, 包含指定的 start_date 和 end_date, 默认返回至 datatime.date.today() 的所有交易日
    """
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    data = HZDataClient.instance().get_trade_days(**locals())
    if str(data.dtype) != "object":
        data = data.astype(datetime.datetime)
    return data


def get_all_securities(types=[], date=None):
    """
    获取平台支持的所有股票、基金、指数、期货信息

    :param types list: 用来过滤securities的类型, list元素可选: ‘stock’, ‘fund’, ‘index’, ‘futures’, ‘etf’, ‘lof’, ‘fja’, ‘fjb’. types为空时返回所有股票, 不包括基金,指数和期货
    :param date 日期, 一个字符串或者 datetime.datetime/datetime.date 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息
    :return pandas.DataFrame
    """
    date = to_date_str(date)

    return HZDataClient.instance().get_all_securities(**locals())


def get_price(security, start_date=None, end_date=None, frequency='daily',
              fields=None, skip_paused=False, fq='pre', count=None, fill_paused=True):
    """
    获取一支或者多只证券的行情数据

    :param security 一支证券代码或者一个证券代码的list
    :param count 与 start_date 二选一，不可同时使用.数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据
    :param start_date 与 count 二选一，不可同时使用. 字符串或者 datetime.datetime/datetime.date 对象, 开始时间
    :param end_date 格式同上, 结束时间, 默认是'2015-12-31', 包含此日期.
    :param frequency 单位时间长度, 几天或者几分钟, 现在支持'Xd','Xm', 'daily'(等同于'1d'), 'minute'(等同于'1m'), X是一个正整数, 分别表示X天和X分钟
    :param fields 字符串list, 默认是None(表示['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段), 支持以下属性 ['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit', 'low_limit', 'avg', 'pre_close', 'paused']
    :param skip_paused 是否跳过不交易日期(包括停牌, 未上市或者退市后的日期). 如果不跳过, 停牌时会使用停牌前的数据填充, 上市前或者退市后数据都为 nan
    :param panel: 当传入一个标的列表的时候，是否返回一个panel对象，默认为True，表示返回一个panel对象
           注意：
               当security为一个标的列表，且panel=False的时候，会返回一个dataframe对象，
               在这个对象中额外多出code、time两个字段，分别表示该条数据对应的标的、时间
    :param fill_paused : False 表示使用NAN填充停牌的数据，True表示用close价格填充，默认True
    :return 如果是一支证券, 则返回pandas.DataFrame对象, 行索引是datetime.datetime对象, 列索引是行情字段名字; 如果是多支证券, 则返回pandas.Panel对象, 里面是很多pandas.DataFrame对象, 索引是行情字段(open/close/…), 每个pandas.DataFrame的行索引是datetime.datetime对象, 列索引是证券代号.
    """

    # security = convert_security(security)
    start_date = to_datetime_str(start_date)
    end_date = to_datetime_str(end_date)
    if (not count) and (not start_date):
        start_date = "2015-01-01"
    if count and start_date:
        raise ParamsError("(start_date, count) only one param is required")
    return HZDataClient.instance().get_price(**locals())


# 获取choiceinfo数据库中的财务数据
def get_choiceinfo(query_object):
    sql = get_finance_sql(query_object)
    params = {
        "sql": sql
    }
    return HZDataClient.instance().get_choiceinfo(**params)


# 获取choice数据库中的财务数据
def get_choice(query_object):
    sql = get_finance_sql(query_object)
    params = {
        "sql": sql
    }
    return HZDataClient.instance().get_choice(**params)


def _collect_func():
    funcs = []
    for func in globals().keys():
        if func.startswith("get"):
            funcs.append(func)
    return funcs


__all__ = [
    "query"
]
__all__.extend(_collect_func())
del _collect_func

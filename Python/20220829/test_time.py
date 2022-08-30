# -*- coding: utf-8 -*-

import datetime
import time


def get_utc_timestamp():
    """获取UTC时间的时间戳"""
    return get_local_timestamp() + time.timezone


def get_local_timestamp():
    """获取本地时间的时间戳"""
    return time.time()


def get_utc_time():
    """
    获取datetime格式的UTC时间
    :return: datetime格式的utc时间
    """
    # 方法一: datetime.datetime(2022, 8, 29, 12, 19, 21, 889000)
    utc_time = datetime.datetime.fromtimestamp(get_utc_timestamp())

    # 方法二: datetime.datetime(2022, 8, 29, 12, 19, 23, 69000)
    # utc_time = datetime.datetime.utcfromtimestamp(time.time())

    return utc_time


def get_local_time():
    """
    获取datetime格式的本地时间
    :return: datetime格式的本地时间
    """
    # 方法一:
    local_time = datetime.datetime.fromtimestamp(get_local_timestamp())

    # 方法二：
    # local_time = datetime.datetime.now()

    return local_time


def get_utc_time_str():
    """
    获取字符串格式的UTC时间
    :return: 字符串格式的utc时间
    """

    utc_time = get_utc_time()
    utc_time_str = datetime_to_str(utc_time)
    return utc_time_str


def get_local_time_str():
    """
    获取字符串格式的本地时间
    :return: 字符串格式的本地时间
    """
    local_time = get_local_time()
    local_time_str = datetime_to_str(local_time)
    return local_time_str


def get_yesterday_utc_time():
    """
    获取昨天此刻的UTC时间
    :return: datetime格式的昨天此刻的UTC时间
    """

    utc_time = get_utc_time()
    return utc_time + datetime.timedelta(days=-1)


def get_yesterday_local_time():
    """
    获取昨天此刻的本地时间
    :return: datetime格式的昨天此刻的本地时间
    """
    local_time = get_local_time()
    return local_time + datetime.timedelta(days=-1)


def timestamp_to_str(timestamp=get_local_timestamp()):
    """
    获取字符串格式的时间
    :param timestamp: 时间戳，格式为浮点型，默认为本地时间
    :return: 返回字符串格式的时间，例如'2022-08-29T09:13:06Z'
    """
    datetime_time = timestamp_to_datetime(timestamp)
    str_time = datetime_to_str(datetime_time)
    return str_time


def timestamp_to_datetime(timestamp):
    """
    将时间戳转换为本地datetime格式的时间
    :param timestamp: 时间戳
    :return: datetime格式的时间
    """
    return datetime.datetime.fromtimestamp(timestamp)


def datetime_to_str(datetime_time, s_format="%Y-%m-%dT%H:%M:%SZ"):
    """
    将datetime格式的时间转换为字符串格式的时间
    :param datetime_time: datetime格式的时间
    :param s_format: 字符串格式时间的具体格式，常见的有"%Y-%m-%dT%H:%M:%SZ"
    :return: 字符串格式的时间，例如'2022-08-29T09:13:06Z'
    """
    return datetime_time.strftime(s_format)


def datetime_to_timestamp(datetime_time):
    """
    将datetime格式的时间转换为浮点型的时间戳
    :param datetime_time: datetime格式的时间
    :return: 浮点型的时间戳，比如1661778641.0
    """
    assert isinstance(datetime_time, datetime.datetime)
    timetuple = datetime_time.timetuple()
    timestamp = time.mktime(timetuple)
    return timestamp


def str_to_datetime(str_time, s_format="%Y-%m-%dT%H:%M:%SZ"):
    """
    将字符串格式的时间转换为datetime格式的时间
    :param str_time: 字符串格式的时间
    :param s_format: 字符串格式时间的具体格式，常见的有"%Y-%m-%dT%H:%M:%SZ"
    :return: datetime格式的时间
    """
    return datetime.datetime.strptime(str_time, s_format)


def str_to_timestamp(str_time):
    datetime_time = str_to_datetime(str_time)
    timestamp = datetime_to_timestamp(datetime_time)
    return timestamp


def utc_to_local(datetime_time):
    """
    将datetime格式的UTC时间，转换为datetime格式的本地时间
    :param datetime_time: datetime格式的UTC时间
    :return: datetime格式的本地时间
    """
    pass


def local_to_utc(datetime_time):
    """
    将datetime格式的本地时间，转换为datetime格式的UTC时间
    :param datetime_time: datetime格式的本地时间
    :return: datetime格式的UTC时间
    """
    pass


def utc_str_to_local_str(str_time):
    """
    将字符串格式的UTC时间，转换为字符串格式的本地时间
    :param str_time: 字符串格式的UTC时间
    :return: 字符串格式的本地时间
    """
    utc_time = datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%SZ")
    return utc_time + datetime.timedelta(hours=8)


def local_str_to_utc_str(str_time):
    """
    将字符串格式的本地时间，转换为字符串格式的UTC时间
    :param str_time: 字符串格式的时间
    :return: 字符串格式的UTC时间
    """
    pass


if __name__ == '__main__':
    print get_utc_timestamp()
    print get_local_timestamp()
    print get_utc_time()
    print get_local_time()
    print get_utc_time_str()
    print get_local_time_str()
    print get_yesterday_utc_time()
    print get_yesterday_local_time()
    print timestamp_to_str(get_utc_timestamp())
    print timestamp_to_datetime(get_utc_timestamp())
    print datetime_to_str(timestamp_to_datetime(get_utc_timestamp()))
    print datetime_to_timestamp(timestamp_to_datetime(get_utc_timestamp()))
    print str_to_datetime(get_local_time_str())
    print str_to_timestamp(get_local_time_str())
    print utc_to_local(get_utc_time())
    print utc_str_to_local_str(get_utc_time_str())
    print local_to_utc(get_local_time())
    print local_str_to_utc_str(get_local_time_str())
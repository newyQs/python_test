def get_date_year_month(pm_date):
    """
    获取参数pm_date对应的年份和月份
    """
    if not pm_date:
        raise Exception("get_curr_year_month: pm_date can not be None")

    # get date's yyyymmddHHMMSS pattern
    str_date = str(pm_date).replace("-", "").replace(" ", "").replace(":", "")

    year = str_date[:4]
    month = str_date[4:6]
    return year, month

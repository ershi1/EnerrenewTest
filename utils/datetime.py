from datetime import datetime, timedelta,date
from dateutil.relativedelta import relativedelta


#处理日期范围
class GetDatetime:
    #获取现在时刻
    def get_now(self):
        now = datetime.now()
        return now.strftime('%H:%M:%S')

    #获取今天日期
    def get_today(self):
        current_date = date.today()
        return current_date.strftime('%Y-%m-%d')

    #获取昨天的日期
    def get_yesterday(self):
        yesterday = datetime.now() - timedelta(days=1)
        return yesterday.strftime('%Y-%m-%d')

    #获取周一日期，返回monday
    def get_monday(self):
        current_date = date.today()
        today_weekday = current_date.weekday()
        monday = current_date - timedelta(days=today_weekday)
        return monday.strftime('%Y-%m-%d')

    # 获取上周今天的日期
    def get_LastWeekToday(self):
        # 确定今天日期
        current_date = date.today()
        # 今天日期减一周是上周的日期
        last_week_today = current_date - timedelta(weeks=1)
        return last_week_today.strftime('%Y-%m-%d')

    #获取上周昨天的日期
    def get_LastWeekYesterday(self):
        current_date = date.today()
        yesterday = current_date - timedelta(days=1)
        last_week_yesterday = yesterday - timedelta(weeks=1)
        return last_week_yesterday.strftime('%Y-%m-%d')

    #获取上周一日期，返回last_monday
    def get_lastmonday(self):
        # 确定今天
        current_date = date.today()
        today_weekday = current_date.weekday()
        last_monday = current_date - timedelta(days=today_weekday + 7)
        return last_monday.strftime('%Y-%m-%d')

    #获取本月1号日期
    def get_monthbegin(self):
        current_date = date.today()
        last_month_begin = current_date.replace(month=current_date.month, day=1)
        return last_month_begin.strftime('%Y-%m-%d')

    # 获取上月月份，返回last_month_begin(上个月1号), last_month_end(上个月今天)
    def get_lastmonth_begin(self):
        current_date = date.today()
        last_month_begin = current_date.replace(month=current_date.month - 1, day=1)
        return last_month_begin.strftime('%Y-%m-%d')

    def get_lastmonth_today(self):
        current_date = date.today()
        last_month_end = current_date.replace(month=current_date.month - 1, day=current_date.day)
        return last_month_end.strftime('%Y-%m-%d')

    #获取去年日期，返回last_year_begin（去年1号）
    def get_lastyear_begin(self):
        current_date = date.today()
        last_year_begin = current_date.replace(year=current_date.year - 1, month=1, day=1)
        return last_year_begin.strftime('%Y-%m-%d')

    #获取去年日期，返回last_year_end(去年今天）
    def get_lastyear_today(self):
        current_date = date.today()
        last_year_today = current_date.replace(year=current_date.year - 1, month=current_date.month, day=current_date.day)
        return last_year_today.strftime('%Y-%m-%d')

    #获取预测周期的最后一天
    def get_endtime(self):
        current_date = date.today()
        end_time = current_date + relativedelta(days=+15)
        return end_time.strftime('%Y-%m-%d')
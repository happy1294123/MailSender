from datetime import datetime, timedelta
import re
import calendar
# import win32com.client as win32   

# data = {
#     'fid': 'Fund Id',
#     'fname': 'Fund Name',
#     'rname': 'Rule Name',
#     'note': 'this is note Note(nothing)',
#     'occurred': '2023-02-11 18:00:00',
#     'fix': '5d',
#     'pm_ratify': True
# }

class MailSender:
    # https://uic.jp/calendar/
    jp_holiday = [
            '2023-02-23',
            '2023-03-21',
            '2023-04-29',
            '2023-05-03',
            '2023-05-04',
            '2023-05-05',
            '2023-07-17',
            '2023-08-11',
            '2023-09-18',
            '2023-09-23',
            '2023-10-09',
            '2023-11-03',
            '2023-11-23'
        ]

    def __init__(self, data):
        self.data = data

    def create_title(self):
        if self.data['pm_ratify']:
            return f"Action Required: {self.data['fname']}"
        else:
            return f"this is just FYI: {self.data['fname']}"

    def create_content(self):
        content = ''
        content += f"【Fund name】({self.data['fid']}){self.data['fname']}<br>"
        content += f"【Occurred date】{self.get_occurred_date().strftime('%m/%d')}<br>"
        content += f"【Fixed Deadline】{self.get_fix_date().strftime('%m/%d')}<br>"
        content += f"【Breadch Detail】{self.get_note()} where rule {self.data['rname']}<br>"
        content += f"【Action Required】{self.get_fix_text()}"
        return content

    def get_occurred_date(self):
        oc_date = datetime.strptime(self.data['occurred'], '%Y-%m-%d %H:%M:%S')
        oc_date = oc_date - timedelta(days=1)
        return self.__skip_holiday(oc_date)

    def get_fix_date(self):
        fix_date = self.get_occurred_date()
        fix = self.data['fix']
        if fix == '5d' or fix == '6d':
            count = int(fix[:-1])
            while count:
                fix_date = fix_date + timedelta(days=1)
                if datetime.date(fix_date).isoweekday() in [6,7]:
                    continue
                elif fix_date.strftime('%Y-%m-%d') in self.jp_holiday:
                    continue
                count -= 1
        elif fix == '3w':
            fix_date += timedelta(weeks=3)
        elif fix == '1m':
            fix_date = self.__add_one_month(fix_date)

        return fix_date

    def __skip_holiday(self, date):
         # 若遇假日，往前到星期五
        week_num = datetime.date(date).isoweekday()
        if week_num == 6: # 星期六
            delta_days = 1
        elif week_num == 7: # 星期天
            delta_days = 2
        else:
            delta_days = 0
        adj_date = date - timedelta(days=delta_days)

        # 檢查日本國定假日
        while adj_date.strftime('%Y-%m-%d') in self.jp_holiday:
            adj_date = adj_date - timedelta(days=1)
        return adj_date

    def __add_one_month(self, date):
        month = date.month
        year = date.year + month // 12
        month = month % 12 + 1
        day = min(date.day, calendar.monthrange(year,month)[1])
        return datetime.strptime(f'{year}-{month}-{day}', "%Y-%m-%d")

    def get_note(self):
        return re.sub("\\(.*\\)", '', self.data['note'])

    def get_fix_text(self):
        fix = self.data['fix']
        if fix == '5d':
            return 'this is 5d text'
        elif fix == '6d':
            return 'this is 6d text'
        elif fix == '3w':
            return 'this is 3w text'
        elif fix == '1m':
            return 'this is 1m text'
        else:
            return 'undefined fix text'

    def write_mail(self):
        # windows
        # olApp = win32.Dispatch('Outlook.Application')
        # olNS = olApp.GetNameSpace('MAPI')

        # mail = olApp.CreateItem(0)
        # mail.Subject = self.create_title()
        # mail.BodyFormat = 1 # plain text
        # mail.Body = self.create_content()
            # mail.HTMLbody = self.create_content()
        # mail.To = 'happy1294123@gmail.com'
            # mail.CC = 'cc1@gmail.com; cc2@gmail.com'
        # mail.Display()

        # Mac
        from appscript import app, k
        outlook = app('Microsoft Outlook')

        msg = outlook.make(
            new=k.outgoing_message,
            with_properties={
                k.subject: self.create_title(),
                k.plain_text_content: self.create_content()})

        msg.make(
            new = k.recipient,
            with_properties={
                k.email_address: {
                    k.name: 'Fake Person',
                    k.address: 'fakeperson@gmail.com'}})

        msg.open()
        msg.activate()





# sender = MailSender(data)
# sender.write_mail()



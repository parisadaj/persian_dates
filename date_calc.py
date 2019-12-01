from datetime import datetime
from datetime import timedelta

class Date_Calc:
    def __init__(self, date, _type = 'date'):
##        print('__init__')
        self.date = date
        self._type = _type
        
        self.day, self.month, self.year = self.calc_days()
        self.new_date = self.check_add()
        print(self.new_date)
        
        self.md = self.calc_md() if self._type == 'date' or self._type == 'm' else 'a'


    def calc_days(self,date = None, _type= None):
##        print('calc_days')

        _type = _type or self._type
        date = date or self.date
        
        
        day, month, year =\
                  (date, 0, 0) if _type == 'd' else\
                  (0, date, 0)  if _type == 'm' else\
                  (0, 0, date) if _type == 'y' else\
                  self.calc_date()
        
        new_date = self.check_add(day = day, month = month, year = year)
        return self.calc_date(new_date)
    
    def check_add(self,
                  day = None,
                month = None,
                year = None):
##        print('check add')

        day = self.day if day == None else day
        month = self.month if month == None else month
        year = self.year if year == None else year
        md = self.calc_md(day, month, year)
        new_date = day + month * 100 + year * 10000
        
        while day > md or month > 12:
            if day > md:
                day -= md
                month += 1
            if month > 12:
                month -= 12
                year += 1
                
            new_date = day + month * 100 + year * 10000
            day, month, year = self.calc_date(new_date)
            md = self.calc_md(day, month, year)
            
        return new_date

    def check_sub(self, o):
        day, month, year, md = self.day, self.month, self.year, self.md
        while day < o.day:
            day += md
            month -= 1
            new_date = day + month * 100 + year * 10000
            day, month, year = self.calc_date(new_date)
            md = self.calc_md(day, month, year)
            
        while month < o.month:
            month += 12
            year -= 1
            new_date = day + month * 100 + year * 10000
            day, month, year = self.calc_date(new_date)
            md = self.calc_md(day, month, year)
        return new_date - o.date

    def calc_date(self,
                  date = None):
##        print('calc_date')

        date = date or self.date
                                                   
        day = date % 100
        month = (date // 100) % 100
        year = (date // 10000) % 10000
        return day, month, year
                                                   
    def calc_md(self,
                day = None,
                month = None,
                year = None):
##        print('calc_md')

        day = self.day if day == None else day
        month = self.month if month == None else month
        year = self.year if year == None else year
        
        if month < 7:
            md = 31
        elif month == 12 and year % 4 != 3:
            md = 29
        else:
            md = 30
        return md
        
    
    def __add__(self, o):
        print('add')

        add = self.new_date + o.new_date 
        return self.check_add(add)
    
    def __sub__(self, o):
        sub = self.date - o.date
        return self.check_sub(o)

a = Date_Calc(13980610)
b = Date_Calc(100, 'd')
c = Date_Calc(2, 'm')
print(a.date, b.date, c.date)

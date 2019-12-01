class Date_Calc:
    def __init__(self, date, _type = 'date'):
        self.date = date
        self._type = _type
        
        self.day, self.month, self.year =\
                  (self.date, 0, 0) if self._type == 'd' else\
                  (0, self.date, 0)  if self._type == 'm' else\
                  (0, 0, self.date) if self._type == 'y' else\
                  self.calc_date()
             
        
        self.md = self.calc_md() if self._type == 'date' or self._type == 'm' else\
                  'a'



    def check_add(self,
                  date = None):
        date = date or self.date
                                                   
        day, month, year = self.calc_date(date)
        md = self.calc_md(day, month, year)
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
        date = date or self.date
                                                   
        day = date % 100
        month = (date // 100) % 100
        year = (date // 10000) % 10000
        return day, month, year
                                                   
    def calc_md(self,
                day = None,
                month = None,
                year = None):
        day = day or self.day
        month = month or self.month
        year = year or self.year
        
        if month <  7:
            md = 31
        elif month == 12 and year % 4 != 3:
            md = 29
        else:
            md = 30
        return md
        
    
    def __add__(self, o):
        add = self.date + o.date 
        return self.check_add(add)
    
    def __sub__(self, o):
        sub = self.date - o.date
        return self.check_sub(o)

a = Date_Calc(13980610)
b = Date_Calc(100, 'd')
c = Date_Calc(2, 'm')
print(a.date, b.date, c)

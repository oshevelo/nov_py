#TODO implement sales' subtype classes

class Report:
    def __init__(self, repmonth, repyear, store, sect, db_conn):
        self.repmonth = repmonth
        self.repyear = repyear
        self.store = store
        self.sect = sect
        self.db_conn = db_conn

    def __str__(self):
        return "reporting month: {}, reporting year: {}, store: {}".format(self.repmonth, self.repyear, self.store)

    def query(self):
        strSelect = "SELECT "
        strFrom = "FROM "
        strWhere = "WHERE repMonth = {} AND repYear = {} AND storeNum = {}".format(self.repmonth, self.repyear, self.store)

        print(strSelect)

    def connectDb(self):
        #method to set up database connection

    def preparerep(self):
        #method to fill in report

    def saverep(self):
        #method to save prepared report

    def sendrep(self):
        #method to send report

class Sales(Report):
    def __str__(self):
       super.__str__(self) + ", Sales concept"

    def __init__(self, repmonth, repyear, store, sect, db_conn, online):
        super.__init__(self, repmonth, repyear, store, sect, db_conn,)
        self.online = online
    def query(self):
        strSelect = "SELECT Sum(Sales)"
        strFrom = "FROM SalesTable"
        strWhere = "WHERE repMonth = {} AND repYear = {} AND storeNum = {}".format(self.repmonth, self.repyear, self.store)

        print(strSelect)

class Units(Report):
    def __str__(self):
       super.__str__(self) + ", Units concept"

    def __init__(self, repmonth, repyear, store, sect, db_conn):
        super.__init__(self, repmonth, repyear, store, sect, db_conn,)
    def query(self):
        strSelect = "SELECT Sum(Units)"
        strFrom = "FROM UnitsTable"
        strWhere = "WHERE repMonth = {} AND repYear = {} AND storeNum = {}".format(self.repmonth, self.repyear, self.store)

        print(strSelect)

class Hours(Report):
    def __str__(self):
       super.__str__(self) + ", Hours concept"

    def __init__(self, repmonth, repyear, store, sect, db_conn):
        super.__init__(self, repmonth, repyear, store, sect, db_conn,)
    def query(self):
        strSelect = "SELECT Sum(Hours)"
        strFrom = "FROM HoursTable"
        strWhere = "WHERE repMonth = {} AND repYear = {} AND storeNum = {}".format(self.repmonth, self.repyear, self.store)

        print(strSelect)

class Productivity(Report):
    def __str__(self):
       super.__str__(self) + ", Productivity concept"

    def __init__(self, repmonth, repyear, store, sect, db_conn, online):
        super.__init__(self, repmonth, repyear, store, sect, db_conn)
        self.online = online
    def query(self):
        s=Sales(repmonth = self.repmonth,repyear = self.repyear, store = self.store, online=self.online)
        h=Hours(repmonth = self.repmonth,repyear = self.repyear, store = self.store)
        try:
            prod=s/h
        except ZeroDivisionError
            prod = 0

class AvPrice(Report):
    def __str__(self):
       super.__str__(self) + ", Average price concept"

    def __init__(self, repmonth, repyear, store, sect, db_conn, online):
        super.__init__(self, repmonth, repyear, store, sect, db_conn)
        self.online = online
    def query(self):
        s=Sales(repmonth = self.repmonth,repyear = self.repyear, store = self.store, online=self.online)
        u=Units(repmonth = self.repmonth,repyear = self.repyear, store = self.store)
        try:
            prod=s/u
        except ZeroDivisionError
            prod = 0


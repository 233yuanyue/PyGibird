from modules.data import Db
from modules.setting import MainSetting


class WinStatus:
    win_showStatus = {
        "loginWidget": False,
        "mainWin_login": False,
        "rememberAcc": False
    }


class status_opn:
    def __init__(self):
        self.sqlAcc = MainSetting.sqlAcc
        self.sqlPwd = MainSetting.sqlPwd
        self.sqlHost = MainSetting.sqlHost
        self.sqlPort = int(MainSetting.sqlPort)
        self.__db = None
        try:
            self.__db = Db(self.sqlAcc, self.sqlPwd, "winStatus", self.sqlHost, self.sqlPort)
            ret = self.__db.select_opn("select * from login_setting", False)
            WinStatus.win_showStatus["rememberAcc"] = True if (ret[0] == 1) else False
            WinStatus.win_showStatus["mainWin_login"] = True if (ret[1] == 1) else False
        except Exception as err:
            print(err)
            try:
                self.__db = Db(self.sqlAcc, self.sqlPwd, "mysql", self.sqlHost, self.sqlPort)
                self.__db.create_db("winStatus")
                self.__db.close()
                self.__db = Db(self.sqlAcc, self.sqlPwd, "winStatus", self.sqlHost, self.sqlPort)
                self.__db.create_tb("create table login_setting(rememberAcc tinyint(1) not null default 0,"
                                    "mainWin_login tinyint(1) not null default 0)")
                self.__db.insert_opn("insert into login_setting values(0, 0)")
            except Exception as err:
                print(str(err) + "\n ERROR: MySQL")

    def changeIni(self, field_name, newData):
        if field_name == "rememberAcc":
            self.__db.update_opn("update login_setting set rememberAcc = %s", newData)
        elif field_name == "mainWin_login":
            self.__db.update_opn("update login_setting set mainWin_login = %s", newData)
        WinStatus.win_showStatus[field_name] = newData

    @staticmethod
    def retVal(field_name):
        return WinStatus.win_showStatus[field_name]

    def retAcc_cacheInfo(self):
        try:
            ret = self.__db.select_opn("select * from user.cache")
            return ret
        except Exception as err:
            print(err)
            try:
                self.__db.create_db("user")
                self.__db.create_tb(
                    "create table if not exists user.cache(accountNum varchar(11) primary key not null)")
                self.__db.create_tb("create table if not exists user.master("
                                    "accountNum varchar(11) primary key not null,"
                                    "password varchar(11) not null)")
                return self.__db.select_opn("select * from user.cache")
            except Exception as err:
                print(str(err) + "\n ERROR: MySQL")

    def clearCache(self):
        # Something wrong with "truncate", so "delete"???
        self.__db.sqlExecute("delete from user.cache")

    def insertCache(self, acc):
        try:
            self.__db.insert_opn("insert into user.cache values(%s)", acc)
        except Exception as err:
            print(err)

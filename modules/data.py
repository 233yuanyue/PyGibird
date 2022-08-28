import pymysql
from modules.setting import MainSetting


class Db:
    def __init__(self, _user, _pwd, _db, _host="localhost", _port=3306, _charset="utf8mb4"):
        self.__conn = pymysql.connect(
            host=_host,
            port=_port,
            user=_user,
            password=_pwd,
            database=_db,
            charset=_charset)

    def sqlExecute(self, sql):
        cursor = self.__conn.cursor()
        cursor.execute(sql)
        self.__conn.commit()

    def insert_opn(self, i_sql, *data):
        cursor = self.__conn.cursor()
        cursor.execute(i_sql, data)
        self.__conn.commit()

    def update_opn(self, u_sql, *data):
        cursor = self.__conn.cursor()
        cursor.execute(u_sql, data)
        self.__conn.commit()

    def select_opn(self, s_sql, fetch_all=True):
        cursor = self.__conn.cursor()
        cursor.execute(s_sql)
        if fetch_all:
            ret = cursor.fetchall()
        else:
            ret = cursor.fetchone()
        self.__conn.commit()
        return ret

    def create_db(self, db_name):
        cursor = self.__conn.cursor()
        cursor.execute("create database if not exists %s" % db_name)
        self.__conn.commit()

    def create_tb(self, c_tb_sql):
        cursor = self.__conn.cursor()
        cursor.execute(c_tb_sql)
        self.__conn.commit()

    def close(self):
        self.__conn.close()

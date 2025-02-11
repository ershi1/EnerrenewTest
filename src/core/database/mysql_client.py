import pymysql


#处理数据库连接

class MysqlConnection:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    #创建连接
    def connect(self):
        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password=self.password,
            database=self.database,
            charset='utf8mb4'  # 修改为正确的字符集名称
        )
        self.cursor = self.conn.cursor()

    #断开连接
    def disconnect(self):
        if self.conn:
            self.conn.close()

    #执行查询
    def execute_query(self,sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()

    #关闭浮标
    def close_cursor(self):
        if self.cursor:
            self.cursor.close()
from sqlalchemy import create_engine

# 数据库的配置变量

HOSTNAME = '127.0.0.1'

PORT = '3306'

DATABASE = 'xt_flask'

USERNAME = 'root'

PASSWORD = 'root'

DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# 创建数据库引擎

engine = create_engine(DB_URI)

# 创建连接

with engine.connect() as con:
    rs = con.execute('SELECT 1')

    print(rs.fetchone())

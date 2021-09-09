import pymysql

# 连接数据库
conn = pymysql.connect(
        host='120.79.169.228',
        port=3306,
        user='erpdbtest02',
        passwd='qq974wlP@da',
        db='lis_one_bbs_order',
        charset = 'utf8'
    )

# 创建游标
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 查询sales_order表所需数据
sql = 'select ID,ACT_PROCESS_ID from sales_order where AUDIT_STATUS = 4'
cursor.execute(sql)

# 获取结果值
result = cursor.fetchone()
print(result)
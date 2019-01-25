import pymysql


def create_relation(location):
    db = connect_mysql()
    cursor = db.cursor()
    sql = "select id, " + location + " from job_entity"
    cursor.execute(sql)
    data = cursor.fetchall()
    # print(data)
    for index in data:
        if str(index[1]) == '0':
            insert = "insert into " + location + "(id," + location + ") VALUES (%d , '0')" % int(index[0])
            cursor.execute(insert)
        else:
            index1 = list(eval(index[1]))
            for detail in index1:
                insert = "insert into " + location + "(id," + location + ") VALUES (%d , '%s')" % (int(index[0]), detail)
                cursor.execute(insert)
    db.commit()


def connect_mysql():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
                         charset='utf8')
    return db


create_relation('seniority')

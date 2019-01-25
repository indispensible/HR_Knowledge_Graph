import pymysql

dictionary = []


def create_userdict(location):
    global dictionary
    filename = 'C:/Users/吕港/Desktop/毕业论文设计/数据/userdict.txt'
    db = connect_mysql()
    cursor = db.cursor()
    sql = "select " + location + " from " + location
    cursor.execute(sql)
    data = cursor.fetchall()
    with open(filename, 'a', encoding='utf-8') as file_object:
        for index in data:
            if str(index[0]) == '0':
                pass
            elif str(index[0]) in dictionary:
                pass
            else:
                file_object.write(str(index[0]) + ',')
                dictionary.append(str(index[0]))


def connect_mysql():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
                         charset='utf8')
    return db


create_userdict('seniority')

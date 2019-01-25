import csv

import pymysql as pymysql


def store_categories(file_name):
    with open(file_name, encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        categories = []
        for line_num, row in enumerate(reader):
            if line_num == 0:
                pass
            else:
                categories.append(row[4])
        categories = set(categories)
        db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
                             charset='utf8')
        cursor = db.cursor()
        try:
            for category in categories:
                sql = "insert into category(name) values ('%s')" % category
                cursor.execute(sql)
                db.commit()
        except:
            pass


file_name = 'C:/Users/吕港/Desktop/毕业论文设计/数据/sf_jd_all.csv'
store_categories(file_name)
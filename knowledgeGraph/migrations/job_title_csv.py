import csv
import traceback

import pymysql as pymysql


def store_categories(filename):
    with open(filename, encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        categories = []
        title = []
        for line_num, row in enumerate(reader):
            if line_num == 0:
                pass
            elif row[3] in title:
                pass
            else:
                categories.append(row[4])
                title.append(row[3])
        db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
                             charset='utf8')
        cursor = db.cursor()
        try:
            for number in range(len(title)):
                num = number + 1
                sql = "insert into title_csv(id, name, category) values ('%d', '%s', '%s')" % (num, title[number], categories[number])
                cursor.execute(sql)
            db.commit()
        except Exception as err:
            traceback.print_exc()


file_name = 'C:/Users/吕港/Desktop/毕业论文设计/数据/sf_jd_all.csv'
store_categories(file_name)

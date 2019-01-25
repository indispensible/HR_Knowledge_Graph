import csv
import traceback

import pymysql as pymysql


def store_categories(filename):
    with open(filename, encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        categories = []
        title = []
        descriptions = []
        requires = []
        id = []
        for line_num, row in enumerate(reader):
            if line_num == 0:
                pass
            else:
                desc = row[2]
                req = row[1]
                categories.append(row[4])
                title.append(row[3])
                descriptions.append(desc.replace("\n", ""))
                requires.append(req.replace("\n", ""))
                id.append(row[0])
        db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
                             charset='utf8')
        cursor = db.cursor()
        try:
            for number in range(len(requires)):
                num = pymysql.escape_string(str(id[number]))
                req1 = pymysql.escape_string(str(requires[number]))
                desc1 = pymysql.escape_string(str(descriptions[number]))
                tit1 = pymysql.escape_string(str(title[number]))
                cate1 = pymysql.escape_string(str(categories[number]))
                sql = "insert into jobs_copy(id, requireDetail, descriptionDetail, titleName, categoryName) values ('%s', '%s', '%s', '%s', '%s')" % (
                num, req1, desc1, tit1, cate1)
                cursor.execute(sql)
            db.commit()
        except Exception as err:
            traceback.print_exc()


file_name = 'C:/Users/吕港/Desktop/毕业论文设计/数据/sf_jd_all.csv'
store_categories(file_name)

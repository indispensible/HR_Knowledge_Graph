import os
import json
import pymysql


def get_files_name(path):
    list_name = []
    for file in os.listdir(path):
        # file_path = os.path.join(path, file)
        list_name.append(file)
    # print(list_name)
    get_jobs_entity(path, list_name)


number = 0


def get_jobs_entity(path1, list_name):
    global number
    for path in list_name:
        candidate = path.split('_')
        id = 0
        if 'json' not in candidate[0]:
            id = str(candidate[2])
        else:
            id = str(candidate[0])
        id = id.split('.')[0]
        path = path1 + path
        f = open(path, encoding='utf-8')
        res = json.loads(f.read())
        db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
                             charset='utf8')
        cursor = db.cursor()
        try:
            sql = "select * from jobs where id = (%d)" % int(id)
            cursor.execute(sql)
            data = cursor.fetchall()
            titleName = data[0][3]
            categoryName = data[0][4]
            skill = juage_null(res['技能'])
            vocational = juage_null(res['业务'])
            qualification = juage_null(res['学历'])
            professional = juage_null(res['专业'])
            industry = juage_null(res['行业'])
            function = juage_null(res['职能'])
            seniority = juage_null(res['年限'])
            sql = "insert into job_entity(categoryName, titleName, skill, vocational, qualification, professional, industry, function, seniority) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                categoryName, titleName, skill, vocational, qualification, professional, industry, function, seniority)
            cursor.execute(sql)
            number = number + 1
            print(number)
        except Exception as err:
            # pass
            number = number + 1
            print(number)
        db.commit()


def juage_null(data):
    if len(data) == 0:
        return '0'
    else:
        return pymysql.escape_string(str(data))


dir_path = 'C:/Users/吕港/Desktop/毕业论文设计/数据/CV_entity/JD_result/'
get_files_name(dir_path)
# list_name = ['2_20181112_6572.json', '2964.json']
# for path in list_name:
#     candidate = path.split('_')
#     id = 0
#     if 'json' not in candidate[0]:
#         id = candidate[2]
#     else:
#         id = candidate[0]
#     path = 'C:/Users/吕港/Desktop/毕业论文设计/数据/CV_entity/JD_result/' + path
#     f = open(path, encoding='utf-8')
#     res = json.loads(f.read())
#     print(id)
#     print(res)

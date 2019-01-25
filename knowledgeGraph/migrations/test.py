import csv
import traceback

import pymysql as pymysql
import urllib3
from pandas import json


def store_categories(filename):
    with open(filename, encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        title = []
        for line_num, row in enumerate(reader):
            if line_num == 0:
                pass
            else:
                title.append(row[3])
        title = set(title)
        print(len(title))
        # db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
        #                      charset='utf8')
        # cursor = db.cursor()
        # try:
        #     for number in range(len(title)):
        #         num = number + 1
        #         sql = "insert into title_csv(id, name, category) values ('%d', '%s', '%s')" % (num, title[number], categories[number])
        #         cursor.execute(sql)
        #     db.commit()
        # except Exception as err:
        #     traceback.print_exc()


# def get_job_title_category(id):
#     db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
#                          charset='utf8')
#     cursor = db.cursor()
#     try:
#         sql = "select * from jobs where id = (%d)" % id
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         print(data[0][4])
#     except Exception as err:
#         traceback.print_exc()
number = 0
def change_number():
    global number
    number = number + 1
    print(number)

# for index in range(5):
#     change_number()
# file_name = 'C:/Users/吕港/Desktop/毕业论文设计/数据/sf_jd_all.csv'
# store_categories(file_name)
# get_job_title_category(6572)


def DNN_judge():
    http = urllib3.PoolManager()
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn?access_token=24.622919d482aad3d8ff925c11144238bf.2592000.1550716334.282335-11177554"
    data = {"text":"良好的管理能力"}
    encode_data = json.dumps(data).encode('GBK')
    # JSON:在发起请求时,可以通过定义body 参数并定义headers的Content-Type参数来发送一个已经过编译的JSON数据：
    request = http.request('POST',
                           url,
                           body=encode_data,
                           headers={'Content-Type': 'application/json'}
                           )
    result = str(request.data, 'GBK')
    print(result)
    return result


DNN_judge()
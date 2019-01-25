import jieba
import pymysql

from knowledgeGraph.migrations.DNN_test import DNN_judge


# def get_dictionary(name, list, dict):
#     print(list)
#     number = 1
#     for deatil in list:
#         key = name + '_' + str(number)
#         dict[key] = deatil
#         number = number + 1
#     return dict


def get_list(list1, detail):
    list1 = list(list1)
    if detail in list1:
        pass
    else:
        if detail is not '0':
            detail = list(eval(detail))
            for element in detail:
                list1.append(element)
    return list1


def get_all_jobs(category):
    jobs = {}
    dictionary = {}
    number = 1
    db = connect_mysql()
    cursor = db.cursor()
    sql = "select name, number from title_csv_rate where category = '%s'" % category
    cursor.execute(sql)
    data = cursor.fetchall()
    jobs['entity'] = category
    try:
        for dic in data:
            dictionary[dic[0]] = int(dic[1])
        dicts = sorted(dictionary.items(), key=lambda d: d[1], reverse=True)
        for job in dicts:
            key = 'job_' + str(number)
            jobs[key] = job[0] + "_" + str(job[1]) + "个"
            number = number + 1
        return jobs
    except:
        for job in data:
            key = 'job_' + str(number)
            jobs[key] = job[0] + "_" + str(job[1]) + "个"
            number = number + 1
        return jobs
    # size = len(jobs)
    # print(size)
    # print(jobs)


def get_all_detail(title):
    details = {'entity': title}
    category = []
    skill = []
    voacational = []
    qualification = []
    professional = []
    industry = []
    function = []
    seniority = []
    db = connect_mysql()
    cursor = db.cursor()
    sql = "select * from job_entity where titleName LIKE '%" + title + "%'"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        sql1 = "select requireDetail, descriptionDetail from jobs where titleName = '" + title + "'"
        cursor.execute(sql1)
        data1 = cursor.fetchall()
        details['req'] = data1[0][0]
        details['desc'] = data1[0][1]
        for detail in data:
            category.append(detail[1])
        for detail1 in data:
            skill = get_list_size(skill, detail1[3])
            voacational = get_list_size(voacational, detail1[4])
            qualification = get_list_size(qualification, detail1[5])
            professional = get_list_size(professional, detail1[6])
            industry = get_list_size(industry, detail1[7])
            function = get_list_size(function, detail1[8])
            seniority = get_list_size(seniority, detail1[9])
        category = set(category)
        skill = set(skill)
        voacational = set(voacational)
        qualification = set(qualification)
        professional = set(professional)
        industry = set(industry)
        function = set(function)
        seniority = set(seniority)
        # details = get_dictionary('category', category, details)
        details['category_1'] = list(category)[0]
        details = get_dictionary('skill', skill, details)
        details = get_dictionary('voacational', voacational, details)
        details = get_dictionary('qualification', qualification, details)
        details = get_dictionary('professional', professional, details)
        details = get_dictionary('industry', industry, details)
        details = get_dictionary('function', function, details)
        details = get_dictionary('seniority', seniority, details)
        print(details)
        return details
    else:
        title1 = ','.join(jieba.cut(title))
        title1 = title1.split(',')
        for second_title in title1:
            sql = "select * from job_entity where titleName LIKE '%" + second_title + "%'"
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:
                sql1 = "select requireDetail, descriptionDetail from jobs where titleName = '" + title + "'"
                cursor.execute(sql1)
                data1 = cursor.fetchall()
                try:
                    details['req'] = data1[0][0]
                    details['desc'] = data1[0][1]
                except:
                    pass
                category1 = list(category)
                for detail1 in data:
                    category1 = [detail1[1]]
                    break
                for detail1 in data:
                    skill = get_list_size(skill, detail1[3])
                    voacational = get_list_size(voacational, detail1[4])
                    qualification = get_list_size(qualification, detail1[5])
                    professional = get_list_size(professional, detail1[6])
                    industry = get_list_size(industry, detail1[7])
                    function = get_list_size(function, detail1[8])
                    seniority = get_list_size(seniority, detail1[9])
                category1 = set(category1)
                skill = set(skill)
                voacational = set(voacational)
                qualification = set(qualification)
                professional = set(professional)
                industry = set(industry)
                function = set(function)
                seniority = set(seniority)
                # details = get_dictionary('category', category1, details)
                details['category_1'] = list(category1)[0]
                details = get_dictionary('skill', skill, details)
                details = get_dictionary('voacational', voacational, details)
                details = get_dictionary('qualification', qualification, details)
                details = get_dictionary('professional', professional, details)
                details = get_dictionary('industry', industry, details)
                details = get_dictionary('function', function, details)
                details = get_dictionary('seniority', seniority, details)
        print(details)
        return details
    data = {'entity': '0'}
    return data


def find_type_category(word):
    categories = ['财务/审计/法务', '客服', '航空', '市场营销', '人资/行政', 'IT']
    if word in categories:
        expressions = get_all_jobs(word)
        return expressions
    else:
        data = {'entity': '0'}
        return data


def find_type_title(word):
    # db = connect_mysql()
    # cursor = db.cursor()
    # sql = "select id from title_csv where name LIKE '%" + word + "%'"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # if data:
    expressions = get_all_detail(word)
    # print(expressions)
    return expressions
    # else:
    #     return '0'


def find_type_potential(word):
    db = connect_mysql()
    cursor = db.cursor()
    sql = "select id from professional where professional LIKE '%" + word + "%'"
    cursor.execute(sql)
    data = cursor.fetchall()
    list_id = []
    list_title = []
    dict_title = {'entity': word}
    if data:
        for index in data:
            list_id.append(index[0])
        list_id = set(list_id)
        for id in list_id:
            sql = "select titleName from job_entity where id = " + str(id)
            cursor.execute(sql)
            data = cursor.fetchall()
            list_title.append(data[0][0])
        list_title = set(list_title)
        dict_title = get_dictionary('job', list_title, dict_title)
        return dict_title
        # print(dict_title)
        # print(len(list_title))
    else:
        title1 = ','.join(jieba.cut(word))
        title1 = title1.split(',')
        for title in title1:
            sql = "select id from professional where professional LIKE '%" + title + "%'"
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:
                for index in data:
                    list_id.append(index[0])
                list_id = set(list_id)
                for id in list_id:
                    sql = "select titleName from job_entity where id = " + str(id)
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    list_title.append(data[0][0])
        list_title = set(list_title)
        dict_title = get_dictionary('job', list_title, dict_title)
        return dict_title
        # print(dict_title)
        # print(len(list_title))
    data = {'entity': '0'}
    return data


def connect_mysql():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='lvgang1997', db='graduate',
                         charset='utf8')
    return db


def get_all_detail_click(title):
    details = {'entity': title}
    category = []
    skill = []
    voacational = []
    qualification = []
    professional = []
    industry = []
    function = []
    seniority = []
    db = connect_mysql()
    cursor = db.cursor()
    sql = "select * from job_entity where titleName = '" + title + "'"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        sql1 = "select requireDetail, descriptionDetail from jobs where titleName = '" + title + "'"
        cursor.execute(sql1)
        data1 = cursor.fetchall()
        details['req'] = data1[0][0]
        details['desc'] = data1[0][1]
        for detail in data:
            category.append(detail[1])
        for detail1 in data:
            skill = get_list_size(skill, detail1[3])
            voacational = get_list_size(voacational, detail1[4])
            qualification = get_list_size(qualification, detail1[5])
            professional = get_list_size(professional, detail1[6])
            industry = get_list_size(industry, detail1[7])
            function = get_list_size(function, detail1[8])
            seniority = get_list_size(seniority, detail1[9])
        category = set(category)
        skill = set(skill)
        voacational = set(voacational)
        qualification = set(qualification)
        professional = set(professional)
        industry = set(industry)
        function = set(function)
        seniority = set(seniority)
        # details = get_dictionary('category', category, details)
        details['category_1'] = list(category)[0]
        details = get_dictionary('skill', skill, details)
        details = get_dictionary('voacational', voacational, details)
        details = get_dictionary('qualification', qualification, details)
        details = get_dictionary('professional', professional, details)
        details = get_dictionary('industry', industry, details)
        details = get_dictionary('function', function, details)
        details = get_dictionary('seniority', seniority, details)
        print(details)
        return details
    else:
        data = {'entity': '0'}
        return data


def get_DNN_score_eng(word):
    # data1 = '富有' + word
    data2 = '熟悉' + word
    data5 = '具备' + word
    score2 = eval(DNN_judge(data2))['ppl']
    score5 = eval(DNN_judge(data5))['ppl']
    random = [(score2, data2), (score5, data5)]
    random.sort()
    print(random)
    return random[0][1]


def get_DNN_score_ch(word):
    data3 = '良好的' + word
    data4 = '熟悉' + word
    score3 = eval(DNN_judge(data3))['ppl']
    score4 = eval(DNN_judge(data4))['ppl']
    random = [(score3, data3), (score4, data4)]
    random.sort()
    print(random)
    return random[0][1]


def get_list_size(list1, detail):
    list1 = list(list1)
    dictionary = {}
    for ele in list1:
        ele_entity = ele.split("#")[0].upper()
        ele_number = int(ele.split("#")[1])
        dictionary[ele_entity] = ele_number
    if detail is not '0':
        detail = list(eval(detail))
        for element in detail:
            element = element.upper()
            if element in dictionary.keys():
                # remove_num = dictionary[element]
                # remove_ele = element + "#" + str(remove_num)
                # list1.remove(remove_ele)
                dictionary[element] = dictionary[element] + 1
            else:
                dictionary[element] = 1
    list2 = []
    # dicts = sorted(dictionary.items(), key=lambda d: d[1], reverse=True)
    # print(dicts)
    for key, value in dictionary.items():
        new_ele = key + "#" + str(value)
        list2.append(new_ele)
    # for value in dicts:
    #     new_ele = value[0] + "#" + str(value[1])
    #     list2.append(new_ele)
    # print(list2)
    return list2


def get_dictionary(name, list, dict):
    try:
        number = 1
        dictionary = {}
        for ele in list:
            ele_entity = ele.split("#")[0].upper()
            ele_number = int(ele.split("#")[1])
            dictionary[ele_entity] = ele_number
        dicts = sorted(dictionary.items(), key=lambda d: d[1], reverse=True)
        list2 = []
        for value in dicts:
            new_ele = value[0] + "#" + str(value[1])
            list2.append(new_ele)
        for deatil in list2:
            key = name + '_' + str(number)
            dict[key] = deatil
            number = number + 1
        return dict
    except:
        number = 1
        for deatil in list:
            key = name + '_' + str(number)
            dict[key] = deatil
            number = number + 1
        return dict


# def get_DNN_score(word):
#     data3 = '熟悉' + word
#     data4 = '较强的' + word
#     score3 = eval(DNN_judge(data3))['ppl']
#     score4 = eval(DNN_judge(data4))['ppl']
#     random = [(score3, data3), (score4, data4)]
#     random.sort()
#     print(random)
#     return random[0][1]


# get_DNN_score("刑法")
# get_all_jobs('人资/行政')
# get_all_detail('应收专员asds')
# find_type('应收专员')
# test_str = '我AAa'
# print(test_str.lower())
# find_type_title('java程序员')
# txt = '管理尼玛'
# a = ','.join(jieba.cut(txt))
# b = a.split(',')
# print(b)
# find_type_potential('管理')
# get_all_detail_click('应收专员')
# get_search("财经类")
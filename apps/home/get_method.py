# from abc import get_cache_token
# from dis import dis
# import re
import numpy as np
import pandas as pd
import pymysql.cursors

def get_top(district, n):
    # 자치구별 top N 추출(리뷰에 의한 평점을 기준으로)
    # Connect to the database
    connection = pymysql.connect(host= 'localhost',
                                port= 3306,
                                user= 'root',
                                password= '1234',
                                database= 'team3',
                                charset='utf8',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # Read Top
            sql = "SELECT info.pid, info.pname, info.photo, df1.new_label FROM df1 LEFT JOIN info ON info.pid=df1.pid WHERE info.district = %s ORDER BY new_label DESC limit %s"
            cursor.execute(sql, (district, n))
            result = cursor.fetchall()
            print(result)



def get_IBF(pid, district):
    # 파일경로 생성
    folder = '../static/assets/filtering_file/'
    # file = f'IBF_{district}.csv'
    file = f'IBF_{district}.csv'
    file_path = folder + file
    ### print(file_path)
    # ibf matrix read
    ibf_matrix = pd.read_csv(file_path)
    temp1 = ibf_matrix.columns.to_list()
    temp2 = ibf_matrix.index.to_list()
    print(ibf_matrix.index.name)
    print(ibf_matrix.columns.name)
    # print(temp1[:5])
    # print(temp2[:5])
    # print(ibf_matrix.head(5))
    print(ibf_matrix.index)
    print(ibf_matrix.columns)

    # 상위 다섯개 추출
    top5 = ibf_matrix[pid].sort_values(ascending=False)[:6]
    print(top5)
    

def get_CBF(pid, district):
    # 파일경로 생성
    folder = '../static/assets/filtering_file/'
    file = f'cbf_{district}.csv'
    file_path = folder + file
    # CBF matrix read
    cbf_matrix = pd.read_csv(file_path)
    # 상위 다섯개 추출
    top5 = cbf_matrix[pid].sort_values(ascending=False)[:6]
    print(type(top5))


if __name__=="__main__":
    get_IBF('323', '강남구')
    # get_CBF('323', '강남구')
    # get_top('강남구', 5)
        


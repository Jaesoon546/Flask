import json
import os
import pymysql

# 접속 정보는 코드에 직접 쓰지 않고 환경변수로 받습니다 (공개 저장소 보호용).
#   export DB_HOST=<서버 IP>  DB_PASSWORD=<비밀번호>
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")

def getConnection():
    return pymysql.connect(host=DB_HOST,port=3306,user='root',password=DB_PASSWORD,
                        database = 'jsdb', charset = 'utf8', autocommit=True)
    
def getSungjuk():
    conn = getConnection()
    cur = conn.cursor()
    cur.callproc("student_select")
    if (cur.rowcount): # 있으면 
        result = cur.fetchall() # 파이썬 형식으로 
        result_rowcount = cur.rowcount 
        print("rowcount=", result_rowcount) # 체크 
    else:
        result = [] # 리스트 초기화 
        print("rowcount=", cur.rowcount)
    cur.close()
    conn.close()
    return result
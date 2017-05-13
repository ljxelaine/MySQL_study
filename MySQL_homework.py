# encoding: utf-8

import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 连接数据库university
conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='elaine19980809',  # 这里要写自己在MySQL的密码
        charset = "utf8",
        db='university',
)

# 获取数据库执行游标
cur = conn.cursor()

# 先读取department.txt文件中的数据,一行一行的读取
f = open("/home/elaine/Desktop/树蛙/university/department.txt","r")
while True:
    line = f.readline()
    #将读取到的数据，用split函数以空格为分隔符，一行一行地分开
    if line:
      line = line.strip("\n")     #去掉读取到的换行符号
      line = line.split(" ")
      print(line)
      dept_name = line[0]
      building = line[1]
      budget = line[2]

      #将三个属性的数据插入到数据库中的department表中
      cur.execute(
      "insert into department(dept_name,building,budget)values(%s,%s,%d)",[dept_name,building,budget])
    else:
       break

#关闭文件
f.close()

#提交操作
conn.commit()

#关闭
conn.close()


#读取exam.txt，并插入exam表中
f = open("/home/elaine/Desktop/树蛙/university/exam.txt","r")
while True:
    line = f.readline()
    if line:
        line = line.strip("\n")
        line = line.split(" ")
        print(line)
        student_ID = line[0]
        exam_name = line[1]
        grade = line[2]
        cur.execute("insert into exam(student_ID,exam_name,grade)values(%d,%s,%d)",[student_ID,exam_name,grade])
    else :
        break


#关闭
f.close()

#提交
conn.commit()

#关闭
conn.close()


#再读取student.txt内的数据，插入数据库中
f = open("/home/elaine/Desktop/树蛙/university/student.txt.txt","r")
while True:
    line = f.readline()
    if line:
        line = line.strip("\n")
        line = line.split(" ")
        print(line)
        ID = line[0]
        name = line[1]
        sex = line[2]
        age = line[3]
        emotion_state = line[4]
        dept_name = line[5]

        #执行插入
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name)values(%d,%s,%s,%d,%s,%s)",[ID,name,sex,age,emotion_state,dept_name])
    else:
        break

#关闭
f.close()

#提交
conn.commit()

#关闭
conn.close()
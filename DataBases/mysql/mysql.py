import _mysql
connection =_mysql.connect(host='localhost',user='root',passwd='test10',db='adventureworks')
connection.query("show tables;")
res = connection.use_result()
print(dir(res))
flag = True
while(flag):
    x = res.fetch_row()[0][0]
    print(x)
    if not x : flag = False

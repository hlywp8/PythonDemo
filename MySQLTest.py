#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      HJJ
#
# Created:     23/08/2013
# Copyright:   (c) HJJ 2013
# Licence:     <your licence>
#Python Version: 2.7.5
#-------------------------------------------------------------------------------
import MySQLdb
def main():
    conn=MySQLdb.connect(user='root',passwd='111111',db='mypythondb',host='127.0.0.1')
    cur=conn.cursor()
    cur.execute("select * from tuser")
    results=cur.fetchall()
    for i in results:
        print(i)
    cur.execute("update tuser set password='333' where id=2")
    conn.commit()
    cur.close()
    conn.close()
if __name__ == '__main__':
    main()

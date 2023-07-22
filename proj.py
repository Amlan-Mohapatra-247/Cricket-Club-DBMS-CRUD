print('Welcome to Club-70')
import mysql.connector as sq
con=sq.connect(host="localhost",user="root",passwd="1234",database="pro12")
cur=con.cursor()
print('Enter 1 for viewing record of a player')
print('Enter 2 for entering a fresh player')
print("Enter 3 for updating a player's record")
print('Enter 4 for removing a player')
f=int(input('Your choice?  '))
if f==1:
    import pandas as pd
    print('Enter 11 for viewing a batsman')
    print('Enter 12 for viewing a bowler')
    q=int(input('Your choice? '))
    if q==11:
        j=input("Enter id of the player you want to view. Enter 'x' if you don't know the id ")
        if j=='x':
            n=input("Enter name of the player ")
            qry1="select * from bat where name='%s'" %(n)
            cur.execute(qry1)
            rows=cur.fetchall()
            w=list(rows[0])
            a=pd.Series(w,index=['ID','NAME','NATIONALITY','RUNS','MATCHES','AVERAGE'])
            print(a)
        else:
            qry="select * from bat where id="+j
            cur.execute(qry)
            rows=cur.fetchall()
            w=list(rows[0])
            a=pd.Series(w,index=['ID','NAME','NATIONALITY','RUNS','MATCHES','AVERAGE'])
            print(a)
    elif q==12:
        j=input("Enter id of the player you want to view. Enter 'x' if you don't know the id ")
        if j=='x':
            n=input("Enter name of the player ")
            qry1="select * from bowl where name='%s'" %(n)
            cur.execute(qry1)
            rows=cur.fetchall()
            w=list(rows[0])
            a=pd.Series(w,index=['ID','NAME','NATIONALITY','WICKETS','MATCHES','WICKETS PER MATCH'])
            print(a)
        else:
            qry2="select * from bowl where id="+j
            cur.execute(qry2)
            rows=cur.fetchall()
            w=list(rows[0])
            a=pd.Series(w,index=['ID','NAME','NATIONALITY','WICKETS','MATCHES','WICKETS PER MATCH'])
            print(a)
    else:
        print("You didn't follow instructions properly")
if f==2:
    h=input("Is he an allrounder( Enter 'y' for yes or 'n' for no )? ")
    if h=='y':
        qr="select max(id) from bat"
        cur.execute(qr)
        r=cur.fetchall()
        r=r[0]
        r=list(r)
        i=r[0]
        i+=1
        n=input("Enter player's name ")
        c=input("Enter his nationality ")
        qry1="insert into bat values(%s,'%s','%s',0,0,NULL)" %(i,n,c)
        cur.execute(qry1)
        qry2="insert into bowl values(%s,'%s','%s',0,0,NULL)" %(i,n,c)
        cur.execute(qry2)
        print('record added')
    elif h=='n':
        print('Enter 21 for entering fresh batsman')
        print('Enter 22 for entering fresh bowler')
        q=int(input('Your choice? '))
        if q==21:
            qr="select max(id) from bat where id not like '___'"
            cur.execute(qr)
            r=cur.fetchall()
            r=r[0]
            r=list(r)
            i=r[0]
            i+=1
            n=input("Enter player's name ")
            c=input("Enter his nationality ")
            qry="insert into bat values(%s,'%s','%s',0,0,NULL)" %(i,n,c)
            cur.execute(qry)
            print('record added')
        elif q==22:
            qr="select max(id) from bowl where id not like '___'"
            cur.execute(qr)
            r=cur.fetchall()
            r=r[0]
            r=list(r)
            i=r[0]
            i+=1
            n=input("Enter player's name ")
            c=input("Enter his nationality ")
            qry="insert into bowl values(%s,'%s','%s',0,0,NULL)" %(i,n,c)
            cur.execute(qry)
            print('record added')
        else:
            print("You didn't follow instructions properly")
    else:
        print("You didn't follow instructions properly")       
if f==3:
    h=input("Is he an allrounder( Enter 'y' for yes or 'n' for no )? ")
    if h=='y':
        i=input("Enter id. Enter 'x' if you don't know the id ")
        if i=='x':
            n=input('Enter name of the player ')
            qry1="select * from bat where name='%s'" %(n)
            cur.execute(qry1)
            rows=cur.fetchall()
            w=list(rows[0])
            i=w[0]
            m=w[4]
            m=m+1
            r=int(input('Enter runs scored in that match '))
            R=w[3]
            r=r+R
            av=r/m
            qry2="update bat set runs=%s, matches=%s, average=%s where id=%s" %(r,m,av,i)
            cur.execute(qry2)
            qry3="select * from bowl where name='%s'" %(n)
            cur.execute(qry3)
            rows=cur.fetchall()
            w=list(rows[0])
            m=w[4]
            m=m+1
            r=int(input('Enter wickets taken in that match '))
            R=w[3]
            r=r+R
            av=r/m
            qry="update bowl set wickets=%s, matches=%s, wickets_per_match=%s where id=%s" %(r,m,av,i)
            cur.execute(qry)
            print('record updated')
        else:    
            qry1="select * from bat where id="+i
            cur.execute(qry1)
            rows=cur.fetchall()
            w=list(rows[0])
            m=w[4]
            m=m+1
            r=int(input('Enter runs scored in that match '))
            R=w[3]
            r=r+R
            av=r/m
            qry2="update bat set runs=%s, matches=%s, average=%s where id=%s" %(r,m,av,i)
            cur.execute(qry2)
            qry="select * from bowl where id="+i
            cur.execute(qry)
            rows=cur.fetchall()
            w=list(rows[0])
            m=w[4]
            m=m+1
            r=int(input('Enter wickets taken in that match '))
            R=w[3]
            r=r+R
            av=r/m
            qry="update bowl set wickets=%s, matches=%s, wickets_per_match=%s where id=%s" %(r,m,av,i)
            cur.execute(qry)
            print('record updated')
    elif h=='n':
        print('Enter 31 for updating batting record')
        print('Enter 32 for updating bowling record')
        q=int(input('Your choice? '))
        if q==31:
            i=input("Enter id. Enter 'x' if you don't know the id ")
            if i=='x':
                n=input('Enter name of the player ')
                qry1="select * from bat where name='%s'" %(n)
                cur.execute(qry1)
                rows=cur.fetchall()
                w=list(rows[0])
                i=w[0]
                m=w[4]
                m=m+1
                r=int(input('Enter runs scored in that match '))
                R=w[3]
                r=r+R
                av=r/m
                qry2="update bat set runs=%s, matches=%s, average=%s where id=%s" %(r,m,av,i)
                cur.execute(qry2)
                print('record updated')
            else:
                qry="select * from bat where id="+i
                cur.execute(qry)
                rows=cur.fetchall()
                w=list(rows[0])
                m=w[4]
                m=m+1
                r=int(input('Enter runs scored in that match '))
                R=w[3]
                r=r+R
                av=r/m
                qry="update bat set runs=%s, matches=%s, average=%s where id=%s" %(r,m,av,i)
                cur.execute(qry)
                print('record updated')
        elif q==32:
            i=input("Enter id. Enter 'x' if you don't know the id ")
            if i=='x':
                n=input('Enter name of the player ')
                qry3="select * from bowl where name='%s'" %(n)
                cur.execute(qry3)
                rows=cur.fetchall()
                w=list(rows[0])
                i=w[0]
                m=w[4]
                m=m+1
                r=int(input('Enter wickets taken in that match '))
                R=w[3]
                r=r+R
                av=r/m
                qry="update bowl set wickets=%s, matches=%s, wickets_per_match=%s where id=%s" %(r,m,av,i)
                cur.execute(qry)
                print('record updated')
            else:    
                qry="select * from bowl where id="+i
                cur.execute(qry)
                rows=cur.fetchall()
                w=list(rows[0])
                m=w[4]
                m=m+1
                r=int(input('Enter wickets taken in that match '))
                R=w[3]
                r=r+R
                av=r/m
                qry="update bowl set wickets=%s, matches=%s, wickets_per_match=%s where id=%s" %(r,m,av,i)
                cur.execute(qry)
                print('record updated')
        else:
            print("You didn't follow instructions properly")
    else:
        print("You didn't follow instructions properly")
if f==4:
    l=input("Is he an allrounder( Enter 'y' for yes or 'n' for no )? ")
    if l=='y':
        i=input("Enter id. Enter 'x' if you don't know the id ")
        if i=='x':
            n=input('Enter name of the player ')
            q1="delete from bat where name='%s'" %(n)
            cur.execute(q1)
            q2="delete from bowl where name='%s'" %(n)
            cur.execute(q2)
            print('record deleted')
        else:
            q1="delete from bat where id=%s" %(i)
            cur.execute(q1)
            q2="delete from bowl where id=%s" %(i)
            cur.execute(q2)
            print('record deleted')
    elif l=='n':
        print("Enter 41 for deleting a batsman's record")
        print("Enter 42 for deleting a bowler's record")
        q=int(input('Your choice? '))
        if q==41:
            i=input("Enter id. Enter 'x' if you don't know the id ")
            if i=='x':
                n=input('Enter name of the player ')
                q1="delete from bat where name='%s'" %(n)
                cur.execute(q1)
                print('record deleted')
            else:            
                q1="delete from bat where id=%s" %(i)
                cur.execute(q1)
                print('record deleted')
        elif q==42:
            i=input("Enter id. Enter 'x' if you don't know the id ")
            if i=='x':
                n=input('Enter name of the player ')
                q1="delete from bowl where name='%s'" %(n)
                cur.execute(q1)
                print('record deleted')
            else:    
                q2="delete from bowl where id=%s" %(i)
                cur.execute(q2)
                print('record deleted')
        else:
            print("You didn't follow instructions properly")
    else:
        print("You didn't follow instructions properly")        
con.commit()
con.close()

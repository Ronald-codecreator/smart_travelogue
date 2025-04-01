from  Dbconnection import Db

def instreenode(nodeid,venueid,distance,parentnodeid,level):

    qry="INSERT INTO `tree`(nodeid,`venueid`,`distance`,`parentnodeid`,`level`)VALUES('"+str(nodeid)+"','"+str(venueid)+"','"+str(distance)+"','"+str(parentnodeid)+"','"+str(level)+"')"
    db=Db()
    res=db.insert(qry)

def getparentnodeid(nodeid):
    qry="SELECT `parentnodeid` FROM `tree` WHERE `nodeid`='"+str(nodeid)+"'"
    db=Db()
    res=db.selectOne(qry)
    return  res['parentnodeid']

def getleafnodeidies():
    qry="SELECT `nodeid` FROM `tree` WHERE `nodeid` NOT IN (SELECT `parentnodeid` FROM `tree`)"
    db=Db()
    res=db.select(qry)
    nodeid=[]
    for i in res:
        nodeid.append(i['nodeid'])

    return nodeid






def getfullpathofparentnodeid(nodeid):

    path=[]

    n=int(nodeid)
    # path.append(n)

    while n>0:


        parentnodeid=getparentnodeid(str(n))
        path.append(n)
        n=parentnodeid

    return path



def getvenuebycategoryid(catid):
    qry="SELECT `venue_id` FROM `venue` WHERE `category_id`='"+str(catid)+"'"
    db=Db()
    res=db.select(qry)
    venueid = []
    for i in res:
        venueid.append(i['venue_id'])

    return venueid

def getnodeidbylevel(level):
    qry="SELECT `nodeid` FROM `tree` WHERE `level`='"+str(level)+"'"
    db = Db()
    res = db.select(qry)
    nodeid = []
    for i in res:
        nodeid.append(i['nodeid'])

    return nodeid


def getdistancebetweentwocord(la1,lo1,la2,lo2):
    from geopy.distance import geodesic
    newport_ri = (la1,lo1)
    cleveland_oh = (la2,lo2)
    s=geodesic(newport_ri, cleveland_oh).kilometers
    print("computed distance", la1,lo1,la2,lo2,s )
    return s


from Constants import connString
import pyodbc
import datetime
import uuid
import time    

class RoleModel:
    def __init__(self, roleID = 0,roleName = '',canRole = False,canUsers = False,canApprovedBy = False,canDocumentHolder = False,canUploadedBy = False):
        self.roleID = roleID
        self.roleName = roleName
        self.canRole = canRole
        self.canUsers = canUsers
        self.canApprovedBy = canApprovedBy
        self.canDocumentHolder = canDocumentHolder
        self.canUploadedBy = canUploadedBy
       
        

    @staticmethod
    def get_all():
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "SELECT * FROM Role ORDER BY roleName"
        cursor.execute(sqlcmd1)
        records = []
        for dbrow in cursor.fetchall():
            row = RoleModel(dbrow[0],dbrow[1],dbrow[2],dbrow[3],dbrow[4],dbrow[5],dbrow[6])
            records.append(row)
        cursor.close()
        conn.close()
        return records

    @staticmethod
    def get_name_id():
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "SELECT roleID, roleName FROM Role ORDER BY roleName"
        cursor.execute(sqlcmd1)
        records = []
        for dbrow in cursor.fetchall():
            row = RoleModel(dbrow[0],dbrow[1])
            records.append(row)
        cursor.close()
        conn.close()
        return records
        
    @staticmethod
    def get_by_id(unique_id):
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "SELECT * FROM Role WHERE roleID = ?"
        cursor.execute(sqlcmd1, unique_id)
        record = None
        for dbrow in cursor.fetchall():
            record = RoleModel(dbrow[0],dbrow[1],dbrow[2],dbrow[3],dbrow[4],dbrow[5],dbrow[6])
        cursor.close()
        conn.close()
        return record
    
    @staticmethod
    def insert(obj):
        obj.roleID = str(uuid.uuid4())
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "INSERT INTO Role (roleName,canRole,canUsers,canApprovedBy,canDocumentHolder,canUploadedBy) VALUES(?,?,?,?,?,?)"
        cursor.execute(sqlcmd1, (obj.roleName,obj.canRole,obj.canUsers,obj.canApprovedBy,obj.canDocumentHolder,obj.canUploadedBy))
        cursor.close()
        conn.close()
        
    
    @staticmethod
    def update(obj):
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "UPDATE Role SET roleName = ?,canRole = ?,canUsers = ?,canApprovedBy = ?,canDocumentHolder = ?,canUploadedBy = ? WHERE roleID = ?"
        cursor.execute(sqlcmd1,  (obj.roleName,obj.canRole,obj.canUsers,obj.canApprovedBy,obj.canDocumentHolder,obj.canUploadedBy,obj.roleID))
        cursor.close()
        conn.close()
    
    @staticmethod
    def delete(unique_id):
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "DELETE FROM Role WHERE roleID = ?"
        cursor.execute(sqlcmd1, (unique_id))
        cursor.close()
        conn.close()


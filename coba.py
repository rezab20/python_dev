import psycopg2

class connections:
    __HOST = '127.0.0.1'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DATABASE = 'dvd_rental'

    def __init__(self):

        self.conn = psycopg2.connect(host= connections.__HOST, user=connections.__USERNAME,
                                     password = connections.__PASSWORD, database=connections.__DATABASE)
    def connect_db(self, username, password):
        pass_check = []
        psql_query = "SELECT * FROM staff WHERE username = '%s' AND password = '%s' " %(username,password)
        curr = self.conn.cursor()
        
        try:
            curr.execute(psql_query)
            result = curr.fetchall()
            for row in result:
                for x in row:
                    pass_check.append(x)
        except:
            print('error')
        if(username and password) in pass_check:
            print('Login Success!')
        else:
            print('Invalid Username/Password')
check = connections()
usr = input("Username: ")
passwd = input("Password: ")
login_success = check.connect_db(usr, passwd)
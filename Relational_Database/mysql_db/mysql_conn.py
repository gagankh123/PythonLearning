import mysql.connector as conn
from mysql_db import strings

class mysql_connection:
    '''
    
    '''
    def __init__(self):
        '''
        
        '''
        self.conn = conn.connect(
            host = strings.str_host,
            user= strings.str_user,
            password= input('Enter MySQL DB Password: '),
            auth_plugin= strings.str_auth_plugin
        )
        self.mysql = self.conn.cursor(buffered=True)
    
    def _commit(self, close=True):
        '''
        
        '''
        self.conn.commit()
        if close:
            self._close(close=close)
    
    def _close(self, close=True):
        self.conn.close()

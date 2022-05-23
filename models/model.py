import sqlite3
from typing import List, Tuple

class Queries:
    
    def add_user(self, first_name: str, last_name: str):
        self.c.execute(f'INSERT INTO {self.student_tb_name}(first_name, last_name) VALUES("{first_name}", "{last_name}")')
        self.conn.commit()
    
    def select_user_by_pk(self, pk: int):
        self.c.execute(f'SELECT * FROM {self.student_tb_name} WHERE student_id = {pk}')
        return self.c.fetchall()

    def delete_user_by_pk(self, pk: int):
        self.c.execute(f'DELETE FROM {self.student_tb_name} WHERE student_id = {pk}')
        self.conn.commit()
    
    def update_user_by_pk(self, pk: int, first_name: str = None, last_name: str = None, math: int = None, history: int = None, biology: int = None, sports: int = None):
        if first_name: self.c.execute(f'UPDATE {self.student_tb_name} SET first_name = "{first_name}" WHERE student_id = {pk}')
        if last_name: self.c.execute(f'UPDATE {self.student_tb_name} SET last_name = "{last_name}" WHERE student_id = {pk}')
        if math: self.c.execute(f'UPDATE {self.student_tb_name} SET math = {math} WHERE student_id = {pk}')
        if history: self.c.execute(f'UPDATE {self.student_tb_name} SET history = {history} WHERE student_id = {pk}')
        if biology: self.c.execute(f'UPDATE {self.student_tb_name} SET biology = {biology} WHERE student_id = {pk}')
        if sports: self.c.execute(f'UPDATE {self.student_tb_name} SET sports = {sports} WHERE student_id = {pk}')
        self.conn.commit()
        
    def query(self):
        self.c.execute(f'SELECT * FROM {self.student_tb_name}')
        return self.c.fetchall()
        
class Model(Queries):
    
    def __init__(self, db_name: str = 'school.db', student_tb_name: str = 'students') -> None:
        self.db_name, self.student_tb_name = db_name, student_tb_name
        
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.c = self.conn.cursor()
        self.__create_students_tb()
        
    def __create_students_tb(self):
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.student_tb_name}(
                       student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       first_name TEXT,
                       last_name TEXT,
                       math INTEGER DEFAULT 0,
                       history INTEGER DEFAULT 0,
                       biology INTEGER DEFAULT 0,
                       sports INTEGER DEFAULT 0)
                       ''')
        self.conn.commit()


model = Model()



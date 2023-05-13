import os
import sqlite3


def get_filepath_Name(filepath):
    path = os.path.split(filepath)
    name = os.path.splitext(path[1])
    return name[0]


def get_file_path_timestrip(filename):
    str = filename.split('-')[1]
    str_hour = int(str.split('点')[0])
    str_min = int(str.split('点')[1].split('分')[0])
    str_sec = int(str.split('点')[1].split('分')[1].split('秒')[0])

    return filename.split('-')[1], str_hour, str_min, str_sec


def get_id(hour, min, sec):
    if hour < 8 or (hour == 8 and min == 0 and sec == 0):
        return 1
    elif hour < 16 or (hour == 16 and min == 0 and sec == 0):
        return 2
    elif hour < 24 or (hour == 0 and min == 0 and sec == 0):
        return 3


def Add_Sqiltedatabase(filename):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       seq                 INT     NOT NULL,
       filename           TEXT    NOT NULL,
       hour               INT     NOT NULL,
       min                INT     NOT NULL,
       sec                INT     NOT NULL);''')
    conn.commit()
    conn.close()

    time_str, hour, min, sec = get_file_path_timestrip(filename)
    id = get_id(hour, min, sec)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO data (seq,filename, hour, min, sec) \
          VALUES ('%d','%s', '%d', '%d', '%d')" % (id, filename, hour, min, sec))
    conn.commit()
    conn.close()

def load_database(filepath,id):
    # 读取数据库
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE seq = '%d'" % (id))
    data = c.fetchall()
    conn.close()
    return data

def data_by_line(data):
    for i in range(len(data)):
        data[i] = data[i][2]
    return data

if __name__ == '__main__':
    # Add_Sqiltedatabase('2011年12月24日-01点26分43秒')
    # Add_Sqiltedatabase('2011年12月24日-07点26分43秒')
    data = load_database('database.db',1)
    data1 = data_by_line(data)
    print(data1)
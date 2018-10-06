


def read_data():
    f = open('passwd_dict.txt','r')
    data=f.readlines()
    f.close()
    return data

def write_data(data):
    f = open('f_data.py','w')
    f.write(str(data))
    f.close()


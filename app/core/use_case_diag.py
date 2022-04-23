import os

def file_exists(filename):
    #判断文件是否存在
    if(filename==None):
        return False
    if(os.path.exists(filename) is False):
        print('文件不存在！')
        return False
    return True

def findStr(file_name, str):
    with open(file_name, 'r', encoding="utf8") as file:
        count = 0

        #对每行数据进行查找
        for line in file.readlines():
            time = line.count(str)
            count += time
        return count

def getActorandUseCase(file_name):
    # 判断文件存在
    if (file_exists(file_name) is False):
        return {'code':322, 'msg': "Input File Error!"}

    #查找执行者
    actor_count = findStr(file_name, "<o:Actor Id")
    #查找用例
    use_case_count = findStr(file_name, "<o:UseCase Id")

    print('Actor count: ', actor_count)
    print('Use case count: ', use_case_count)
    return{'code':200, 'actor': actor_count, 'use_case': use_case_count}

if __name__ == '__main__':
    file_name = "D:\diagram\CCMS.oom"
    getActorandUseCase(file_name)
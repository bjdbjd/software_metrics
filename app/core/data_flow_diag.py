import os

def file_exists(filename):
    #判断文件是否存在
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

def getMcCabe(file_name):
    # 判断文件存在
    if (file_exists(file_name) is False):
        os.kill()

    # 查找开始节点数
    start_count = findStr(file_name, "<o:Start Id")
    # 查找终止节点数
    end_count = findStr(file_name, "<o:End Id")
    # 查找操作数
    oper_count = findStr(file_name, "<o:Activity Id")
    # 查找判断数
    dec_count = findStr(file_name, "<o:Decision Id")
    # 查找边数
    flow_count = findStr(file_name, "<o:ActivityFlow Id")

    # 计算圈复杂度，分别为边数-节点数+2及判断数+1
    McCabe_2 = flow_count - (oper_count + dec_count + start_count + end_count) + 2
    McCabe_3 = dec_count + 1

    # 验证
    if (McCabe_2 == McCabe_3):
        return([{'McCabe': McCabe_2}])
    else:
        return([{'message': "wrong input image!"}])


if __name__ == '__main__':
    file_name = "D:\diagram\ControlFlowDiagram.oom"

    getMcCabe(file_name)
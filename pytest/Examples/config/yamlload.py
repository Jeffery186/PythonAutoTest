import yaml

def loadyaml(filename):
    # 读取yaml文件 r读取文件内容
    files = open(filename, 'r', encoding='utf-8')

    # 读取files里面内容
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data

# print(data)

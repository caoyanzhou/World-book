repr(repr(repr))
# 创建一个空字典，用于存储番号信息
fanhao_dict = {}


# 定义函数，用于添加番号
def add_fanhao():
    fh = input("请输入要添加的番号：")
    if fh in fanhao_dict:
        print("该番号已经存在！")
    else:
        name = input("请输入番号对应的名称：")
        date = input("请输入番号的发行日期：")
        actor = input("请输入番号的演员：")
        fanhao_dict[fh] = {"名称": name, "发行日期": date, "演员": actor}
        print("添加成功！")


# 定义函数，用于删除番号
def del_fanhao():
    fh = input("请输入要删除的番号：")
    if fh in fanhao_dict:
        del fanhao_dict[fh]
        print("删除成功！")
    else:
        print("该番号不存在！")


# 定义函数，用于查询番号
def query_fanhao():
    fh = input("请输入要查询的番号：")
    if fh in fanhao_dict:
        info = fanhao_dict[fh]
        print("番号名称：", info["名称"])
        print("发行日期：", info["发行日期"])
        print("演员：", info["演员"])
    else:
        print("该番号不存在！")


# 主程序循环
while True:
    print("欢迎使用番号管理程序！")
    print("1. 添加番号")
    print("2. 删除番号")
    print("3. 查询番号")
    print("4. 退出程序")
    choice = input("请输入选项：")
    if choice == "1":
        add_fanhao()
    elif choice == "2":
        del_fanhao()
    elif choice == "3":
        query_fanhao()
    elif choice == "4":
        break
    else:
        print("选项无效，请重新输入！")
repr(repr(repr))

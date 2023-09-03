import os
import shutil

# 定义要分类的文件夹和关键词-文件夹映射
folder_mapping = {
    '10150830z': '一诺',
    '80228226578': '金的绿',
    '71847920366': '香菜噗噗',
    '68947529465': '老王酱',
    '52441256350': '老婆饼不要老婆',
    '20613836096': '腋毛且66',
    '75542917740': '腋毛且66',
    '35816651471': '宝云朵花',
    '75819948301': '白狮子',
    'CYN6129': '白狮子',
    '84355641338': '是小朱吖房产',
    'mengmeng577017': '是小朱吖房产',
    '6666666Hly': '葫芦爱健身',
    'tingtingyuzhinan': '婷婷与直男',
    'Xiaomaomie666': 'DJ小奶猫',
    '0110Yolo': '悲伤tomato（张璇）',
    'Yolo0110': '悲伤tomato（张璇）',
    '22514191177': '大飞起来了',
    '60141447035': '杂鱼川',
    'dy14gannku894': '杂鱼川',
    'ysy_cz': '川子哥（杨诗语）',
    'xiaolukxy': '小璐来了',
    'Wk0108._': '王雪儿',
    'Wan050208': '一碗米',
    'mili0208': '一碗米',
    'Fanfan0208': '一碗米',
    'swbz0327': '蛇尾巴猪',
    'swbz8208': '蛇尾巴猪',
    'showworld0609': '湫骊',
    'shanyuan802': '珍妮',
    'senterzz': '轩美丽',
    'Queenshou': 'LISA大漂亮',
    'qq.mma': '郭小包',
    'Q111369': '齐一昂',
    'preciousfan': '徐凡凡',
    'nng397': '万能皮',
    'nan20180507': '叫楠哥',
    'MH564564': '美子~',
    'LYX_20010404': '白羊羊',
    'lqylqy888': '玉玉',
    'LQ30466': '说什么我听不清（李清/李雪妮）',
    'linxi357': '林希',
    'Linchuyi': '林初一',
    'Liiiihoo': 'Liiiihoo',
    '7639465': 'Liiiihoo',
    'Ligeantong520': 'Lovely彤宝',
    'Ligeantong21': 'Lovely彤宝',
    'jss88800':'金瘦瘦',
    'hanenxi0827': '韩筱熙',
    'hanxiaoxi0827': '韩筱熙',
    'hahah07': '一条有志向的🐟',
    'belleee23': '张贝儿',



}

# 输入文件夹和输出文件夹路径
input_folder = 'E:\桌面\手机相册8月29日'
output_base_folder = 'E:\桌面\手机相册8月29日'

# 遍历输入文件夹中的文件
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    # 检查文件是否是文件而不是文件夹
    if os.path.isfile(file_path):
        for keyword, output_folder_name in folder_mapping.items():
            # 如果关键词在文件名中，将文件移动到相应的输出文件夹
            if keyword in filename:
                output_folder = os.path.join(output_base_folder, output_folder_name)
                os.makedirs(output_folder, exist_ok=True)
                output_path = os.path.join(output_folder, filename)
                shutil.move(file_path, output_path)
                break

print("已完成")

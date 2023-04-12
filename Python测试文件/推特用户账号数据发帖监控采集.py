# coding='utf-8'

import random
import xlsxwriter as xw
import time

from lxml import etree

from selenium import webdriver


def open_web_driver():
    '''打开浏览器'''
    # browser = webdriver.Chrome()
    # file_path = r'C:\Users\zsjw03\AppData\Roaming\Mozilla\Firefox\Profiles\gr2556xd.default'
    # # 保留浏览器的设置，即相关cookies，下次直接跳过登陆访问页面
    # fp = webdriver.FirefoxProfile(file_path)
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser


def close_web_driver(browser):
    '''关闭浏览器'''
    browser.quit()


def driver_scroll(driver, url, keyword,zong_sums):
    '''模拟浏览器操作请求页面信息，滚动条可设置，滚动位置可设置'''
    try:
        browser.get(url)
    except:
        pass


    time.sleep(18)
    scroll_step_list=[1600]

    # 从第二行写入
    sums = zong_sums
    set_list = []
    ks = 1
    # 结束条件
    js_sum = 1
    # 结束事件二
    js2 = 1
    bczz = 1
    k11 = 1
    for i in range(5000000):
        # 报错终止
        try:
            browser.execute_script("window.scrollBy(0, {});".format(scroll_step_list[0]))
            # browser.execute_script("window.scrollTo(0, 300);")
            # browser.execute_script("window.scrollTo")
            time.sleep(random.randint(15, 20))
            # parser_tweets_info(driver.page_source, keyword)
            # 从第二行写入

            # 数据入库
            if '没有符合搜索条件的结果' in driver.page_source:
                print("没有符合搜索条件的结果-----------")
                return

            html = etree.HTML(driver.page_source)
            tweets_list = html.xpath("//div[@class='css-1dbjc4n']/article/div/div/div/div[2]/div[2]")
            # print('tweets_list',tweets_list)
            # 推特账号昵称
            # //div[@class='css-1dbjc4n r-1ifxtd0 r-ymttw5 r-ttdzmv']/div[2]/div/div/div[1]/div/span/span/text()
            name = html.xpath(
                "//div[@class='css-1dbjc4n r-1ifxtd0 r-ymttw5 r-ttdzmv']/div[2]/div/div/div[1]/div/span/span/text()")[0]

            print('共', len(tweets_list), '数据')
            if len(tweets_list) == 0:
                print(keyword,'没有发表帖子或受保护！')
                # 0 代表没有发表帖子或受保护！
                row = 'A' + str(sums)
                wsheet1.write_row(row, [keyword,'无','无','无','没有发表帖子或受保护！','无',0,0,0])
                # print("***********",list_data)
                # print('第', sums - 1, '页数据', 'list_data>>>>>>', list_data)
                print('******第', sums - 1, '条数据******')
                sums += 1
                return sums
            sum11 = 0
            for tweet_info in tweets_list:
                # 写入的数据列表
                list_data = []
                set_list1 = []
                # 账号ID
                id = keyword  # id
                list_data.append(id)
                print(id)
                # 账号昵称
                list_data.append(name)
                # print(name)
                # print('tweet_info',tweet_info)
                # 发布时间
                Time = tweet_info.xpath('.//a/time/text()')[0]
                print('Time----',Time)
                # 需要改
                # 12小时转日期
                try:
                    if Time[-1] == '钟':
                        TTime = time.time()
                        xs = int(Time.split('分钟')[0])
                        sjc = xs * 60
                        dq_time = TTime - sjc
                        now_data = time.strftime('%m月%d日 %H:%M', time.localtime(dq_time))
                        now_date = now_data[1:]
                        list_data.append(now_date)
                    else:
                        TTime = time.time()
                        xs = int(Time.split('小时')[0])
                        print('xs',xs)
                        sjc = xs * 60 * 60
                        dq_time = TTime - sjc
                        now_data = time.strftime('%m月%d日 %H:%M', time.localtime(dq_time))
                        now_date = now_data[1:]
                        list_data.append(now_date)
                    # TTime = time.time()
                    # xs = int(Time.split('小时')[0])
                    # sjc = xs * 60 * 60
                    # dq_time = TTime - sjc
                    # now_data = time.strftime('%m月%d日 %H:%M', time.localtime(dq_time))
                    # now_date = now_data[1:]
                    # list_data.append(now_date)
                except:
                    # 本月数据写入
                    try:
                        by = int(Time.split('月')[0])
                        if by == 8:
                            list_data.append(Time)
                        else:
                            print("不是本月数据！不保存",js2)
                            js2 +=1
                            if js2 == 15:
                                print(id,'****共',sums-2,'条数据****')
                                time.sleep(random.randint(50, 60))
                                return sums
                            else:
                                continue
                    except:
                        if k11 == 8:
                            print(id, '****共', sums - 2, '条数据****')
                            time.sleep(random.randint(40, 50))
                            return sums
                        else:
                            print("----年开头不是本月数据！----",k11)
                            k11 += 1
                            continue


                set_list1.append(Time)

                # print('list_data2', list_data)
                # 发布标题
                # //div[2]/div[@class='css-1dbjc4n']/div[@class='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']//text()
                data_biaoti = tweet_info.xpath(
                    ".//div[2]/div[@class='css-1dbjc4n']/div[@class='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']//text()")
                # print(data_biaoti)
                # data_biaoti
                # print('data_biaoti:',data_biaoti)

                biaoti = "".join(data_biaoti)
                print(biaoti)
                list_data.append(biaoti)
                set_list1.append(biaoti)

                # 内容
                try:
                    # 读取内容文本
                    data_neirong = tweet_info.xpath(
                        ".//div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']//text()")
                    # print('data_neirong>>>>>>>>>>>>>',data_neirong)
                    if data_neirong == []:
                        neirong = '图片'
                    else:
                        neirong = "".join(data_neirong)
                    # print(neirong)
                    list_data.append(neirong)
                    # 读取内容图片链接
                    # imgs = tweet_info.xpath(".//div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']//text()")
                    # for img in imgs:
                    #     list_data.append(img)
                except:
                    neirong = '内容提取有误！'
                    list_data.append(neirong)
                    # imgs = tweet_info.xpath(".//div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']//text()")
                    # for img in imgs:
                    #     list_data.append(img)

                # 推文链接
                lianjie = tweet_info.xpath(".//div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n r-zl2h9q']/div[1]/div/a/@href")[0]
                # https://twitter.com/ConfuciusNZ/status/1400768126665457664
                data_lianjie = 'https://twitter.com' + lianjie
                print(data_lianjie)
                list_data.append(data_lianjie)
                set_list1.append(data_lianjie)
                # 评
                try:
                    ping_data1 = tweet_info.xpath(
                        ".//div[3]/div/div[1]/div/div//text()")[
                        0]
                    if ',' in ping_data1:
                        ping = ping_data1.replace(',', '')
                    elif '万' in ping_data1:
                        ping2 = ping_data1.replace('万', '')
                        ping = float(ping2) * 10000
                    else:
                        ping = ping_data1
                    print('ping', ping)
                    list_data.append(int(ping))
                except:
                    ping_data1 = 0
                    print(ping_data1)
                    list_data.append(ping_data1)
                # 转
                try:
                    zhuan_data1 = tweet_info.xpath(
                        ".//div[3]/div/div[2]/div/div//text()")[
                        0]
                    if ',' in zhuan_data1:
                        zhuan = zhuan_data1.replace(',', '')
                    elif '万' in zhuan_data1:
                        zhuan2 = zhuan_data1.replace('万', '')
                        zhuan = float(zhuan2) * 10000
                    else:
                        zhuan = zhuan_data1
                    print('zhuan', zhuan)
                    list_data.append(int(zhuan))
                except:
                    zhuan_data1 = 0
                    list_data.append(zhuan_data1)
                # 赞
                try:
                    zan_data1 = tweet_info.xpath(
                        ".//div[3]/div/div[3]/div/div//text()")[
                        0]
                    # print('zan',zan_data1)
                    if ',' in zan_data1:
                        zan = zan_data1.replace(',', '')
                    elif '万' in zan_data1:
                        zan2 = zan_data1.replace('万', '')
                        zan = float(zan2) * 10000
                    else:
                        zan = zan_data1
                    print('zan',zan)
                    list_data.append(int(zan))
                except:
                    zan_data1 = 0
                    list_data.append(zan_data1)

                # 账号主页链接
                list_data.append(url)
                # 判断数据是否到底
                if set_list1 in set_list:
                    # print("*******已重复获取*********",sum11)
                    # print('set_list1',set_list1)
                    sum11 += 1
                    if sum11 == len(tweets_list):
                        print("<<<<<<<<<<<<<数据页面重复",js_sum,'次>>>>>>>>>>>>>>')
                        js_sum +=1
                        if js_sum ==3:
                            print(id,'****共',sums-2,'条数据****')
                            time.sleep(random.randint(50, 65))
                            return sums
                else:
                    # print('list_data1',list_data)
                    set_list.append(set_list1)
                    row = 'A' + str(sums)
                    wsheet1.write_row(row, list_data)
                    # print("***********",list_data)
                    # print('第', sums - 1, '页数据', 'list_data>>>>>>', list_data)
                    print('******第', sums - 1, '条数据******')
                    sums += 1
                    # print('set_list>>>>>>>>>>>>',set_list)
                    # print('set_list1>>>>>>>>>>>>',set_list1)

            # scroll_step_list[0]=(browser.execute_script("return document.body.scrollHeight;"))
        except Exception as e:
            time.sleep(random.randint(10, 20))
            print("数据有误！",e,bczz)
            bczz +=1
            if bczz == 4:
                row = 'A' + str(sums)
                wsheet1.write_row(row, [keyword,'id无发布账号','无','无','无','无',0,0,0])
                # print("***********",list_data)
                # print('第', sums - 1, '页数据', 'list_data>>>>>>', list_data)
                print('******第', sums - 1, '条数据******')
                sums += 1
                print('****共', sums - 2, '条数据****')
                time.sleep(random.randint(10, 15))
                return sums
        ks += 1

    print('下拉循环结束！！下一位------')



def main(browser, keyword_list=None):

    global wbook
    # wbook = xw.Workbook('师资处--亚非（发声途径）推特数据4月.xlsx')
    # wbook = xw.Workbook('师资处--欧洲教师自愿者推特数据4月.xlsx')
    # wbook = xw.Workbook('师资处--欧洲教师自愿者推特数据4月.xlsx')
    # wbook = xw.Workbook('师资处--亚非（发声途径）推特数据8月.xlsx')
    wbook = xw.Workbook('美大地区自媒体推特账号数据8月.xlsx')
    # wbook = xw.Workbook('缺失interpretaatioo.xlsx')
    global wsheet1
    wsheet1 = wbook.add_worksheet('Sheet1')  # 创建工作表
    wsheet1.activate()  # 激活表
    title = ['账号ID', '发布账户', '时间', '标题', '发帖内容','发帖链接', '评论量', '转发量','点赞量','账号主页链接']  # 设置表头
    wsheet1.write_row('A1', title)  # 从A1单元格写入表头
    # 志愿者处推特账号数据4月.xlsx
    # keyword_list = ['0327Gul','daisy','hann_lh','lenka','Maggie','nanCy','Rachlai','yang','limonian0617','louissssssmile','PzEnll','Benice58179573','Lydia69299359','CedricChang7','GatheringV','PeipeiZhang610','YeyeYzw','amandaypj','elie50651039','qingaqing1','63X4tttxq4MXArA','Bless_Lucky_','cccccci9','ErjinP','FionaYue3','HCaixiang','HUIZI92123','JOJO61611444','kepluence','Liana63845353','Lily_haruharu','maria03024','MWangcito','Nicolee59490329','SallyYangyang','Yvonne45364843','yyybeier','ZhangFang666','zorazc2625','1S3ihe790TII317','Aria96367818','Cabiwoo0618','Christi63119299','cswsantiniketan','DawnMarrrr','DeonLeowzk','djS8fYXDvKwgypG','Eleven42835322','Esquilo_Hanz','Estella58429332','Eva12291209','ft1sLE1dLRE3kCF','fugui42112644','Heya_rong','Ivyki2','Jene38893014','Jia49537324','jiamin84403979','jiumia','JKmuCqWGq24PKrF','junjunjingsheng','Kiki44204778','KishiShen','LIANGYU99531912','LiChen92047456','lily91152252','lilyc_loveart','Lilytan16722889','LingzhiWang6','linpinru2020','Lowboom233','LuluAdela_Yu','mingduo4','Nadya83567533','Niki22878835','peng34114638','qinqinlin7','queyuhe','saijun_jin','shanshan_meow','Siqin52813699','sourfishxy','svenjaindeu','TreeSerene','yizhidaidai','YueyuanChen230','YvetteYu1','zfW4b8j97KdO4eB','Zhang26999732','Melon75275430','a402651181','diego87122390','5v2qcDHGu9Khl4','LilihuangSA','della08231','Jasnelly','Delia','chen0801','esytella1','alisony','ciellexd','AliciaChen','dilidili','ChelseaDSQ','ahuang','Felicia','forence','LeoLiu','Anitawbb','BRAD_SHEN','fusuluobo','kun_hoa','Cecilia_S','jingyi_qin','win_y','LILAS','MAYMAY','Xuejiao91551097','Meiya20532615','Ximena0707','oneday','Yenni','liuying']
    # 第二行开始写入
    zong_sums = 2

    for keyword in keyword_list:
        # search_url = "https://twitter.com/search?f=live&q=coronavirus%20until%3A2020-01-31%20since%3A2020-01-30&src=typed_query".format(keyword)  #中文搜索
        # search_url = """https://twitter.com/search?q="{}"%20-"约炮"-%20until%3A2020-12-06%20since%3A2020-06-01&src=typed_query&f=live""".format(keyword)  # 不限语言
        search_url = "https://twitter.com/{}".format(keyword)
        print("正在获取用户【{}】下的推特信息----".format(keyword), '\n', search_url)
        time.sleep(2)

        try:
            print('browser',browser)
            # driver_scroll(browser, search_url, keyword, zong_sums)
            zong_sums = driver_scroll(browser, search_url, keyword, zong_sums)
            print('zong_sums:',zong_sums)
        except Exception as WebDriverErr:
            print("模拟出错！", WebDriverErr)
            continue
        # break
    wbook.close()

if __name__ == '__main__':
    # main()  Rachlai
    domain_name = 'https://twitter.com'
    browser = open_web_driver()
    try:
        main(browser)
    except Exception as mainErr:
        print(mainErr)
        close_web_driver(browser)
    close_web_driver(browser)
    print("本轮抓取结束，请等待s进入下一轮抓取!!!")
    # while True:
    #     browser = open_web_driver()
    #     try:
    #         main(browser)
    #     except Exception as mainErr:
    #         print(mainErr)
    #         close_web_driver(browser)
    #         continue
    #     close_web_driver(browser)
    #     t = random.randrange(60, 100)
    #     print("本轮抓取结束，请等待{}s进入下一轮抓取!!!".format(t))
    #     time.sleep(t)
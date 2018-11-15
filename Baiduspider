# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random
import time
import os
import urllib2
from lxml import etree
from conf import db,conn


class Baidu():
    def get_header(self):

        use_header = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        ]
        uer_agent = random.choice(use_header)
        return uer_agent

    def get_html(self,url):
        header={
            'Referer':'https://xin.baidu.com/',
            'User-Agent': self.get_header()
        }
        print(url)
        req = urllib2.Request(url, headers=header)
        response = urllib2.urlopen(req, None, timeout=10)
        html = response.read()
        code = response.getcode()
        if code != 200:
            print("访问失败，请换ip")
        else:
            error = '<head><meta charset="utf-8"><title>百度企业信用</title><meta name="keywords" content="信用,百度企业信用,企业信用查询,企业信用,企业名查询,注册号查询,法定代表人查询,工商信息查询" /><meta name="description" content="百度企业信用是百度推出的实用企业信用信息查询工具,提供最全最新的企业信息实时查询，可以查询企业相关的工商信息、股东、主要成员、变更记录、网站备案、对外投资、分支机构、年报、风险警示、口碑舆情信息；提供北京、上海、广州、武汉、河南、河北、浙江、安徽、山东、湖南等全国企业工商信息,公司工商注册登记信息信用查询服务以及企业诉讼，商标和专利信息查询。" />'
            result = error in html
            if result is not True:
                print(result)
                # print(html)
                return html
            else:
                Baidu().get_ip()
                # Baidu().run(key)

    def get_home_html(self,html):
        html1 = etree.HTML(html)
        # print(html1)
        try:
            div_list = html1.xpath('//*[@class="zx-list-wrap"]/div')[0]
            url = div_list.xpath('.//div[@class="zx-ent-items"]/h3/a/@href')[0]
            return url
        except:
            pass
    def get_details_html(self,html):
        html1 = etree.HTML(html)
        details_list = {}

        # 公司名
        details_list['name'] = html1.xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/span/text()')[0]
        # 注册号
        details_list['cieat']=  html1.xpath('//*[@id="basic"]/div[2]/p[2]/text()')[0]
        # 组织机构编号
        try:
            a = u'\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801\u2003' # 组织机构编码
            ins1 = html1.xpath('//*[@id="basic"]/div[2]/p[2]/span/text()')[0]
            ins2 = html1.xpath('//*[@id="basic"]/div[2]/p[3]/span/text()')[0]
            ins3 = html1.xpath('//*[@id="basic"]/div[2]/p[4]/span/text()')[0]
            if ins1 == a:
                details_list['institution'] = html1.xpath('//*[@id="basic"]/div[2]/p[2]/text()')[0]
            elif ins2 == a:
                details_list['institution'] = html1.xpath('//*[@id="basic"]/div[2]/p[3]/text()')[0]
            elif ins3 == a:
                details_list['institution'] = html1.xpath('//*[@id="basic"]/div[2]/p[4]/text()')[0]
            else:
                details_list['institution'] = '-'
        except:
            details_list['institution'] = '-'
        # 法人
        try:
            b = u'\u6cd5\u5b9a\u4ee3\u8868\u4eba\u2003'# 法定代表人
            leg1 = html1.xpath('//*[@id="basic"]/div[2]/p[3]/span/text()')[0]
            leg2 = html1.xpath('//*[@id="basic"]/div[2]/p[4]/span/text()')[0]
            leg3 = html1.xpath('//*[@id="basic"]/div[2]/p[5]/span/text()')[0]
            if leg1 == b:
                details_list['legalname'] = html1.xpath('//*[@id="basic"]/div[2]/p[3]/text()')[0]
            elif leg2 == b:
                details_list['legalname'] = html1.xpath('//*[@id="basic"]/div[2]/p[4]/text()')[0]
            elif leg3 == b:
                details_list['legalname'] = html1.xpath('//*[@id="basic"]/div[2]/p[5]/text()')[0]
        except:
            details_list['legalname'] = '-'
        # 经营状态
        try:
            c = u'\u7ecf\u8425\u72b6\u6001\u2003' # 经营状态
            bus1 = html1.xpath('//*[@id="basic"]/div[2]/p[4]/span/text()')[0]
            bus2 = html1.xpath('//*[@id="basic"]/div[2]/p[5]/span/text()')[0]
            bus3 = html1.xpath('//*[@id="basic"]/div[2]/p[6]/span/text()')[0]
            if bus1 ==c:
                details_list['business'] = html1.xpath('//*[@id="basic"]/div[2]/p[4]/text()')[0]
            elif bus2 == c :
                details_list['business'] = html1.xpath('//*[@id="basic"]/div[2]/p[5]/text()')[0]
            elif bus3 == c:
                details_list['business'] = html1.xpath('//*[@id="basic"]/div[2]/p[6]/text()')[0]
            else:
                details_list['business'] = '-'
        except:
            details_list['business'] = '-'
        # 成立时间
        try:
            d = u'\u6210\u7acb\u65f6\u95f4\u2003'# 成立时间
            open1 = html1.xpath('//*[@id="basic"]/div[2]/p[5]/span/text()')[0]
            open2 = html1.xpath('//*[@id="basic"]/div[2]/p[6]/span/text()')[0]
            open3 = html1.xpath('//*[@id="basic"]/div[2]/p[7]/span/text()')[0]
            if open1 == d:
                details_list['opentime'] = html1.xpath('//*[@id="basic"]/div[2]/p[5]/text()')[0]
            elif open2 ==d:
                details_list['opentime'] = html1.xpath('//*[@id="basic"]/div[2]/p[6]/text()')[0]
            elif open3 == d:
                details_list['opentime'] = html1.xpath('//*[@id="basic"]/div[2]/p[7]/text()')[0]
            else:
                details_list['opentime'] = '-'
        except:
            details_list['opentime'] = '-'
        # 经营期限
        try:
            e = u'\u8425\u4e1a\u671f\u9650\u2003'# 经营日期
            term1 = html1.xpath('//*[@id="basic"]/div[2]/p[6]/span/text()')[0]
            term2 = html1.xpath('//*[@id="basic"]/div[2]/p[7]/span/text()')[0]
            term3 = html1.xpath('//*[@id="basic"]/div[2]/p[8]/span/text()')[0]
            if term1 == e:
                details_list['term'] = html1.xpath('//*[@id="basic"]/div[2]/p[6]/text()')[0]
            elif term2 == e:
                details_list['term'] = html1.xpath('//*[@id="basic"]/div[2]/p[7]/text()')[0]
            elif term3 == e:
                details_list['term'] = html1.xpath('//*[@id="basic"]/div[2]/p[8]/text()')
            else:
                details_list['term'] = ''
        except:
            details_list['term'] = ''
        # 审核时间
        try:
            f = u'\u5ba1\u6838/\u5e74\u68c0\u65f6\u95f4\u2003'# 审核/年检时间

            rev1 = html1.xpath('//*[@id="basic"]/div[2]/p[7]/span/text()')[0]
            rev2 = html1.xpath('//*[@id="basic"]/div[2]/p[8]/span/text()')[0]
            rev3 = html1.xpath('//*[@id="basic"]/div[2]/p[9]/span/text()')[0]
            if rev1 == f:
                details_list['reviewtime'] = html1.xpath('//*[@id="basic"]/div[2]/p[7]/text()')[0]
            elif rev2 == f:
                details_list['reviewtime'] = html1.xpath('//*[@id="basic"]/div[2]/p[8]/text()')[0]
            elif rev3 == f:
                details_list['reviewtime'] = html1.xpath('//*[@id="basic"]/div[2]/p[9]/text()')[0]
            else:
                details_list['reviewtime'] = '-'
        except:
            details_list['reviewtime'] = '-'
        # 注册资本
        try:
            g = u'\u6ce8\u518c\u8d44\u672c\u2003' # 注册资本
            reg1 = html1.xpath('//*[@id="basic"]/div[2]/p[8]/span/text()')[0]
            reg2 = html1.xpath('//*[@id="basic"]/div[2]/p[9]/span/text()')[0]
            reg3 = html1.xpath('//*[@id="basic"]/div[2]/p[10]/span/text()')[0]
            if reg1 == g:
                details_list['registered'] = html1.xpath('//*[@id="basic"]/div[2]/p[8]/text()')[0]
            elif reg2 == g:
                details_list['registered'] = html1.xpath('//*[@id="basic"]/div[2]/p[9]/text()')[0]
            elif reg3 == g:
                details_list['registered'] = html1.xpath('//*[@id="basic"]/div[2]/p[10]/text()')[0]
            else:
                details_list['registered'] = '-'
        except:
            details_list['registered'] = '-'
        # 企业类型
        try:
            h = u'\u4f01\u4e1a\u7c7b\u578b\u2003' # 企业类型
            ent1 = html1.xpath('//*[@id="basic"]/div[2]/p[9]/span/text()')[0]
            ent2 = html1.xpath('//*[@id="basic"]/div[2]/p[10]/span/text()')[0]
            ent3 = html1.xpath('//*[@id="basic"]/div[2]/p[11]/span/text()')[0]
            if ent1 == h: # 企业类型
                details_list['enterprise'] = html1.xpath('//*[@id="basic"]/div[2]/p[9]/text()')[0]
            elif ent2 == h:
                details_list['enterprise'] = html1.xpath('//*[@id="basic"]/div[2]/p[10]/text()')[0]
            elif ent3 == h:
                details_list['enterprise'] = html1.xpath('//*[@id="basic"]/div[2]/p[11]/text()')[0]
            else:
                details_list['enterprise'] = '-'
        except:
            details_list['enterprise'] = '-'
        # 机构类型
        try:
            i = u'\u673a\u6784\u7c7b\u578b\u2003' # 机构类型
            org1 = html1.xpath('//*[@id="basic"]/div[2]/p[9]/span/text()')[0]
            org2 = html1.xpath('//*[@id="basic"]/div[2]/p[10]/span/text()')[0]
            org3 = html1.xpath('//*[@id="basic"]/div[2]/p[11]/span/text()')[0]
            if org1 == i:
                details_list['organization'] = html1.xpath('//*[@id="basic"]/div[2]/p[9]/text()')[0]
            elif org2 == i: # 所属行业
                details_list['organization'] = html1.xpath('//*[@id="basic"]/div[2]/p[10]/text()')[0]
            elif org3 == i:
                details_list['organization'] = html1.xpath('//*[@id="basic"]/div[2]/p[11]/text()')[0]
            else:
                details_list['organization'] = '-'
        except:
            details_list['organization'] = '-'
        # 所属行业
        try:
            g = u'\u6240\u5c5e\u884c\u4e1a\u2003' # 所属行业
            ind1 = html1.xpath('//*[@id="basic"]/div[2]/p[9]/span/text()')[0]
            ind2 = html1.xpath('//*[@id="basic"]/div[2]/p[10]/span/text()')[0]
            ind3 = html1.xpath('//*[@id="basic"]/div[2]/p[11]/span/text()')[0]
            ind4 = html1.xpath('//*[@id="basic"]/div[2]/p[12]/span/text()')[0]
            if ind1 == g:
                details_list['industry'] = html1.xpath('//*[@id="basic"]/div[2]/p[9]/text()')[0]
            elif ind2 == g:
                details_list['industry'] = html1.xpath('//*[@id="basic"]/div[2]/p[10]/text()')[0]
            elif ind3 == g:
                details_list['industry'] = html1.xpath('//*[@id="basic"]/div[2]/p[11]/text()')[0]
            elif ind4 == g:
                details_list['industry'] = html1.xpath('//*[@id="basic"]/div[2]/p[12]/text()')[0]
            else:
                details_list['industry'] = '-'
        except:
            details_list['industry'] = '-'
        # 联系电话
        details_list['tel'] = html1.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[3]/div[3]/text()')[0]
        # 地址
        details_list['address'] = html1.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[4]/div[3]/text()')[0]
        # print(details_list)
        return details_list

    def save_sql(self,details_list):

        sql = """INSERT INTO company (name,legalname,cieat,tel,institution,business,opentime,term,reviewtime,registered,enterprise,organization,industry,address)
        VALUES('{name}','{legalname}','{cieat}','{tel}','{institution}','{business}','{opentime}','{term}','{reviewtime}','{registered}','{enterprise}','{organization}','{industry}','{address}')
                """.format(name=details_list['name'], legalname=details_list['legalname'], cieat=details_list['cieat'], tel=details_list['tel'],institution=details_list['institution'],business=details_list['business'],
                           opentime=details_list['opentime'], term=details_list['term'], reviewtime=details_list['reviewtime'], registered=details_list['registered'],
                           enterprise=details_list['enterprise'],organization=details_list['organization'], industry=details_list['industry'], address=details_list['address'])

        print(sql)
        try:
            db.execute(sql)
            conn.commit()
        except:
            print("数据存入失败")

    def run(self,key):
        url = "https://xin.baidu.com/s?q={}&t=0".format(key)
        try:
            home_html = self.get_html(url)
            url_list = self.get_home_html(home_html)
            detail_list = list()
            urls = 'https://xin.baidu.com/m' + url_list
            detail_html = self.get_html(urls)
            data_info = self.get_details_html(detail_html)
            detail_list.append(data_info)
            print(detail_list)
                        # with open('./jieguo_baidu.txt', 'a+') as f:
                        #     f.write(str(detail_list).encode('utf-8').decode('utf-8') + "\r\n")
            self.save_sql(data_info)
            return detail_list
        except:
            pass


    def get_ip(self):
        cmd_str = "d:\IP.vbs"
        os.system(cmd_str)
        time.sleep(5)
        print("ip已更换！")

if __name__ == "__main__":
    f = open("./company.txt", "rb")
    while True:
        key = f.readline().replace('\r\n','')
        if not key:
            break
        print(key)
        Baidu().run(key)
        time.sleep(2)

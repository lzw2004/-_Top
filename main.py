"""
爬取豆瓣电影top榜
    * 名字 √
    * 评分 √
    * 链接 √ 
    * 图片 √ 
    * 导演 √
    * 编剧 √ 
    * 简介 √
"""

import requests
from lxml import etree
# import time
# import os



url = 'https://movie.douban.com/top250?start=0&filter='

# 爬取网页源码
def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
    }
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'
    html = r.text
    # print(html)
    return html
# get_html(url)

# 爬取电影名称
def get_name(html):
    """
    返回电影名 
    return : titles
    """
    html = etree.HTML(html)
    titles = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div/div/a/span[1]/text()')
    # print(titles)
    return titles

# 爬取电影评分
def get_score(html):
    """
    返回电影评分
    return : scores
    """
    html = etree.HTML(html)
    scores = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div/div[2]/div/span[2]/text()')
    # print(scores)
    return scores

# 爬取电影主图
def get_image(html):
    """
    返回电影主图
    return : image
    """
    html = etree.HTML(html)
    image = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src')
    # print(image)
    return image

# 爬取电影链接
def get_link(html):
    """
    返回电影链接
    return : links
    """
    html = etree.HTML(html)
    links = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href')
    # print(links)
    return links

# 爬取电影导演
def get_director(html):
    """
    返回电影导演
    return : director
    """
    html = etree.HTML(html)
    director = html.xpath('//*[@id="info"]/span[1]/span/a/text()')
    # print(director)
    return director

# 爬取电影编剧
def get_writer(html):
    """
    返回电影编剧
    return : writer
    """
    html = etree.HTML(html)
    writer = html.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')
    # print(writer)
    return writer

# 爬取电影简介
def get_introduction(html):
    """
      返回电影简介
      return : introduction
      """
    html = etree.HTML(html)
    introduction = html.xpath('//*[@id="link-report-intra"]/span[1]/span/text()')
    if introduction == []:
        introduction = html.xpath('//*[@id="link-report-intra"]/span[1]/text()')
        text = [data.strip() for data in introduction if data.strip()]
        # print(text)
        return text
    else:
        introduction = html.xpath('//*[@id="link-report-intra"]/span[1]/span/text()')
        text = [data.strip() for data in introduction if data.strip()]
        # print(text)
        return text








# if __name__ == '__main__':
#     html = get_html(url=url)
#     for i, m, z, j in zip(get_name(html), get_link(html), get_score(html), get_image(html)):
#         html_1 = get_html(m)
#         print(f"{i}")
#         print(f"评分 ：{z}")
#         print(f"链接 ：{m}")
#         print(f"主图 ：{j}")
#         print(f"{i}链接：{m}")
#         print(f"导演：{get_director(html_1)}")     # 导演
#         print(f"编剧：{get_writer(html_1)}")      # 编剧
#         print(f"简介：{get_introduction(html_1)}")     # 简介
#         # print(f"简介：{get_introduction(html_1).str.replace()}")
#         print("--------------------------------------------------------","\n")

if __name__ == '__main__':
    html = get_html(url=url)
    # 打开文件，模式为 "w" 表示写入模式，如果文件不存在则创建
    with open(".\movie_info.txt", "w+", encoding="utf-8") as f:
        for i, m, z, j in zip(get_name(html), get_link(html), get_score(html), get_image(html)):
            html_1 = get_html(m)
            f.write(f"{i}\n")
            print(f"{i}")

            f.write(f"评分：{z}\n")
            print(f"评分 ：{z}")

            f.write(f"链接：{m}\n")
            print(f"链接 ：{m}")

            f.write(f"主图：{j}\n")
            print(f"主图 ：{j}")

            f.write(f"{i}链接：{m}\n")
            print(f"{i}链接：{m}")

            f.write(f"导演：{get_director(html_1)}\n")
            print(f"导演：{get_director(html_1)}")

            f.write(f"编剧：{get_writer(html_1)}\n")
            print(f"编剧：{get_writer(html_1)}")

            f.write(f"简介：{get_introduction(html_1)}\n")
            print(f"简介：{get_introduction(html_1)}")

            f.write("====================================================================================="+"\n\n")


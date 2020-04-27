import requests
import json
from terminaltables import AsciiTable




def getRank(area, id, stageId, nums):
    url = "https://competition.huaweicloud.com/competition/v1/competitions/ranking/{0}?stage_id={1}&page_no=1&page_size={2}".format(id,stageId,nums)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    r = requests.get(url)
    rj = json.loads(r.text)
    results= rj['result']['teamRankingList']['results']
    return [[area, r['teamName'],r['score']] for r in results]

if __name__ == '__main__':
    info = {
            # '京津东北赛区':['1000036574', '136710'],
            # '上合赛区':['1000036576', '136712'],
            # '杭厦赛区':['1000036577', '136713'],
            # '江山赛区':['1000036578', '136714'],
            # '成渝赛区':['1000036579', '136715'],
            '西北赛区':['1000036580', '136716'],
            # '武长赛区':['1000036581', '136717'],
            # '粤港澳赛区':['1000036582', '136718'],
            # '海外赛区':['1000036583', '136719']
            }
    # 
    res = []
    for (key, value) in info.items():
        res += getRank(key, *value, 32)

    res.sort(key=lambda x: x[2])
    res = [[index+1]+r for index,r in enumerate(res) ]
    res = [['排名','赛区', '团队名', '分数']] + res
    table = AsciiTable(res)
    print(table.table)
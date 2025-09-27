print("20224016-박소호")

import urllib.request

page = urllib.request.urlopen("https://sports.news.naver.com/wfootball/record/index?tab=player&category=epl#playerRanking")
text = page.read().decode("utf8")
target  = 'onerror="imageOnError(this);"></div>'
gate = 0
rate = []
while gate > -1:
    gate = text.find(target,gate)
    rate.append(gate)
    if gate > -1:
        gate +=len(target)
where_start_goal = text.find(">최다 득점</strong>")
where_end_goal = rate[0]
start_goal =  where_start_goal + 188
end_goal = where_end_goal - 2
rank_goal = text[start_goal:end_goal]
where_start_assist = text.find("최다 도움</strong>")
where_end_assist = rate[1]
start_assist = where_start_assist +187
end_assist = where_end_assist -2
rank_assist = text[start_assist:end_assist]
print("EPL 최다 득점자:%s" %rank_goal)
print("EPL 최다 도움:%s" %rank_assist)

"""
有一個老師想要幫學生的期末分數加分，加分規則如下:
如果新分數小於40分，不予加分(保持原分數)。
如果原分數的下一個最接近的5的倍數跟原分數的差在3以下，新分數則為下一個最接近的5的倍數
請利用程式來計算下列4位學生換算後的總成績為何?

德瑞克 33
尚恩 73
傑夫 63
馬基 39
"""

score_dict = {"德瑞克": 33, "尚恩": 73, "傑夫": 63, "馬基": 39}

for name in score_dict.keys():
    mod = score_dict[name] // 5
    new_score = 5 * (mod + 1)

    if new_score < 40:
        pass
        print(f"{name}: {score_dict[name]}")
    elif new_score - score_dict[name] < 3:
        score_dict[name] = new_score
        print(f"{name}: {score_dict[name]}")
        
        
"""
德瑞克小朋友在公園溜滑梯的高處將一顆球從100公分的高度自由落下，每次落地後反跳回原高度的一半；然後再落下。
請使用一段程式實做，並算出它在第10次落地時，總共經歷過了多少公分？和第10次的反彈有多高？
"""
def calculate_height(Height, rebound_count):
    total_height = 0
    before_rebound = 0

    for i in range(1, rebound_count + 1):
        Height = Height / 2
        total_height += Height * 2
        before_rebound = total_height - Height * 2
    before_rebound += 100

    print(f"第{rebound_count}次落地時，總共經歷 {before_rebound} 公分")
    print(f"第{rebound_count}次反彈 {Height} 公分")

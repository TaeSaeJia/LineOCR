def extrac_total_prize(texts) :
    check_list = ["合計","合言十","言十","合计"]
    for i in texts :
        if i in check_list :
            return texts[texts.index(i)+1]
    return ""
        
def extrac_date_branch(texts) :
    ans = {'date' : "", "branch" : ""}
    for i in texts :
        if "年" in i and "月" in i and "日" in i :
            ans['date'] = i
        if "店" in i :
            ans['branch'] = i
    return ans

def extrac_good_name(texts) :
    return ""
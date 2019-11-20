#是否为变位词字典解法

def is_Change_word(s1,s2):
    s1_dict=dict()
    s2_dict=dict()
    for s1 in s1:
        s1_dict[s1]=s1_dict.get(s1,0)+1
    for s2 in s2:
        s2_dict[s2]=s2_dict.get(s2,0)+1
    if len(s1_dict)==len(s2_dict):
        for key in s1_dict:
            if s1_dict[key]!=s2_dict.get(key,0):
                return False
    else:
        return False
    return True


s1='python'
s2='typhon'
if is_Change_word(s1,s2):
    print ('True')
else:
    print ('False')

# Write your code here
def format_time(h,m,s):
    sh=str(h)
    sm=str(m)
    ss=str(s)
    if(len(sh)<2):
        sh="0"+sh
    if(len(sm)<2):
        sm="0"+sm
    if(len(ss)<2):
        ss="0"+ss
    return f'{sh}:{sm}:{ss}'
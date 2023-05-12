our_res = \
{4: 0.0,
 5: 0.0014705882352941124,
 6: 0.0018382352941176405,
 7: 0.006740196078431349,
 8: 0.011386846405228732}
sba_res = \
{4: 0.0009191176470588203,
 5: 0.004411764705882337,
 6: 0.006740196078431349,
 7: 0.012021475256769363,
 8: 0.02226307189542484}
sba_our_search = \
{4: 0.0009191176470588203,
 5: 0.00588235294117645,
 6: 0.030024509803921556,
 7: 0.08771008403361343,
 8: 0.0785845588235294}
sba_our_search_mean = \
{4: 0.0009191176470588203,
 5: 0.003676470588235281,
 6: 0.007965686274509776,
 7: 0.008403361344537816,
 8: 0.022058823529411742}

def to_percent(x):
    if x == 1:
        return "100\%"
    return ("%.2g" % (x * 100)) + "\%"

def table1():
    for i in range(4, 9):
        print(f"\sba,\emberchip,{i},{to_percent(sba_res[i])},--")
        print(f"\\tool,\emberchip,{i},{to_percent(our_res[i])},{to_percent((sba_res[i] - our_res[i]) / sba_res[i])}")

if __name__ == "__main__":
    table1()


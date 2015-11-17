from snsurvey import total_ctime

def test_total_ctime():
    ct =  total_ctime(0.05, [1000], [20], ['bessellb'])
    assert ct[0] == 48.125205025375969

def test_total_ctime2():
    ct = total_ctime(0.05, [1000,1020], [20,20], ['bessellb','bessellb'])
    assert ct[1] == 20

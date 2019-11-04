import sys


def func(a, b, c):
    # a = sys.argv[1]
    # b = sys.argv[2]
    # c = sys.argv[3]
    a = a
    b = b
    c = c
    res = {
        "sum": 2,
        "pass": 2,
        "fail": 0,
        "error": 0,
        "detail": [
            {
                "scr_casename": "页面字典值获取成功",
                "scr_result": "pass",
                "scr_log": "lsakfjsald发的发飞洒发沙发沙发法规jfsalkfsafsakfjsalfj"
                           "salkfasfsajflsajfsajfslfhaslf发顺丰拉风龙卡及法律上开发"
            },
            {
                "scr_casename": "页面字典值获取失败",
                "scr_result": "pass",
                "scr_log": "fasdfasfsa退群天气网约约约法司法的沙发沙发是范德萨发公司法fs"
                           "afsafsafasfsafwtwqrqwerwqrwqrqw法法师法"
            }
        ]
    }

    d = a + " " + b + " " + c
    print(d)
    return res



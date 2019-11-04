import logging

from api_test.models import ScriptCase
from celery_tasks.main import app


@app.task(bind=True, name='send_start_script', retry_backoff=3)
def send_start_script(self, path, enter_file, exit_file, res_data):

    try:
        # res = start_script(path, enter_file, exit_file)
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
        for case in res["detail"]:
            scr_case = ScriptCase.objects.create(case_name=case["scr_casename"], test_result=case["scr_result"],
                                                 case_test_log=case["scr_log"],
                                                 applicationScript_id=res_data.data["id"])
            case_count = ScriptCase.objects.filter(case_name=case["scr_casename"],
                                                   applicationScript_id=res_data.data["id"]).count()
            if case_count > 10:
                case_amount = ScriptCase.objects.filter(case_name=case["scr_casename"],
                                                        applicationScript_id=res_data.data["id"]).order_by(
                    "-updateTime")
                case_amount[10].delete()
        return res

    except Exception as e:
        logging.exception(e)
        self.retry(exc=e, max_retries=3)




# -*- coding: utf-8 -*-
import os
try:
    import imp
except ImportError:  # py12
    imp = None
    import importlib
    import importlib.machinery


def action_caller(service):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    if imp:
        fp, pathname, desc = imp.find_module(service, [cur_path])
        mod = imp.load_module("tccli.services." + service, fp, pathname, desc)
    else:
        spec = importlib.machinery.PathFinder().find_spec(service, [cur_path])
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    return mod.action_caller


SERVICE_VERSIONS = {
    "advisor": [
        "2020-07-21"
    ],
    "aiart": [
        "2022-12-29"
    ],
    "ams": [
        "2020-12-29"
    ],
    "antiddos": [
        "2020-03-09"
    ],
    "apigateway": [
        "2018-08-08"
    ],
    "autoscaling": [
        "2018-04-19"
    ],
    "batch": [
        "2017-03-12"
    ],
    "billing": [
        "2018-07-09"
    ],
    "cam": [
        "2019-01-16"
    ],
    "captcha": [
        "2019-07-22"
    ],
    "car": [
        "2022-01-10"
    ],
    "cbs": [
        "2017-03-12"
    ],
    "ccc": [
        "2020-02-10"
    ],
    "cdb": [
        "2017-03-20"
    ],
    "cdn": [
        "2018-06-06"
    ],
    "cdwdoris": [
        "2021-12-28"
    ],
    "cfg": [
        "2021-08-20"
    ],
    "cfs": [
        "2019-07-19"
    ],
    "cfw": [
        "2019-09-04"
    ],
    "chdfs": [
        "2020-11-12"
    ],
    "ciam": [
        "2022-03-31",
        "2021-04-20"
    ],
    "ckafka": [
        "2019-08-19"
    ],
    "clb": [
        "2018-03-17"
    ],
    "cloudaudit": [
        "2019-03-19"
    ],
    "cls": [
        "2020-10-16"
    ],
    "cmq": [
        "2019-03-04"
    ],
    "controlcenter": [
        "2023-01-10"
    ],
    "csip": [
        "2022-11-21"
    ],
    "cvm": [
        "2017-03-12"
    ],
    "cwp": [
        "2018-02-28"
    ],
    "cynosdb": [
        "2019-01-07"
    ],
    "dataintegration": [
        "2022-06-13"
    ],
    "dayu": [
        "2018-07-09"
    ],
    "dbbrain": [
        "2021-05-27",
        "2019-10-16"
    ],
    "dc": [
        "2018-04-10"
    ],
    "dcdb": [
        "2018-04-11"
    ],
    "dlc": [
        "2021-01-25"
    ],
    "dms": [
        "2020-08-19"
    ],
    "dnspod": [
        "2021-03-23"
    ],
    "domain": [
        "2018-08-08"
    ],
    "dts": [
        "2021-12-06",
        "2018-03-30"
    ],
    "eb": [
        "2021-04-16"
    ],
    "ecdn": [
        "2019-10-12"
    ],
    "ecm": [
        "2019-07-19"
    ],
    "eiam": [
        "2021-04-20"
    ],
    "emr": [
        "2019-01-03"
    ],
    "es": [
        "2018-04-16"
    ],
    "facefusion": [
        "2022-09-27"
    ],
    "faceid": [
        "2018-03-01"
    ],
    "gaap": [
        "2018-05-29"
    ],
    "gme": [
        "2018-07-11"
    ],
    "gpm": [
        "2020-08-20"
    ],
    "gse": [
        "2019-11-12"
    ],
    "iai": [
        "2020-03-03"
    ],
    "ims": [
        "2020-12-29"
    ],
    "intlpartnersmgt": [
        "2022-09-28"
    ],
    "iotcloud": [
        "2021-04-08"
    ],
    "ip": [
        "2021-04-09"
    ],
    "kms": [
        "2019-01-18"
    ],
    "lcic": [
        "2022-08-17"
    ],
    "lighthouse": [
        "2020-03-24"
    ],
    "live": [
        "2018-08-01"
    ],
    "mariadb": [
        "2017-03-12"
    ],
    "mdc": [
        "2020-08-28"
    ],
    "mdl": [
        "2020-03-26"
    ],
    "mdp": [
        "2020-05-27"
    ],
    "mongodb": [
        "2019-07-25"
    ],
    "monitor": [
        "2018-07-24"
    ],
    "mps": [
        "2019-06-12"
    ],
    "msp": [
        "2018-03-19"
    ],
    "ocr": [
        "2018-11-19"
    ],
    "omics": [
        "2022-11-28"
    ],
    "organization": [
        "2021-03-31",
        "2018-12-25"
    ],
    "postgres": [
        "2017-03-12"
    ],
    "privatedns": [
        "2020-10-28"
    ],
    "redis": [
        "2018-04-12"
    ],
    "rum": [
        "2021-06-22"
    ],
    "scf": [
        "2018-04-16"
    ],
    "ses": [
        "2020-10-02"
    ],
    "sms": [
        "2021-01-11",
        "2019-07-11"
    ],
    "sqlserver": [
        "2018-03-28"
    ],
    "ssl": [
        "2019-12-05"
    ],
    "ssm": [
        "2019-09-23"
    ],
    "sts": [
        "2018-08-13"
    ],
    "tag": [
        "2018-08-13"
    ],
    "tat": [
        "2020-10-28"
    ],
    "tcaplusdb": [
        "2019-08-23"
    ],
    "tchd": [
        "2023-03-06"
    ],
    "tcmpp": [
        "2024-08-01"
    ],
    "tcr": [
        "2019-09-24"
    ],
    "tcss": [
        "2020-11-01"
    ],
    "tdid": [
        "2021-05-19"
    ],
    "tdmq": [
        "2020-02-17"
    ],
    "tem": [
        "2021-07-01",
        "2020-12-21"
    ],
    "teo": [
        "2022-09-01",
        "2022-01-06"
    ],
    "tiw": [
        "2019-09-19"
    ],
    "tke": [
        "2018-05-25"
    ],
    "tms": [
        "2020-12-29"
    ],
    "tmt": [
        "2018-03-21"
    ],
    "trtc": [
        "2019-07-22"
    ],
    "tts": [
        "2019-08-23"
    ],
    "vm": [
        "2021-09-22",
        "2020-12-29"
    ],
    "vod": [
        "2018-07-17"
    ],
    "vpc": [
        "2017-03-12"
    ],
    "waf": [
        "2018-01-25"
    ],
    "wedata": [
        "2021-08-20"
    ],
    "yunjing": [
        "2018-02-28"
    ]
}
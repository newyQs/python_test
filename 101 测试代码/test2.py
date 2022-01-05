"""

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-23 13:40:11
# @Author  : yizhilaolihua

import requests
import json
from requests.exceptions import ConnectTimeout, ConnectionError
from json.decoder import JSONDecodeError
from flask import current_app
from traceback import format_exc
from app import db
from app.models import ThirdPartRecord, ReleaseConfig


def get_nexus_cfg():
    r = ReleaseConfig.query.filter_by(name="nexus_upload_cfg").first()
    sql_cfgs = json.loads(r.value)
    all_cfgs = dict(
        repo="releases",
        timeout=60 * 10,
        url="http://nexus.****.cn/service/local/artifact/maven/content"
    )
    all_cfgs.update(sql_cfgs)
    return all_cfgs


def nexus_upload_file(**kwargs):
    """
        curl -v -F hasPom=false
                -F r=releases
                -F e=jar
                -F g=com.***.devops
                -F a=helloworld3
                -F v=0.0.5
                -F p=jar
                -F file=@/someworkspace/nexus-devops-testhelloworld/helloworld-core/target/helloworld-10.7.2.1.jar
                -u user:password
        http://nexus.****.cn/service/local/artifact/maven/content

        refer to https://support.sonatype.com/hc/en-us/articles/213465818-How-can-I-programmatically-upload-an-artifact-into-Nexus-2-
    """
    para2check = ("group_id", "artifact_id", "version", "file_path")
    assert all(map(lambda x: x in kwargs, para2check)), "缺少以下参数:{}".format(
        [each for each in para2check if each not in kwargs]
    )

    current_app.logger.info("调用上传nexus:{0}".format(kwargs))
    nexus_cfg = get_nexus_cfg()

    data = dict(
        hasPom="false",
        r=nexus_cfg.get("repo"),
        e="jar",
        p="jar",
        g=kwargs["group_id"],
        a=kwargs["artifact_id"],
        v=kwargs["version"],
    )
    try:
        success = False
        with open(kwargs["file_path"], 'rb') as f:
            res = requests.post(
                nexus_cfg.get("url"),
                files={'file': f},
                data=data,
                auth=(nexus_cfg.get("user"), nexus_cfg.get("passwd")),
                timeout=nexus_cfg.get("timeout")
            )
            # 大文件需要设置超长的超时时间，180M文件上传需要3分25秒。
            current_app.logger.info("调用上传nexus接口返回,code:{0},res:{1}".format(res.status_code, res.text))
        success = True if res.status_code in (201,) else False
        result = res.json()
    except (ConnectionError, ConnectTimeout):
        result = {"request_failed": "上传nexus接口调用超时/断开，请联系运维处理"}
        current_app.logger.error("上传nexus接口调用超时/断开：{}".format(format_exc()))
    except FileNotFoundError:
        result = {"request_failed": "未找到上传文件{}".format(kwargs["file_path"])}
        current_app.logger.error("未找到上传文件：{}".format(format_exc()))
    except JSONDecodeError:
        result = {"request_failed": "请求失败，code:{0},返回:{1}".format(res.status_code, res.text)}
        # nexus原生提示信息优化
        if res.status_code == 400 and "not allow updating artifacts" in res.text:
            result = {"request_failed": "请求失败，返回code:{0}，不允许重复上传！".format(res.status_code)}
    except Exception as e:
        result = {"request_failed": '未知失败类型：{}'.format(e)}
        current_app.logger.error("上传nexus失败：{}".format(format_exc()))

    return success, result

# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli.nice_command import NiceCommand
import tccli.error_msg as ErrorMsg
import tccli.help_template as HelpTemplate
from tccli import __version__
from tccli.utils import Utils
from tccli.configure import Configure
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.vod.v20180717 import vod_client as vod_client_v20180717
from tencentcloud.vod.v20180717 import models as models_v20180717
from tccli.services.vod import v20180717
from tccli.services.vod.v20180717 import help as v20180717_help


def doDeleteAnimatedGraphicsTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAnimatedGraphicsTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAnimatedGraphicsTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAnimatedGraphicsTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAdaptiveDynamicStreamingTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAdaptiveDynamicStreamingTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Type": argv.get("--Type"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAdaptiveDynamicStreamingTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAdaptiveDynamicStreamingTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSubAppIds(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSubAppIds", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSubAppIdsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSubAppIds(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSampleSnapshotTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSampleSnapshotTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "SampleType": argv.get("--SampleType"),
        "SampleInterval": Utils.try_to_json(argv, "--SampleInterval"),
        "Name": argv.get("--Name"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "ResolutionAdaptive": argv.get("--ResolutionAdaptive"),
        "Format": argv.get("--Format"),
        "Comment": argv.get("--Comment"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "FillType": argv.get("--FillType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSampleSnapshotTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateSampleSnapshotTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEditMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EditMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "InputType": argv.get("--InputType"),
        "FileInfos": Utils.try_to_json(argv, "--FileInfos"),
        "StreamInfos": Utils.try_to_json(argv, "--StreamInfos"),
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "ProcedureName": argv.get("--ProcedureName"),
        "OutputConfig": Utils.try_to_json(argv, "--OutputConfig"),
        "SessionContext": argv.get("--SessionContext"),
        "TasksPriority": Utils.try_to_json(argv, "--TasksPriority"),
        "SessionId": argv.get("--SessionId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EditMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EditMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAIAnalysisTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAIAnalysisTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAIAnalysisTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAIAnalysisTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doConfirmEvents(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ConfirmEvents", g_param[OptionsDefine.Version])
        return

    param = {
        "EventHandles": Utils.try_to_json(argv, "--EventHandles"),
        "ExtInfo": argv.get("--ExtInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ConfirmEventsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ConfirmEvents(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSnapshotByTimeOffsetTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSnapshotByTimeOffsetTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Type": argv.get("--Type"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSnapshotByTimeOffsetTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSnapshotByTimeOffsetTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPullUpload(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PullUpload", g_param[OptionsDefine.Version])
        return

    param = {
        "MediaUrl": argv.get("--MediaUrl"),
        "MediaName": argv.get("--MediaName"),
        "CoverUrl": argv.get("--CoverUrl"),
        "Procedure": argv.get("--Procedure"),
        "ExpireTime": argv.get("--ExpireTime"),
        "StorageRegion": argv.get("--StorageRegion"),
        "ClassId": Utils.try_to_json(argv, "--ClassId"),
        "SessionContext": argv.get("--SessionContext"),
        "SessionId": argv.get("--SessionId"),
        "ExtInfo": argv.get("--ExtInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PullUploadRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PullUpload(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doApplyUpload(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ApplyUpload", g_param[OptionsDefine.Version])
        return

    param = {
        "MediaType": argv.get("--MediaType"),
        "MediaName": argv.get("--MediaName"),
        "CoverType": argv.get("--CoverType"),
        "Procedure": argv.get("--Procedure"),
        "ExpireTime": argv.get("--ExpireTime"),
        "StorageRegion": argv.get("--StorageRegion"),
        "ClassId": Utils.try_to_json(argv, "--ClassId"),
        "SourceContext": argv.get("--SourceContext"),
        "SessionContext": argv.get("--SessionContext"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ApplyUploadRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ApplyUpload(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Container": argv.get("--Container"),
        "Name": argv.get("--Name"),
        "Comment": argv.get("--Comment"),
        "RemoveVideo": Utils.try_to_json(argv, "--RemoveVideo"),
        "RemoveAudio": Utils.try_to_json(argv, "--RemoveAudio"),
        "VideoTemplate": Utils.try_to_json(argv, "--VideoTemplate"),
        "AudioTemplate": Utils.try_to_json(argv, "--AudioTemplate"),
        "TEHDConfig": Utils.try_to_json(argv, "--TEHDConfig"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSnapshotByTimeOffsetTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSnapshotByTimeOffsetTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": argv.get("--Name"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "ResolutionAdaptive": argv.get("--ResolutionAdaptive"),
        "Format": argv.get("--Format"),
        "Comment": argv.get("--Comment"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "FillType": argv.get("--FillType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSnapshotByTimeOffsetTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateSnapshotByTimeOffsetTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCommitUpload(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CommitUpload", g_param[OptionsDefine.Version])
        return

    param = {
        "VodSessionKey": argv.get("--VodSessionKey"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CommitUploadRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CommitUpload(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeMediaInfos(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeMediaInfos", g_param[OptionsDefine.Version])
        return

    param = {
        "FileIds": Utils.try_to_json(argv, "--FileIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeMediaInfosRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeMediaInfos(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAIAnalysisTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAIAnalysisTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAIAnalysisTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAIAnalysisTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPullEvents(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PullEvents", g_param[OptionsDefine.Version])
        return

    param = {
        "ExtInfo": argv.get("--ExtInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PullEventsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PullEvents(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSimpleHlsClip(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SimpleHlsClip", g_param[OptionsDefine.Version])
        return

    param = {
        "Url": argv.get("--Url"),
        "StartTimeOffset": Utils.try_to_json(argv, "--StartTimeOffset"),
        "EndTimeOffset": Utils.try_to_json(argv, "--EndTimeOffset"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SimpleHlsClipRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SimpleHlsClip(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTaskDetail(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTaskDetail", g_param[OptionsDefine.Version])
        return

    param = {
        "TaskId": argv.get("--TaskId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTaskDetailRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTaskDetail(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doProcessMediaByUrl(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ProcessMediaByUrl", g_param[OptionsDefine.Version])
        return

    param = {
        "InputInfo": Utils.try_to_json(argv, "--InputInfo"),
        "OutputInfo": Utils.try_to_json(argv, "--OutputInfo"),
        "AiContentReviewTask": Utils.try_to_json(argv, "--AiContentReviewTask"),
        "AiAnalysisTask": Utils.try_to_json(argv, "--AiAnalysisTask"),
        "AiRecognitionTask": Utils.try_to_json(argv, "--AiRecognitionTask"),
        "TasksPriority": Utils.try_to_json(argv, "--TasksPriority"),
        "TasksNotifyMode": argv.get("--TasksNotifyMode"),
        "SessionContext": argv.get("--SessionContext"),
        "SessionId": argv.get("--SessionId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ProcessMediaByUrlRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ProcessMediaByUrl(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySampleSnapshotTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySampleSnapshotTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": argv.get("--Name"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "ResolutionAdaptive": argv.get("--ResolutionAdaptive"),
        "SampleType": argv.get("--SampleType"),
        "SampleInterval": Utils.try_to_json(argv, "--SampleInterval"),
        "Format": argv.get("--Format"),
        "Comment": argv.get("--Comment"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "FillType": argv.get("--FillType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySampleSnapshotTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySampleSnapshotTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSearchMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SearchMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "Text": argv.get("--Text"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "ClassIds": Utils.try_to_json(argv, "--ClassIds"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "SourceType": argv.get("--SourceType"),
        "StreamId": argv.get("--StreamId"),
        "Vid": argv.get("--Vid"),
        "Sort": Utils.try_to_json(argv, "--Sort"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SearchMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteWatermarkTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteWatermarkTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteWatermarkTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteWatermarkTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSnapshotByTimeOffsetTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteSnapshotByTimeOffsetTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSnapshotByTimeOffsetTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteSnapshotByTimeOffsetTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeReviewDetails(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeReviewDetails", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeReviewDetailsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeReviewDetails(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeStorageData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeStorageData", g_param[OptionsDefine.Version])
        return

    param = {
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeStorageDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeStorageData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeStorageDetails(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeStorageDetails", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Interval": argv.get("--Interval"),
        "StorageType": argv.get("--StorageType"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeStorageDetailsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeStorageDetails(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doForbidMediaDistribution(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ForbidMediaDistribution", g_param[OptionsDefine.Version])
        return

    param = {
        "FileIds": Utils.try_to_json(argv, "--FileIds"),
        "Operation": argv.get("--Operation"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ForbidMediaDistributionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ForbidMediaDistribution(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAIAnalysisTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAIAnalysisTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": argv.get("--Name"),
        "Comment": argv.get("--Comment"),
        "ClassificationConfigure": Utils.try_to_json(argv, "--ClassificationConfigure"),
        "TagConfigure": Utils.try_to_json(argv, "--TagConfigure"),
        "CoverConfigure": Utils.try_to_json(argv, "--CoverConfigure"),
        "FrameTagConfigure": Utils.try_to_json(argv, "--FrameTagConfigure"),
        "HighlightConfigure": Utils.try_to_json(argv, "--HighlightConfigure"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAIAnalysisTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAIAnalysisTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteProcedureTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteProcedureTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": argv.get("--Name"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteProcedureTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteProcedureTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySubAppIdInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySubAppIdInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "Name": argv.get("--Name"),
        "Description": argv.get("--Description"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySubAppIdInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySubAppIdInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProcedureTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeProcedureTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Names": Utils.try_to_json(argv, "--Names"),
        "Type": argv.get("--Type"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProcedureTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeProcedureTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateWatermarkTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateWatermarkTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Type": argv.get("--Type"),
        "Name": argv.get("--Name"),
        "Comment": argv.get("--Comment"),
        "CoordinateOrigin": argv.get("--CoordinateOrigin"),
        "XPos": argv.get("--XPos"),
        "YPos": argv.get("--YPos"),
        "ImageTemplate": Utils.try_to_json(argv, "--ImageTemplate"),
        "TextTemplate": Utils.try_to_json(argv, "--TextTemplate"),
        "SvgTemplate": Utils.try_to_json(argv, "--SvgTemplate"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateWatermarkTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateWatermarkTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSampleSnapshotTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteSampleSnapshotTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSampleSnapshotTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteSampleSnapshotTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doWeChatMiniProgramPublish(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("WeChatMiniProgramPublish", g_param[OptionsDefine.Version])
        return

    param = {
        "FileId": argv.get("--FileId"),
        "SourceDefinition": Utils.try_to_json(argv, "--SourceDefinition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.WeChatMiniProgramPublishRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.WeChatMiniProgramPublish(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAnimatedGraphicsTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAnimatedGraphicsTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": argv.get("--Name"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "ResolutionAdaptive": argv.get("--ResolutionAdaptive"),
        "Format": argv.get("--Format"),
        "Fps": Utils.try_to_json(argv, "--Fps"),
        "Quality": Utils.try_to_json(argv, "--Quality"),
        "Comment": argv.get("--Comment"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAnimatedGraphicsTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAnimatedGraphicsTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAIRecognitionTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAIRecognitionTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAIRecognitionTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAIRecognitionTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAudioTrackTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAudioTrackTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Type": argv.get("--Type"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAudioTrackTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAudioTrackTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAnimatedGraphicsTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAnimatedGraphicsTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Fps": Utils.try_to_json(argv, "--Fps"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "ResolutionAdaptive": argv.get("--ResolutionAdaptive"),
        "Format": argv.get("--Format"),
        "Quality": Utils.try_to_json(argv, "--Quality"),
        "Name": argv.get("--Name"),
        "Comment": argv.get("--Comment"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAnimatedGraphicsTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAnimatedGraphicsTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAnimatedGraphicsTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAnimatedGraphicsTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Type": argv.get("--Type"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAnimatedGraphicsTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAnimatedGraphicsTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateProcedureTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateProcedureTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": argv.get("--Name"),
        "MediaProcessTask": Utils.try_to_json(argv, "--MediaProcessTask"),
        "AiContentReviewTask": Utils.try_to_json(argv, "--AiContentReviewTask"),
        "AiAnalysisTask": Utils.try_to_json(argv, "--AiAnalysisTask"),
        "AiRecognitionTask": Utils.try_to_json(argv, "--AiRecognitionTask"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateProcedureTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateProcedureTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPushUrlCache(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PushUrlCache", g_param[OptionsDefine.Version])
        return

    param = {
        "Urls": Utils.try_to_json(argv, "--Urls"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PushUrlCacheRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PushUrlCache(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVideoTrackTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVideoTrackTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Type": argv.get("--Type"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVideoTrackTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVideoTrackTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySnapshotByTimeOffsetTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySnapshotByTimeOffsetTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": argv.get("--Name"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "ResolutionAdaptive": argv.get("--ResolutionAdaptive"),
        "Format": argv.get("--Format"),
        "Comment": argv.get("--Comment"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "FillType": argv.get("--FillType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySnapshotByTimeOffsetTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySnapshotByTimeOffsetTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResetProcedureTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResetProcedureTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": argv.get("--Name"),
        "MediaProcessTask": Utils.try_to_json(argv, "--MediaProcessTask"),
        "AiContentReviewTask": Utils.try_to_json(argv, "--AiContentReviewTask"),
        "AiAnalysisTask": Utils.try_to_json(argv, "--AiAnalysisTask"),
        "AiRecognitionTask": Utils.try_to_json(argv, "--AiRecognitionTask"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResetProcedureTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResetProcedureTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doExecuteFunction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ExecuteFunction", g_param[OptionsDefine.Version])
        return

    param = {
        "FunctionName": argv.get("--FunctionName"),
        "FunctionArg": argv.get("--FunctionArg"),
        "SessionContext": argv.get("--SessionContext"),
        "SessionId": argv.get("--SessionId"),
        "ExtInfo": argv.get("--ExtInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ExecuteFunctionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ExecuteFunction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateClass", g_param[OptionsDefine.Version])
        return

    param = {
        "ParentId": Utils.try_to_json(argv, "--ParentId"),
        "ClassName": argv.get("--ClassName"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySubAppIdStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySubAppIdStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "Status": argv.get("--Status"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySubAppIdStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySubAppIdStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCDNUsageData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCDNUsageData", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "DataType": argv.get("--DataType"),
        "DataInterval": Utils.try_to_json(argv, "--DataInterval"),
        "DomainNames": Utils.try_to_json(argv, "--DomainNames"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCDNUsageDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCDNUsageData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Container": argv.get("--Container"),
        "Name": argv.get("--Name"),
        "Comment": argv.get("--Comment"),
        "RemoveVideo": Utils.try_to_json(argv, "--RemoveVideo"),
        "RemoveAudio": Utils.try_to_json(argv, "--RemoveAudio"),
        "VideoTemplate": Utils.try_to_json(argv, "--VideoTemplate"),
        "AudioTemplate": Utils.try_to_json(argv, "--AudioTemplate"),
        "TEHDConfig": Utils.try_to_json(argv, "--TEHDConfig"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyWatermarkTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyWatermarkTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": argv.get("--Name"),
        "Comment": argv.get("--Comment"),
        "CoordinateOrigin": argv.get("--CoordinateOrigin"),
        "XPos": argv.get("--XPos"),
        "YPos": argv.get("--YPos"),
        "ImageTemplate": Utils.try_to_json(argv, "--ImageTemplate"),
        "TextTemplate": Utils.try_to_json(argv, "--TextTemplate"),
        "SvgTemplate": Utils.try_to_json(argv, "--SvgTemplate"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyWatermarkTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyWatermarkTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeMediaProcessUsageData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeMediaProcessUsageData", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Type": argv.get("--Type"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeMediaProcessUsageDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeMediaProcessUsageData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyImageSpriteTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyImageSpriteTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": argv.get("--Name"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "ResolutionAdaptive": argv.get("--ResolutionAdaptive"),
        "SampleType": argv.get("--SampleType"),
        "SampleInterval": Utils.try_to_json(argv, "--SampleInterval"),
        "RowCount": Utils.try_to_json(argv, "--RowCount"),
        "ColumnCount": Utils.try_to_json(argv, "--ColumnCount"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "FillType": argv.get("--FillType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyImageSpriteTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyImageSpriteTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doLiveRealTimeClip(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("LiveRealTimeClip", g_param[OptionsDefine.Version])
        return

    param = {
        "StreamId": argv.get("--StreamId"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "IsPersistence": Utils.try_to_json(argv, "--IsPersistence"),
        "ExpireTime": argv.get("--ExpireTime"),
        "Procedure": argv.get("--Procedure"),
        "MetaDataRequired": Utils.try_to_json(argv, "--MetaDataRequired"),
        "Host": argv.get("--Host"),
        "ExtInfo": argv.get("--ExtInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.LiveRealTimeClipRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.LiveRealTimeClip(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doComposeMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ComposeMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "Tracks": Utils.try_to_json(argv, "--Tracks"),
        "Output": Utils.try_to_json(argv, "--Output"),
        "Canvas": Utils.try_to_json(argv, "--Canvas"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ComposeMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ComposeMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doProcessMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ProcessMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "FileId": argv.get("--FileId"),
        "MediaProcessTask": Utils.try_to_json(argv, "--MediaProcessTask"),
        "AiContentReviewTask": Utils.try_to_json(argv, "--AiContentReviewTask"),
        "AiAnalysisTask": Utils.try_to_json(argv, "--AiAnalysisTask"),
        "AiRecognitionTask": Utils.try_to_json(argv, "--AiRecognitionTask"),
        "TasksPriority": Utils.try_to_json(argv, "--TasksPriority"),
        "TasksNotifyMode": argv.get("--TasksNotifyMode"),
        "SessionContext": argv.get("--SessionContext"),
        "SessionId": argv.get("--SessionId"),
        "ExtInfo": argv.get("--ExtInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ProcessMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ProcessMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSampleSnapshotTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSampleSnapshotTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Type": argv.get("--Type"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSampleSnapshotTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSampleSnapshotTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeImageSpriteTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeImageSpriteTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Type": argv.get("--Type"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeImageSpriteTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeImageSpriteTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doProcessMediaByProcedure(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ProcessMediaByProcedure", g_param[OptionsDefine.Version])
        return

    param = {
        "FileId": argv.get("--FileId"),
        "ProcedureName": argv.get("--ProcedureName"),
        "TasksPriority": Utils.try_to_json(argv, "--TasksPriority"),
        "TasksNotifyMode": argv.get("--TasksNotifyMode"),
        "SessionContext": argv.get("--SessionContext"),
        "SessionId": argv.get("--SessionId"),
        "ExtInfo": argv.get("--ExtInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ProcessMediaByProcedureRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ProcessMediaByProcedure(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAIAnalysisTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAIAnalysisTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": argv.get("--Name"),
        "Comment": argv.get("--Comment"),
        "ClassificationConfigure": Utils.try_to_json(argv, "--ClassificationConfigure"),
        "TagConfigure": Utils.try_to_json(argv, "--TagConfigure"),
        "CoverConfigure": Utils.try_to_json(argv, "--CoverConfigure"),
        "FrameTagConfigure": Utils.try_to_json(argv, "--FrameTagConfigure"),
        "HighlightConfigure": Utils.try_to_json(argv, "--HighlightConfigure"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAIAnalysisTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAIAnalysisTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAIRecognitionTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAIRecognitionTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAIRecognitionTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAIRecognitionTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeWatermarkTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeWatermarkTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Type": argv.get("--Type"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeWatermarkTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeWatermarkTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateImageSpriteTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateImageSpriteTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "SampleType": argv.get("--SampleType"),
        "SampleInterval": Utils.try_to_json(argv, "--SampleInterval"),
        "RowCount": Utils.try_to_json(argv, "--RowCount"),
        "ColumnCount": Utils.try_to_json(argv, "--ColumnCount"),
        "Name": argv.get("--Name"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "ResolutionAdaptive": argv.get("--ResolutionAdaptive"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "FillType": argv.get("--FillType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateImageSpriteTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateImageSpriteTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteImageSpriteTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteImageSpriteTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteImageSpriteTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteImageSpriteTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTranscodeTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTranscodeTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Type": argv.get("--Type"),
        "ContainerType": argv.get("--ContainerType"),
        "TEHDType": argv.get("--TEHDType"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTranscodeTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTranscodeTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeContentReviewTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeContentReviewTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeContentReviewTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeContentReviewTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180717": vod_client_v20180717,

}

MODELS_MAP = {
    "v20180717": models_v20180717,

}

ACTION_MAP = {
    "DeleteAnimatedGraphicsTemplate": doDeleteAnimatedGraphicsTemplate,
    "DescribeAdaptiveDynamicStreamingTemplates": doDescribeAdaptiveDynamicStreamingTemplates,
    "DescribeSubAppIds": doDescribeSubAppIds,
    "CreateSampleSnapshotTemplate": doCreateSampleSnapshotTemplate,
    "EditMedia": doEditMedia,
    "DeleteAIAnalysisTemplate": doDeleteAIAnalysisTemplate,
    "ConfirmEvents": doConfirmEvents,
    "DescribeSnapshotByTimeOffsetTemplates": doDescribeSnapshotByTimeOffsetTemplates,
    "PullUpload": doPullUpload,
    "ApplyUpload": doApplyUpload,
    "ModifyTranscodeTemplate": doModifyTranscodeTemplate,
    "CreateSnapshotByTimeOffsetTemplate": doCreateSnapshotByTimeOffsetTemplate,
    "CommitUpload": doCommitUpload,
    "DescribeMediaInfos": doDescribeMediaInfos,
    "DescribeAIAnalysisTemplates": doDescribeAIAnalysisTemplates,
    "PullEvents": doPullEvents,
    "SimpleHlsClip": doSimpleHlsClip,
    "DescribeTaskDetail": doDescribeTaskDetail,
    "ProcessMediaByUrl": doProcessMediaByUrl,
    "ModifySampleSnapshotTemplate": doModifySampleSnapshotTemplate,
    "SearchMedia": doSearchMedia,
    "DeleteWatermarkTemplate": doDeleteWatermarkTemplate,
    "DeleteSnapshotByTimeOffsetTemplate": doDeleteSnapshotByTimeOffsetTemplate,
    "DescribeReviewDetails": doDescribeReviewDetails,
    "DescribeStorageData": doDescribeStorageData,
    "DescribeStorageDetails": doDescribeStorageDetails,
    "ForbidMediaDistribution": doForbidMediaDistribution,
    "ModifyAIAnalysisTemplate": doModifyAIAnalysisTemplate,
    "DeleteProcedureTemplate": doDeleteProcedureTemplate,
    "ModifySubAppIdInfo": doModifySubAppIdInfo,
    "DescribeProcedureTemplates": doDescribeProcedureTemplates,
    "CreateWatermarkTemplate": doCreateWatermarkTemplate,
    "DeleteSampleSnapshotTemplate": doDeleteSampleSnapshotTemplate,
    "WeChatMiniProgramPublish": doWeChatMiniProgramPublish,
    "ModifyAnimatedGraphicsTemplate": doModifyAnimatedGraphicsTemplate,
    "DeleteAIRecognitionTemplate": doDeleteAIRecognitionTemplate,
    "DescribeAudioTrackTemplates": doDescribeAudioTrackTemplates,
    "CreateAnimatedGraphicsTemplate": doCreateAnimatedGraphicsTemplate,
    "DescribeAnimatedGraphicsTemplates": doDescribeAnimatedGraphicsTemplates,
    "CreateProcedureTemplate": doCreateProcedureTemplate,
    "PushUrlCache": doPushUrlCache,
    "DescribeVideoTrackTemplates": doDescribeVideoTrackTemplates,
    "ModifySnapshotByTimeOffsetTemplate": doModifySnapshotByTimeOffsetTemplate,
    "ResetProcedureTemplate": doResetProcedureTemplate,
    "ExecuteFunction": doExecuteFunction,
    "CreateClass": doCreateClass,
    "ModifySubAppIdStatus": doModifySubAppIdStatus,
    "DescribeCDNUsageData": doDescribeCDNUsageData,
    "CreateTranscodeTemplate": doCreateTranscodeTemplate,
    "ModifyWatermarkTemplate": doModifyWatermarkTemplate,
    "DescribeMediaProcessUsageData": doDescribeMediaProcessUsageData,
    "ModifyImageSpriteTemplate": doModifyImageSpriteTemplate,
    "LiveRealTimeClip": doLiveRealTimeClip,
    "ComposeMedia": doComposeMedia,
    "ProcessMedia": doProcessMedia,
    "DescribeSampleSnapshotTemplates": doDescribeSampleSnapshotTemplates,
    "DescribeImageSpriteTemplates": doDescribeImageSpriteTemplates,
    "ProcessMediaByProcedure": doProcessMediaByProcedure,
    "CreateAIAnalysisTemplate": doCreateAIAnalysisTemplate,
    "DescribeAIRecognitionTemplates": doDescribeAIRecognitionTemplates,
    "DescribeWatermarkTemplates": doDescribeWatermarkTemplates,
    "CreateImageSpriteTemplate": doCreateImageSpriteTemplate,
    "DeleteImageSpriteTemplate": doDeleteImageSpriteTemplate,
    "DescribeTranscodeTemplates": doDescribeTranscodeTemplates,
    "DescribeContentReviewTemplates": doDescribeContentReviewTemplates,

}

AVAILABLE_VERSION_LIST = [
    v20180717.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180717.version.replace('-', ''): {"help": v20180717_help.INFO,"desc": v20180717_help.DESC},

}


def vod_action(argv, arglist):
    if "help" in argv:
        versions = sorted(AVAILABLE_VERSIONS.keys())
        opt_v = "--" + OptionsDefine.Version
        version = versions[-1]
        if opt_v in argv:
            version = 'v' + argv[opt_v].replace('-', '')
        if version not in versions:
            print("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
            return
        action_str = ""
        docs = AVAILABLE_VERSIONS[version]["help"]
        desc = AVAILABLE_VERSIONS[version]["desc"]
        for action, info in docs.items():
            action_str += "        %s\n" % action
            action_str += Utils.split_str("        ", info["desc"], 120)
        helpstr = HelpTemplate.SERVICE % {"name": "vod", "desc": desc, "actions": action_str}
        print(helpstr)
    else:
        print(ErrorMsg.FEW_ARG)


def version_merge():
    help_merge = {}
    for v in AVAILABLE_VERSIONS:
        for action in AVAILABLE_VERSIONS[v]["help"]:
            if action not in help_merge:
                help_merge[action] = {}
            help_merge[action]["cb"] = ACTION_MAP[action]
            help_merge[action]["params"] = []
            for param in AVAILABLE_VERSIONS[v]["help"][action]["params"]:
                if param["name"] not in help_merge[action]["params"]:
                    help_merge[action]["params"].append(param["name"])
    return help_merge


def register_arg(command):
    cmd = NiceCommand("vod", vod_action)
    command.reg_cmd(cmd)
    cmd.reg_opt("help", "bool")
    cmd.reg_opt(OptionsDefine.Version, "string")
    help_merge = version_merge()

    for actionName, action in help_merge.items():
        c = NiceCommand(actionName, action["cb"])
        cmd.reg_cmd(c)
        c.reg_opt("help", "bool")
        for param in action["params"]:
            c.reg_opt("--" + param, "string")

        for opt in OptionsDefine.ACTION_GLOBAL_OPT:
            stropt = "--" + opt
            c.reg_opt(stropt, "string")


def parse_global_arg(argv):
    params = {}
    for opt in OptionsDefine.ACTION_GLOBAL_OPT:
        stropt = "--" + opt
        if stropt in argv:
            params[opt] = argv[stropt]
        else:
            params[opt] = None
    if params[OptionsDefine.Version]:
        params[OptionsDefine.Version] = "v" + params[OptionsDefine.Version].replace('-', '')

    config_handle = Configure()
    profile = config_handle.profile
    if ("--" + OptionsDefine.Profile) in argv:
        profile = argv[("--" + OptionsDefine.Profile)]

    is_conexist, conf_path = config_handle._profile_existed(profile + "." + config_handle.configure)
    is_creexist, cred_path = config_handle._profile_existed(profile + "." + config_handle.credential)
    config = {}
    cred = {}
    if is_conexist:
        config = config_handle._load_json_msg(conf_path)
    if is_creexist:
        cred = config_handle._load_json_msg(cred_path)
    if os.environ.get(OptionsDefine.ENV_SECRET_ID):
        cred[OptionsDefine.SecretId] = os.environ.get(OptionsDefine.ENV_SECRET_ID)
    if os.environ.get(OptionsDefine.ENV_SECRET_KEY):
        cred[OptionsDefine.SecretKey] = os.environ.get(OptionsDefine.ENV_SECRET_KEY)
    if os.environ.get(OptionsDefine.ENV_REGION):
        config[OptionsDefine.Region] = os.environ.get(OptionsDefine.ENV_REGION)

    for param in params.keys():
        if param == OptionsDefine.Version:
            continue
        if params[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId]:
                if param in cred:
                    params[param] = cred[param]
                else:
                    raise Exception("%s is invalid" % param)
            else:
                if param in config:
                    params[param] = config[param]
                elif param == OptionsDefine.Region:
                    raise Exception("%s is invalid" % OptionsDefine.Region)
    try:
        if params[OptionsDefine.Version] is None:
            version = config["vod"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["vod"][OptionsDefine.Endpoint]
    except Exception as err:
        raise Exception("config file:%s error, %s" % (conf_path, str(err)))
    versions = sorted(AVAILABLE_VERSIONS.keys())
    if params[OptionsDefine.Version] not in versions:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
    return params


def show_help(action, version):
    docs = AVAILABLE_VERSIONS[version]["help"][action]
    desc = AVAILABLE_VERSIONS[version]["desc"]
    docstr = ""
    for param in docs["params"]:
        docstr += "        %s\n" % ("--" + param["name"])
        docstr += Utils.split_str("        ", param["desc"], 120)

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "vod", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["vod"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]

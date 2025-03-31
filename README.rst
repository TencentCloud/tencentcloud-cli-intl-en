Install
=======

.. code-block:: sh

    pip install tccli-intl-en
    complete -C 'tccli_completer' tccli

Configure
=========

.. code-block:: sh

    $  tccli configure
    TencentCloud API secretId [*afcQ]:AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
    TencentCloud API secretKey [*ArFd]:OxXj7khcV1234dQSSYNABcdCc1LiArFd
    region: ap-guangzhou
    output[json]:

SecretId: Cloud API key SecretId. SecretIKey: Cloud API key SecretKey. Region: Tencent Cloud services region. Please move to the corresponding product page to get the available region. Output: optional parameter, request return packet output format, support [ Json table text] three formats, default is json. For more information, please perform tccli configure help view.

Note: if the environment variable defines the relevant configuration, it takes precedence over the configuration file. They are TENCENTCLOUD. \_ SECRET \_ ID,TENCENTCLOUD \_ SECRET \_ KEY,TENCENTCLOUD \_ REGION .

Usage
=====

.. code-block:: sh

    tccli cvm RunInstances --InstanceChargeType POSTPAID_BY_HOUR --Placement '{"Zone":"ap-guangzhou-2"}' --InstanceType S1.SMALL1 --ImageId img-8toqc6s3 --SystemDisk '{"DiskType":"CLOUD_BASIC", "DiskSize":50}' --InternetAccessible '{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":10,"PublicIpAssigned":true}' --InstanceCount 1 --InstanceName TCCLI-TEST --LoginSettings '{"Password":"P1easeChange1t@"}' --HostName TCCLI-HOST-NAME1


Note: If a parameter is not a basic type (number or string), you need to specify a json string format. For example, above parameter `Placement` is a dictionary object, so its format is a quoted json string `'{"Zone":"ap-guangzhou-2"}'`. For list type parameter, such as `SecurityGroupIds`, its format is a quoted json string like `["sg-1q2w3e4r"]`.

Compliance Notice
=================

Please prioritize using the ​default domain names configured in the SDK for each product. If using other domains, note that ​overseas domains may pose ​data compliance risks.

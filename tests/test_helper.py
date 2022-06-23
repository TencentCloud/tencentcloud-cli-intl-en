# -*- coding:utf8 -*-
from utils import TestCli


def test_help():
    cmd = 'tccli help'
    expect = 'tccli [options] <service> [options] <action> [options] [options and parameters]'
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_cvm_help():
    cmd = 'tccli cvm help'
    expect = '<DescribeRegions>'
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_cvm_help_detail():
    cmd = 'tccli cvm help --detail'
    expect = 'AVAILABLE ACTIONS\n    AllocateHosts'
    test_cli = TestCli()
    test_cli.equal(cmd, expect)

# -*- coding: utf-8 -*-
DESC = "tke-2018-05-25"
INFO = {
  "CreateCluster": {
    "params": [
      {
        "name": "ClusterCIDRSettings",
        "desc": "Container networking configuration information for the cluster"
      },
      {
        "name": "ClusterType",
        "desc": "Cluster type. Managed cluster: MANAGED_CLUSTER; self-deployed cluster: INDEPENDENT_CLUSTER."
      },
      {
        "name": "RunInstancesForNode",
        "desc": "Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the API for [creating a CVM instance](https://cloud.tencent.com/document/product/213/15730)."
      },
      {
        "name": "ClusterBasicSettings",
        "desc": "Basic configuration information of the cluster"
      },
      {
        "name": "ClusterAdvancedSettings",
        "desc": "Advanced configuration information of the cluster"
      },
      {
        "name": "InstanceAdvancedSettings",
        "desc": "Advanced configuration information of the node"
      },
      {
        "name": "ExistedInstancesForNode",
        "desc": "Configuration information of an existing instance"
      },
      {
        "name": "InstanceDataDiskMountSettings",
        "desc": "CVM type and the corresponding data disk mounting configuration information."
      }
    ],
    "desc": "This API is used to create a cluster."
  },
  "DescribeImages": {
    "params": [],
    "desc": "This API is used to get image information."
  },
  "ModifyClusterAsGroupAttribute": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "ClusterAsGroupAttribute",
        "desc": "Cluster-associated scaling group attributes"
      }
    ],
    "desc": "Modify cluster scaling group attributes"
  },
  "DeleteClusterEndpoint": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "IsExtranet",
        "desc": "Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE)."
      }
    ],
    "desc": "Delete the cluster access port (intranet / extranet access is enabled for independent clusters, and intranet access is supported for managed clusters)"
  },
  "CreateClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID. Enter the ClusterId field returned by the DescribeClusters API"
      },
      {
        "name": "RunInstancePara",
        "desc": "Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the [RunInstances](https://cloud.tencent.com/document/product/213/15730) API."
      },
      {
        "name": "InstanceAdvancedSettings",
        "desc": "Additional parameter to be set for the instance"
      }
    ],
    "desc": "This API is used to create one or more nodes in a cluster."
  },
  "ModifyClusterAttribute": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "ProjectId",
        "desc": "Project of the Cluster"
      },
      {
        "name": "ClusterName",
        "desc": "Cluster name"
      },
      {
        "name": "ClusterDesc",
        "desc": "Cluster description"
      }
    ],
    "desc": "This API is used to modify cluster attributes."
  },
  "DeleteClusterAsGroups": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "The cluster ID, obtained through the [DescribeClusters](https://cloud.tencent.com/document/api/457/31862) API."
      },
      {
        "name": "AutoScalingGroupIds",
        "desc": "Cluster scaling group ID list"
      },
      {
        "name": "KeepInstance",
        "desc": "Whether to keep nodes in the scaling group. Default to **false** (not keep)"
      }
    ],
    "desc": "Delete a cluster scaling group"
  },
  "DeleteClusterRoute": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "Route table name."
      },
      {
        "name": "GatewayIp",
        "desc": "Next hop address."
      },
      {
        "name": "DestinationCidrBlock",
        "desc": "Destination CIDR."
      }
    ],
    "desc": "This API is used to delete a cluster route."
  },
  "DescribeClusterEndpointVipStatus": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      }
    ],
    "desc": "Query cluster open port process status (only supports external ports of the managed cluster)"
  },
  "DeleteCluster": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "InstanceDeleteMode",
        "desc": "Policy used to delete an instance in the cluster: terminate (terminates the instance. Only available for instances on pay-as-you-go CVMs); retain (only removes it from the cluster. The instance will be retained.)"
      },
      {
        "name": "ResourceDeleteOptions",
        "desc": "Specifies the policy to deal with resources in the cluster when the cluster is deleted. It only supports CBS now. The default policy is to retain CBS disks."
      }
    ],
    "desc": "This API is used to delete a cluster. (Cloud API v3)."
  },
  "CreateClusterAsGroup": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "AutoScalingGroupPara",
        "desc": "The pass-through parameters for scaling group creation, in the format of a JSON string. For more information, see the [CreateAutoScalingGroup](https://cloud.tencent.com/document/api/377/20440) API. The **LaunchConfigurationId** is created with the LaunchConfigurePara parameter, which does not support data entry."
      },
      {
        "name": "LaunchConfigurePara",
        "desc": "The pass-through parameters for launch configuration creation, in the format of a JSON string. For more information, see the [CreateLaunchConfiguration](https://cloud.tencent.com/document/api/377/20447) API. **ImageId** is not required as it is already included in the cluster dimension. **UserData** is not required as it's set through the **UserScript**."
      },
      {
        "name": "InstanceAdvancedSettings",
        "desc": "Advanced configuration information of the node"
      },
      {
        "name": "Labels",
        "desc": "Node label array"
      }
    ],
    "desc": "Create a scaling group for an existing cluster"
  },
  "DescribeExistedInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID. Enter the `ClusterId` field returned when you call the DescribeClusters API (Only VPC ID obtained through `ClusterId` need filtering conditions. When comparing statuses, the nodes on all clusters in this region will be used for comparison. You cannot specify `InstanceIds` and `ClusterId` at the same time.)"
      },
      {
        "name": "InstanceIds",
        "desc": "Query by one or more instance ID(s). Instance ID format: ins-xxxxxxxx. (Refer to section ID.N of the API overview for this parameter's specific format.) Up to 100 instances are allowed for each request. You cannot specify InstanceIds and Filters at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. For fields and other information, see [the DescribeInstances API](https://cloud.tencent.com/document/api/213/15728). If a ClusterId has been set, then the cluster's VPC ID will be attached as a query field. In this situation, if a \"vpc-id\" is specified in Filter, then the specified VPC ID must be consistent with the cluster's VPC ID."
      },
      {
        "name": "VagueIpAddress",
        "desc": "Filter by instance IP (Supports both private and public IPs)"
      },
      {
        "name": "VagueInstanceName",
        "desc": "Filter by instance name"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on Offset, see the relevant section in the API [Introduction](https://cloud.tencent.com/document/api/213/15688)."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on Limit, see the relevant section in the API [Introduction](https://cloud.tencent.com/document/api/213/15688)."
      }
    ],
    "desc": "This API is used to query one or more existing node and determine whether they can be added to a cluster."
  },
  "CreateClusterRouteTable": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "Route table name"
      },
      {
        "name": "RouteTableCidrBlock",
        "desc": "Route table CIDR"
      },
      {
        "name": "VpcId",
        "desc": "VPC bound to the route table"
      },
      {
        "name": "IgnoreClusterCidrConflict",
        "desc": "Whether to ignore CIDR conflicts"
      }
    ],
    "desc": "This API is used to create a cluster route table."
  },
  "DescribeClusterAsGroupOption": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      }
    ],
    "desc": "Cluster auto scaling configuration"
  },
  "DescribeClusters": {
    "params": [
      {
        "name": "ClusterIds",
        "desc": "Cluster ID list (When it is empty,\nall clusters under the account will be obtained)"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of output entries. Default value: 20"
      },
      {
        "name": "Filters",
        "desc": "Filter condition. Currently, only filtering by a single ClusterName is supported"
      }
    ],
    "desc": "This API is used to query clusters list."
  },
  "DescribeClusterEndpointStatus": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "IsExtranet",
        "desc": "Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE)."
      }
    ],
    "desc": "Query cluster access port status (intranet / extranet access is enabled for independent clusters, and intranet access is supported for managed clusters)"
  },
  "DescribeClusterAsGroups": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "AutoScalingGroupIds",
        "desc": "Scaling group ID list. If this value is null, it indicates that all cluster-associated scaling groups are pulled."
      },
      {
        "name": "Offset",
        "desc": "Offset. This value defaults to 0. For more information on Offset, see the relevant sections in API [Overview](https://cloud.tencent.com/document/api/213/15688)."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. This value defaults to 20. The maximum is 100. For more information on Limit, see the relevant sections in API [Overview](https://cloud.tencent.com/document/api/213/15688)."
      }
    ],
    "desc": "Cluster-associated scaling group list"
  },
  "CreateClusterEndpoint": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "SubnetId",
        "desc": "The ID of the subnet where the cluster's port is located (only needs to be entered when the non-public network access is enabled, and must be within the subnet of the cluster's VPC). "
      },
      {
        "name": "IsExtranet",
        "desc": "Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE)."
      }
    ],
    "desc": "Create a cluster access port (intranet / extranet access is enabled for independent clusters, and intranet access is supported for managed clusters)"
  },
  "DescribeClusterRouteTables": {
    "params": [],
    "desc": "This API is used to query one or more cluster route tables."
  },
  "DescribeRegions": {
    "params": [],
    "desc": "This API is used to obtain all regions supported by TKE."
  },
  "AddExistedInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "InstanceIds",
        "desc": "Instance list"
      },
      {
        "name": "InstanceAdvancedSettings",
        "desc": "Additional parameter to be set for the instance"
      },
      {
        "name": "EnhancedService",
        "desc": "Enhanced services. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitor and Cloud Security are enabled by default."
      },
      {
        "name": "LoginSettings",
        "desc": "Node login information (currently only supports using Password or single KeyIds)"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "Security group to which the instance belongs. This parameter can be obtained from the `sgId` field returned by DescribeSecurityGroups. If this parameter is not specified, the default security group is bound. (Currently, you can only set a single sgId)"
      },
      {
        "name": "HostName",
        "desc": ""
      }
    ],
    "desc": "This API is used to add one or more existing instances to a cluster."
  },
  "DescribeClusterSecurity": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID. Enter the ClusterId field returned by the DescribeClusters API"
      }
    ],
    "desc": "This API is used to query the key information of a cluster."
  },
  "DescribeRouteTableConflicts": {
    "params": [
      {
        "name": "RouteTableCidrBlock",
        "desc": "Route table CIDR"
      },
      {
        "name": "VpcId",
        "desc": "VPC bound to the route table"
      }
    ],
    "desc": "This API is used to query the list of route table conflicts."
  },
  "DescribeClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of output entries. Default value: 20"
      },
      {
        "name": "InstanceIds",
        "desc": "List of instance IDs to be obtained. This parameter is empty by default, which indicates that all instances in the cluster will be pulled."
      },
      {
        "name": "InstanceRole",
        "desc": ""
      }
    ],
    "desc": " This API is used to query information of one or more instances in a cluster. "
  },
  "DeleteClusterEndpointVip": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      }
    ],
    "desc": "Delete the external network access port of the managed cluster (the old way, only the external network port of the managed cluster is supported)"
  },
  "DeleteClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "InstanceIds",
        "desc": "List of Instance IDs"
      },
      {
        "name": "InstanceDeleteMode",
        "desc": "Policy used to delete an instance in the cluster: `terminate` (terminates the instance. Only available for pay-as-you-go CVMs); `retain` (only removes it from the cluster. The instance will be retained.)"
      },
      {
        "name": "ForceDelete",
        "desc": ""
      }
    ],
    "desc": "This API is used to delete one or more nodes from a cluster."
  },
  "ModifyClusterEndpointSP": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "SecurityPolicies",
        "desc": "Security policy opens single IP or CIDR block to the Internet (for example: '192.168.1.0/24', with 'reject all' as the default)."
      }
    ],
    "desc": "Modify the security policy of the external port of the managed cluster (the old way, only the external port of the managed cluster is supported)"
  },
  "CreateClusterEndpointVip": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "Cluster ID"
      },
      {
        "name": "SecurityPolicies",
        "desc": "Security policy opens single IP or CIDR to the Internet (for example: '192.168.1.0/24', with 'reject all' as the default)."
      }
    ],
    "desc": "Create an external network access port for the managed cluster (the old way, only the external network port for the managed cluster is supported)"
  },
  "DeleteClusterRouteTable": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "Route table name"
      }
    ],
    "desc": "This API is used to delete cluster a route table."
  },
  "DescribeClusterRoutes": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "Route table name."
      }
    ],
    "desc": "This API is used to query cluster routes."
  }
}
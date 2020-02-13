# -*- coding: utf-8 -*-
DESC = "billing-2018-07-09"
INFO = {
  "DescribeBillDetail": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Quantity, maximum is 100"
      },
      {
        "name": "PeriodType",
        "desc": "The period type. byUsedTime: By usage period; byPayTime: By payment period. Must be the same as the period of the current monthly bill of the Billing Center. You can check your bill statistics period type at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page. "
      },
      {
        "name": "Month",
        "desc": "Month; format: yyyy-mm. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available."
      },
      {
        "name": "BeginTime",
        "desc": "The start time of the period; format: Y-m-d H:i:s. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. BeginTime and EndTime must be inputted as a pair. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available."
      },
      {
        "name": "EndTime",
        "desc": "The end time of the period; format: Y-m-d H:i:s. You only have to enter either Month or BeginTime and EndTime. When you enter values for BeginTime and EndTime, Month becomes invalid. BeginTime and EndTime must be inputted as a pair. This value must be no earlier than the month when Bill 2.0 is activated; last 24 months data are available."
      },
      {
        "name": "NeedRecordNum",
        "desc": "Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.\n1 = yes, 0 = no"
      },
      {
        "name": "ProductCode",
        "desc": "Queries information on a specified product"
      },
      {
        "name": "PayMode",
        "desc": "Billing mode: prePay/postPay"
      },
      {
        "name": "ResourceId",
        "desc": "Queries information on a specified resource"
      }
    ],
    "desc": "This API is used to query bill details."
  },
  "DescribeBillSummaryByPayMode": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "Query bill data user’s UIN"
      },
      {
        "name": "BeginTime",
        "desc": "Only beginning in the current month is supported, and it must be the same month as the EndTime. For example, 2018-09-01 00:00:00."
      },
      {
        "name": "EndTime",
        "desc": "Only ending in the current month is supported, and it must be the same month as the BeginTime. For example, 2018-09-30 23:59:59."
      }
    ],
    "desc": "Gets the bill summarized according to billing mode"
  },
  "DescribeBillResourceSummary": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Quantity, maximum is 1000"
      },
      {
        "name": "PeriodType",
        "desc": "The period type. byUsedTime: By usage period; byPayTime: by payment period. Must be the same as the period of the current monthly bill of the Billing Center. You can check your bill statistics period type at the top of the [Bill Overview](https://console.cloud.tencent.com/expense/bill/overview) page."
      },
      {
        "name": "Month",
        "desc": "Month; format: yyyy-mm. This value cannot be earlier than the month when Bill 2.0 is enabled. Last 24 months data are available."
      },
      {
        "name": "NeedRecordNum",
        "desc": "Indicates whether or not the total number of records of accessing the list is required, used for frontend pages.\n1 = yes, 0 = no"
      }
    ],
    "desc": "This API is used to query bill resources summary. "
  },
  "DescribeBillSummaryByRegion": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "Queries bill data user’s UIN"
      },
      {
        "name": "BeginTime",
        "desc": "Only beginning in the current month is supported, and it must be the same month as the EndTime. For example, 2018-09-01 00:00:00."
      },
      {
        "name": "EndTime",
        "desc": "Only ending in the current month is supported, and it must be the same month as the BeginTime. For example, 2018-09-30 23:59:59."
      }
    ],
    "desc": "Gets the bill summarized according to region"
  },
  "DescribeBillSummaryByProject": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "Queries bill data user’s UIN"
      },
      {
        "name": "BeginTime",
        "desc": "Only beginning in the current month is supported, and it must be the same month as the EndTime. For example, 2018-09-01 00:00:00."
      },
      {
        "name": "EndTime",
        "desc": "Only ending in the current month is supported, and it must be the same month as the BeginTime. For example, 2018-09-30 23:59:59."
      }
    ],
    "desc": "Gets the bill summarized according to project"
  },
  "DescribeBillSummaryByProduct": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "Queries bill data user’s UIN"
      },
      {
        "name": "BeginTime",
        "desc": "Only beginning in the current month is supported, and it must be the same month as the EndTime. For example, 2018-09-01 00:00:00."
      },
      {
        "name": "EndTime",
        "desc": "Only ending in the current month is supported, and it must be the same month as the BeginTime. For example, 2018-09-30 23:59:59."
      }
    ],
    "desc": "Gets the bill summarized according to product"
  },
  "DescribeBillSummaryByTag": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "Payer UIN"
      },
      {
        "name": "BeginTime",
        "desc": "Currently the period to be queried must start from a time point in the current month, and the starting time and the end time must be in the same month. Example: 2018-09-01 00:00:00."
      },
      {
        "name": "EndTime",
        "desc": "Currently the period to be queried must end at a time point in the current month, and the starting time and the end time must be in the same month. Example: 2018-09-30 23:59:59."
      },
      {
        "name": "TagKey",
        "desc": "Cost allocation tag key"
      }
    ],
    "desc": "This API is used to get the cost distribution over different tags."
  }
}
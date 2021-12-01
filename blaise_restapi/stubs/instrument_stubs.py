from typing import Any, Dict, List


def api_instruments_with_cati_data_stub_response() -> List[Dict[str, Any]]:
    return [
        {
            "name": "DST2106X",
            "id": "12345-12345-12345-12345-XXXXX",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.99999+01:00",
            "status": "Active",
            "dataRecordCount": 1337,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ],
            "Active": True,
            "ActiveToday": True,
            "DeliverData": True,
            "surveyDays": [
                "2021-01-28T00:00:00",
                "2021-01-29T00:00:00",
            ],
        },
        {
            "name": "DST2106Y",
            "id": "12345-12345-12345-12345-YYYYY",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.99999+01:00",
            "status": "Active",
            "dataRecordCount": 42,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ],
            "Active": False,
            "ActiveToday": False,
            "DeliverData": False,
            "surveyDays": [
                "2021-04-01T00:00:00",
                "2021-04-02T00:00:00",
            ],
        },
    ]


def api_instrument_with_cati_data_stub_response() -> Dict[str, Any]:
    return {
            "name": "DST2106X",
            "id": "12345-12345-12345-12345-XXXXX",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.99999+01:00",
            "status": "Active",
            "dataRecordCount": 1337,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ],
            "Active": True,
            "ActiveToday": True,
            "DeliverData": True,
            "surveyDays": [
                "2021-01-28T00:00:00",
                "2021-01-29T00:00:00",
            ],
        }


def api_instruments_stub_response() -> List[Dict[str, Any]]:
    return [
        {
            "name": "DST2106X",
            "id": "12345-12345-12345-12345-XXXXX",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.99999+01:00",
            "status": "Active",
            "dataRecordCount": 1337,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        },
        {
            "name": "DST2106Y",
            "id": "12345-12345-12345-12345-YYYYY",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.99999+01:00",
            "status": "Active",
            "dataRecordCount": 42,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        },
        {
            "name": "DST2106Z",
            "id": "12345-12345-12345-12345-ZZZZZ",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.99999+01:00",
            "status": "Active",
            "dataRecordCount": 999,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        }
    ]


def api_instrument_stub_response() -> Dict[str, Any]:
    return {
            "name": "DST2106X",
            "id": "12345-12345-12345-12345-XXXXX",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.99999+01:00",
            "status": "Active",
            "dataRecordCount": 1337,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        }


def api_instrument_data_response() -> Dict[str, Any]:
    return {
        "instrumentName": "DST2106Z",
        "instrumentId": "12345-12345-12345-12345-12345",
        "reportingData": [
            {
                "qiD.Serial_Number": "10010",
                "qhAdmin.HOut": "110"
            },
            {
                "qiD.Serial_Number": "10020",
                "qhAdmin.HOut": "110"
            },
            {
                "qiD.Serial_Number": "10030",
                "qhAdmin.HOut": "110"

            }
        ]
    }


def api_install_instrument_response() -> Dict[str, Any]:
    return {
        "instrumentFile": "DST2106Z.bpkg"
    }


def api_create_case_response() -> Dict[str, Any]:
    return {
        "caseId": "1000001"
    }
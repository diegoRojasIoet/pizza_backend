import pytest


def test_get_repor_service(client, create_orders, report_uri):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
    returned_report = response.json
    assert(returned_report['most_requested_ingredient'])
    assert(returned_report['month_with_more_revenue'])
    assert(returned_report['top_3_clients'])

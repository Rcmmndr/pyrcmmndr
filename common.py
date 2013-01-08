import json
import httplib2
import logging as logger

__author__ = 'codemomentum'

def get_content(url):
    try:
        h = httplib2.Http()
        resp, content = h.request(url, 'GET', headers={'Content-Type': 'application/json'})
        assert (resp.status is 200) or (resp.status is 201) or (resp.status is 204)
        logger.info('Http GET Finished [%s]', url)
    except Exception as e:
        logger.exception('Http Request To the Url [%s] failed: %s', url, e)
        raise e
    except AssertionError as ae:
        logger.exception('Expected Response status was 200x but it is  [%s]', resp.status)
        raise ae
    return parse_json(content)


def post_content(url, body, request_headers=None):
    if not request_headers: request_headers = {'Content-Type': 'application/json'}
    try:
        h = httplib2.Http()
        resp, content = h.request(url, 'POST', body, headers=request_headers)
        assert (resp.status is 200) or (resp.status is 201) or (resp.status is 204)
        logger.info('Http POST Finished [%s]', url)
    except Exception as e:
        logger.exception('Http Request To the Url [%s] failed: %s', url, e)
        raise e
    except AssertionError as ae:
        logger.exception('Expected Response status was 200x but it is  [%s]', resp.status)
        raise ae
    return content


def put_content(url, body):
    try:
        h = httplib2.Http()
        resp, content = h.request(url, 'PUT', body, headers={'Content-Type': 'application/json'})
        assert (resp.status is 200) or (resp.status is 201) or (resp.status is 204)
        logger.info('Http PUT Finished [%s]', url)
    except Exception as e:
        logger.exception('Http Request To the Url [%s] failed: %s', url, e)
        raise e
    except AssertionError as ae:
        logger.exception('Expected Response status was 200x but it is  [%s]', resp.status)
        raise ae
    return content


def delete_content(url):
    try:
        h = httplib2.Http()
        resp, content = h.request(url, 'DELETE', headers={'Content-Type': 'application/json'})
        assert (resp.status is 200) or (resp.status is 201) or (resp.status is 204)
        logger.info('Http DELETE Finished [%s]', url)
    except Exception as e:
        logger.exception('Http Request To the Url [%s] failed: %s', url, e)
        raise e
    except AssertionError as ae:
        logger.exception('Expected Response status was 200x but it is  [%s]', resp)
        raise ae


def parse_json(json_body):
    return json.loads(json_body)
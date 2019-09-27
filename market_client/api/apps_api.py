# coding: utf-8

"""
    rainbond cloud app market OpenAPI.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: 576501057@qq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from market_client.api_client import ApiClient


class AppsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def download_app_by_order(self, order_id, **kwargs):  # noqa: E501
        """download_app_by_order  # noqa: E501

        download app installation metadata by order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_app_by_order(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int order_id: an id of order (required)
        :return: StoreAppVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_app_by_order_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_app_by_order_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def download_app_by_order_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """download_app_by_order  # noqa: E501

        download app installation metadata by order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_app_by_order_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int order_id: an id of order (required)
        :return: StoreAppVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_app_by_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `download_app_by_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderID'] = params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['enterprise_key', 'token_key']  # noqa: E501

        return self.api_client.call_api(
            '/openapi/v2/orders/{orderID}/downloadapp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreAppVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_recommended_app_list(self, **kwargs):  # noqa: E501
        """get recommended app list  # noqa: E501

        This will show recommended app  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recommended_app_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: current page number
        :param int limit: current page limit number
        :param int group_name: search for application name
        :return: AppListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_recommended_app_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_recommended_app_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_recommended_app_list_with_http_info(self, **kwargs):  # noqa: E501
        """get recommended app list  # noqa: E501

        This will show recommended app  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recommended_app_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: current page number
        :param int limit: current page limit number
        :param int group_name: search for application name
        :return: AppListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'group_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recommended_app_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'group_name' in params:
            query_params.append(('group_name', params['group_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['enterprise_key', 'token_key']  # noqa: E501

        return self.api_client.call_api(
            '/openapi/v2/recommended/apps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

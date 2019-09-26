# coding: utf-8

"""
    rainbond cloud app market OpenAPI.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: 576501057@qq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AppListRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'group_name': 'int',
        'limit': 'int',
        'page': 'int'
    }

    attribute_map = {
        'group_name': 'group_name',
        'limit': 'limit',
        'page': 'page'
    }

    def __init__(self, group_name=None, limit=None, page=None):  # noqa: E501
        """AppListRequest - a model defined in Swagger"""  # noqa: E501

        self._group_name = None
        self._limit = None
        self._page = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if limit is not None:
            self.limit = limit
        if page is not None:
            self.page = page

    @property
    def group_name(self):
        """Gets the group_name of this AppListRequest.  # noqa: E501

        search for application name  In: query  # noqa: E501

        :return: The group_name of this AppListRequest.  # noqa: E501
        :rtype: int
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AppListRequest.

        search for application name  In: query  # noqa: E501

        :param group_name: The group_name of this AppListRequest.  # noqa: E501
        :type: int
        """

        self._group_name = group_name

    @property
    def limit(self):
        """Gets the limit of this AppListRequest.  # noqa: E501

        current page limit number  In: query  # noqa: E501

        :return: The limit of this AppListRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this AppListRequest.

        current page limit number  In: query  # noqa: E501

        :param limit: The limit of this AppListRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def page(self):
        """Gets the page of this AppListRequest.  # noqa: E501

        current page number  In: query  # noqa: E501

        :return: The page of this AppListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AppListRequest.

        current page number  In: query  # noqa: E501

        :param page: The page of this AppListRequest.  # noqa: E501
        :type: int
        """

        self._page = page

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AppListRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
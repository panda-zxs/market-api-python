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

from market_client.models.delivery_mode import DeliveryMode  # noqa: F401,E501
from market_client.models.enterprise import Enterprise  # noqa: F401,E501
from market_client.models.store_app_tag import StoreAppTag  # noqa: F401,E501
from market_client.models.store_app_version import StoreAppVersion  # noqa: F401,E501


class StoreApp(object):
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
        'app_detail_url': 'str',
        'app_key_id': 'str',
        'app_tag_ids': 'list[str]',
        'app_tags': 'list[StoreAppTag]',
        'app_type_id': 'str',
        'app_versions': 'list[StoreAppVersion]',
        'code_page': 'str',
        'create_time': 'datetime',
        'delivery_mode': 'list[DeliveryMode]',
        'desc': 'str',
        'download_count': 'int',
        'enterprise': 'Enterprise',
        'enterprise_id': 'str',
        'home_page': 'str',
        'install_count': 'int',
        'install_status': 'bool',
        'introduction': 'str',
        'is_official': 'bool',
        'joint_cloud_id': 'str',
        'logo': 'str',
        'name': 'str',
        'pic': 'list[str]',
        'price': 'float',
        'publish_type': 'str',
        'show_count': 'int',
        'start_count': 'int',
        'status': 'str',
        'update_time': 'datetime'
    }

    attribute_map = {
        'app_detail_url': 'app_detail_url',
        'app_key_id': 'app_key_id',
        'app_tag_ids': 'app_tag_ids',
        'app_tags': 'app_tags',
        'app_type_id': 'app_type_id',
        'app_versions': 'app_versions',
        'code_page': 'code_page',
        'create_time': 'create_time',
        'delivery_mode': 'delivery_mode',
        'desc': 'desc',
        'download_count': 'download_count',
        'enterprise': 'enterprise',
        'enterprise_id': 'enterprise_id',
        'home_page': 'home_page',
        'install_count': 'install_count',
        'install_status': 'install_status',
        'introduction': 'introduction',
        'is_official': 'is_official',
        'joint_cloud_id': 'joint_cloud_id',
        'logo': 'logo',
        'name': 'name',
        'pic': 'pic',
        'price': 'price',
        'publish_type': 'publish_type',
        'show_count': 'show_count',
        'start_count': 'start_count',
        'status': 'status',
        'update_time': 'update_time'
    }

    def __init__(self, app_detail_url=None, app_key_id=None, app_tag_ids=None, app_tags=None, app_type_id=None, app_versions=None, code_page=None, create_time=None, delivery_mode=None, desc=None, download_count=None, enterprise=None, enterprise_id=None, home_page=None, install_count=None, install_status=None, introduction=None, is_official=None, joint_cloud_id=None, logo=None, name=None, pic=None, price=None, publish_type=None, show_count=None, start_count=None, status=None, update_time=None):  # noqa: E501
        """StoreApp - a model defined in Swagger"""  # noqa: E501

        self._app_detail_url = None
        self._app_key_id = None
        self._app_tag_ids = None
        self._app_tags = None
        self._app_type_id = None
        self._app_versions = None
        self._code_page = None
        self._create_time = None
        self._delivery_mode = None
        self._desc = None
        self._download_count = None
        self._enterprise = None
        self._enterprise_id = None
        self._home_page = None
        self._install_count = None
        self._install_status = None
        self._introduction = None
        self._is_official = None
        self._joint_cloud_id = None
        self._logo = None
        self._name = None
        self._pic = None
        self._price = None
        self._publish_type = None
        self._show_count = None
        self._start_count = None
        self._status = None
        self._update_time = None
        self.discriminator = None

        if app_detail_url is not None:
            self.app_detail_url = app_detail_url
        if app_key_id is not None:
            self.app_key_id = app_key_id
        if app_tag_ids is not None:
            self.app_tag_ids = app_tag_ids
        if app_tags is not None:
            self.app_tags = app_tags
        if app_type_id is not None:
            self.app_type_id = app_type_id
        if app_versions is not None:
            self.app_versions = app_versions
        if code_page is not None:
            self.code_page = code_page
        if create_time is not None:
            self.create_time = create_time
        if delivery_mode is not None:
            self.delivery_mode = delivery_mode
        if desc is not None:
            self.desc = desc
        if download_count is not None:
            self.download_count = download_count
        if enterprise is not None:
            self.enterprise = enterprise
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if home_page is not None:
            self.home_page = home_page
        if install_count is not None:
            self.install_count = install_count
        if install_status is not None:
            self.install_status = install_status
        if introduction is not None:
            self.introduction = introduction
        if is_official is not None:
            self.is_official = is_official
        if joint_cloud_id is not None:
            self.joint_cloud_id = joint_cloud_id
        if logo is not None:
            self.logo = logo
        if name is not None:
            self.name = name
        if pic is not None:
            self.pic = pic
        if price is not None:
            self.price = price
        if publish_type is not None:
            self.publish_type = publish_type
        if show_count is not None:
            self.show_count = show_count
        if start_count is not None:
            self.start_count = start_count
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time

    @property
    def app_detail_url(self):
        """Gets the app_detail_url of this StoreApp.  # noqa: E501


        :return: The app_detail_url of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._app_detail_url

    @app_detail_url.setter
    def app_detail_url(self, app_detail_url):
        """Sets the app_detail_url of this StoreApp.


        :param app_detail_url: The app_detail_url of this StoreApp.  # noqa: E501
        :type: str
        """

        self._app_detail_url = app_detail_url

    @property
    def app_key_id(self):
        """Gets the app_key_id of this StoreApp.  # noqa: E501


        :return: The app_key_id of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._app_key_id

    @app_key_id.setter
    def app_key_id(self, app_key_id):
        """Sets the app_key_id of this StoreApp.


        :param app_key_id: The app_key_id of this StoreApp.  # noqa: E501
        :type: str
        """

        self._app_key_id = app_key_id

    @property
    def app_tag_ids(self):
        """Gets the app_tag_ids of this StoreApp.  # noqa: E501


        :return: The app_tag_ids of this StoreApp.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_tag_ids

    @app_tag_ids.setter
    def app_tag_ids(self, app_tag_ids):
        """Sets the app_tag_ids of this StoreApp.


        :param app_tag_ids: The app_tag_ids of this StoreApp.  # noqa: E501
        :type: list[str]
        """

        self._app_tag_ids = app_tag_ids

    @property
    def app_tags(self):
        """Gets the app_tags of this StoreApp.  # noqa: E501


        :return: The app_tags of this StoreApp.  # noqa: E501
        :rtype: list[StoreAppTag]
        """
        return self._app_tags

    @app_tags.setter
    def app_tags(self, app_tags):
        """Sets the app_tags of this StoreApp.


        :param app_tags: The app_tags of this StoreApp.  # noqa: E501
        :type: list[StoreAppTag]
        """

        self._app_tags = app_tags

    @property
    def app_type_id(self):
        """Gets the app_type_id of this StoreApp.  # noqa: E501


        :return: The app_type_id of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._app_type_id

    @app_type_id.setter
    def app_type_id(self, app_type_id):
        """Sets the app_type_id of this StoreApp.


        :param app_type_id: The app_type_id of this StoreApp.  # noqa: E501
        :type: str
        """

        self._app_type_id = app_type_id

    @property
    def app_versions(self):
        """Gets the app_versions of this StoreApp.  # noqa: E501


        :return: The app_versions of this StoreApp.  # noqa: E501
        :rtype: list[StoreAppVersion]
        """
        return self._app_versions

    @app_versions.setter
    def app_versions(self, app_versions):
        """Sets the app_versions of this StoreApp.


        :param app_versions: The app_versions of this StoreApp.  # noqa: E501
        :type: list[StoreAppVersion]
        """

        self._app_versions = app_versions

    @property
    def code_page(self):
        """Gets the code_page of this StoreApp.  # noqa: E501


        :return: The code_page of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._code_page

    @code_page.setter
    def code_page(self, code_page):
        """Sets the code_page of this StoreApp.


        :param code_page: The code_page of this StoreApp.  # noqa: E501
        :type: str
        """

        self._code_page = code_page

    @property
    def create_time(self):
        """Gets the create_time of this StoreApp.  # noqa: E501


        :return: The create_time of this StoreApp.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StoreApp.


        :param create_time: The create_time of this StoreApp.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def delivery_mode(self):
        """Gets the delivery_mode of this StoreApp.  # noqa: E501


        :return: The delivery_mode of this StoreApp.  # noqa: E501
        :rtype: list[DeliveryMode]
        """
        return self._delivery_mode

    @delivery_mode.setter
    def delivery_mode(self, delivery_mode):
        """Sets the delivery_mode of this StoreApp.


        :param delivery_mode: The delivery_mode of this StoreApp.  # noqa: E501
        :type: list[DeliveryMode]
        """

        self._delivery_mode = delivery_mode

    @property
    def desc(self):
        """Gets the desc of this StoreApp.  # noqa: E501


        :return: The desc of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this StoreApp.


        :param desc: The desc of this StoreApp.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def download_count(self):
        """Gets the download_count of this StoreApp.  # noqa: E501


        :return: The download_count of this StoreApp.  # noqa: E501
        :rtype: int
        """
        return self._download_count

    @download_count.setter
    def download_count(self, download_count):
        """Sets the download_count of this StoreApp.


        :param download_count: The download_count of this StoreApp.  # noqa: E501
        :type: int
        """

        self._download_count = download_count

    @property
    def enterprise(self):
        """Gets the enterprise of this StoreApp.  # noqa: E501


        :return: The enterprise of this StoreApp.  # noqa: E501
        :rtype: Enterprise
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this StoreApp.


        :param enterprise: The enterprise of this StoreApp.  # noqa: E501
        :type: Enterprise
        """

        self._enterprise = enterprise

    @property
    def enterprise_id(self):
        """Gets the enterprise_id of this StoreApp.  # noqa: E501


        :return: The enterprise_id of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this StoreApp.


        :param enterprise_id: The enterprise_id of this StoreApp.  # noqa: E501
        :type: str
        """

        self._enterprise_id = enterprise_id

    @property
    def home_page(self):
        """Gets the home_page of this StoreApp.  # noqa: E501


        :return: The home_page of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._home_page

    @home_page.setter
    def home_page(self, home_page):
        """Sets the home_page of this StoreApp.


        :param home_page: The home_page of this StoreApp.  # noqa: E501
        :type: str
        """

        self._home_page = home_page

    @property
    def install_count(self):
        """Gets the install_count of this StoreApp.  # noqa: E501


        :return: The install_count of this StoreApp.  # noqa: E501
        :rtype: int
        """
        return self._install_count

    @install_count.setter
    def install_count(self, install_count):
        """Sets the install_count of this StoreApp.


        :param install_count: The install_count of this StoreApp.  # noqa: E501
        :type: int
        """

        self._install_count = install_count

    @property
    def install_status(self):
        """Gets the install_status of this StoreApp.  # noqa: E501


        :return: The install_status of this StoreApp.  # noqa: E501
        :rtype: bool
        """
        return self._install_status

    @install_status.setter
    def install_status(self, install_status):
        """Sets the install_status of this StoreApp.


        :param install_status: The install_status of this StoreApp.  # noqa: E501
        :type: bool
        """

        self._install_status = install_status

    @property
    def introduction(self):
        """Gets the introduction of this StoreApp.  # noqa: E501


        :return: The introduction of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._introduction

    @introduction.setter
    def introduction(self, introduction):
        """Sets the introduction of this StoreApp.


        :param introduction: The introduction of this StoreApp.  # noqa: E501
        :type: str
        """

        self._introduction = introduction

    @property
    def is_official(self):
        """Gets the is_official of this StoreApp.  # noqa: E501


        :return: The is_official of this StoreApp.  # noqa: E501
        :rtype: bool
        """
        return self._is_official

    @is_official.setter
    def is_official(self, is_official):
        """Sets the is_official of this StoreApp.


        :param is_official: The is_official of this StoreApp.  # noqa: E501
        :type: bool
        """

        self._is_official = is_official

    @property
    def joint_cloud_id(self):
        """Gets the joint_cloud_id of this StoreApp.  # noqa: E501


        :return: The joint_cloud_id of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._joint_cloud_id

    @joint_cloud_id.setter
    def joint_cloud_id(self, joint_cloud_id):
        """Sets the joint_cloud_id of this StoreApp.


        :param joint_cloud_id: The joint_cloud_id of this StoreApp.  # noqa: E501
        :type: str
        """

        self._joint_cloud_id = joint_cloud_id

    @property
    def logo(self):
        """Gets the logo of this StoreApp.  # noqa: E501


        :return: The logo of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this StoreApp.


        :param logo: The logo of this StoreApp.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def name(self):
        """Gets the name of this StoreApp.  # noqa: E501


        :return: The name of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoreApp.


        :param name: The name of this StoreApp.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pic(self):
        """Gets the pic of this StoreApp.  # noqa: E501


        :return: The pic of this StoreApp.  # noqa: E501
        :rtype: list[str]
        """
        return self._pic

    @pic.setter
    def pic(self, pic):
        """Sets the pic of this StoreApp.


        :param pic: The pic of this StoreApp.  # noqa: E501
        :type: list[str]
        """

        self._pic = pic

    @property
    def price(self):
        """Gets the price of this StoreApp.  # noqa: E501


        :return: The price of this StoreApp.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this StoreApp.


        :param price: The price of this StoreApp.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def publish_type(self):
        """Gets the publish_type of this StoreApp.  # noqa: E501


        :return: The publish_type of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._publish_type

    @publish_type.setter
    def publish_type(self, publish_type):
        """Sets the publish_type of this StoreApp.


        :param publish_type: The publish_type of this StoreApp.  # noqa: E501
        :type: str
        """

        self._publish_type = publish_type

    @property
    def show_count(self):
        """Gets the show_count of this StoreApp.  # noqa: E501


        :return: The show_count of this StoreApp.  # noqa: E501
        :rtype: int
        """
        return self._show_count

    @show_count.setter
    def show_count(self, show_count):
        """Sets the show_count of this StoreApp.


        :param show_count: The show_count of this StoreApp.  # noqa: E501
        :type: int
        """

        self._show_count = show_count

    @property
    def start_count(self):
        """Gets the start_count of this StoreApp.  # noqa: E501


        :return: The start_count of this StoreApp.  # noqa: E501
        :rtype: int
        """
        return self._start_count

    @start_count.setter
    def start_count(self, start_count):
        """Sets the start_count of this StoreApp.


        :param start_count: The start_count of this StoreApp.  # noqa: E501
        :type: int
        """

        self._start_count = start_count

    @property
    def status(self):
        """Gets the status of this StoreApp.  # noqa: E501


        :return: The status of this StoreApp.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StoreApp.


        :param status: The status of this StoreApp.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update_time(self):
        """Gets the update_time of this StoreApp.  # noqa: E501


        :return: The update_time of this StoreApp.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this StoreApp.


        :param update_time: The update_time of this StoreApp.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

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
        if issubclass(StoreApp, dict):
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
        if not isinstance(other, StoreApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

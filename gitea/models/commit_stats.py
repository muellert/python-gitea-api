# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.22.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CommitStats(object):
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
        'additions': 'int',
        'deletions': 'int',
        'total': 'int'
    }

    attribute_map = {
        'additions': 'additions',
        'deletions': 'deletions',
        'total': 'total'
    }

    def __init__(self, additions=None, deletions=None, total=None):  # noqa: E501
        """CommitStats - a model defined in Swagger"""  # noqa: E501
        self._additions = None
        self._deletions = None
        self._total = None
        self.discriminator = None
        if additions is not None:
            self.additions = additions
        if deletions is not None:
            self.deletions = deletions
        if total is not None:
            self.total = total

    @property
    def additions(self):
        """Gets the additions of this CommitStats.  # noqa: E501


        :return: The additions of this CommitStats.  # noqa: E501
        :rtype: int
        """
        return self._additions

    @additions.setter
    def additions(self, additions):
        """Sets the additions of this CommitStats.


        :param additions: The additions of this CommitStats.  # noqa: E501
        :type: int
        """

        self._additions = additions

    @property
    def deletions(self):
        """Gets the deletions of this CommitStats.  # noqa: E501


        :return: The deletions of this CommitStats.  # noqa: E501
        :rtype: int
        """
        return self._deletions

    @deletions.setter
    def deletions(self, deletions):
        """Sets the deletions of this CommitStats.


        :param deletions: The deletions of this CommitStats.  # noqa: E501
        :type: int
        """

        self._deletions = deletions

    @property
    def total(self):
        """Gets the total of this CommitStats.  # noqa: E501


        :return: The total of this CommitStats.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CommitStats.


        :param total: The total of this CommitStats.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(CommitStats, dict):
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
        if not isinstance(other, CommitStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

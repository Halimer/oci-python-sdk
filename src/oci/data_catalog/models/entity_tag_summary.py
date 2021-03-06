# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityTagSummary(object):
    """
    Summary of an entity tag.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityTagSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_key:
            The value to assign to the entity_key property of this EntityTagSummary.
        :type entity_key: str

        :param key:
            The value to assign to the key property of this EntityTagSummary.
        :type key: str

        :param time_created:
            The value to assign to the time_created property of this EntityTagSummary.
        :type time_created: datetime

        :param name:
            The value to assign to the name property of this EntityTagSummary.
        :type name: str

        :param uri:
            The value to assign to the uri property of this EntityTagSummary.
        :type uri: str

        :param term_key:
            The value to assign to the term_key property of this EntityTagSummary.
        :type term_key: str

        :param term_path:
            The value to assign to the term_path property of this EntityTagSummary.
        :type term_path: str

        :param term_description:
            The value to assign to the term_description property of this EntityTagSummary.
        :type term_description: str

        :param glossary_key:
            The value to assign to the glossary_key property of this EntityTagSummary.
        :type glossary_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EntityTagSummary.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'entity_key': 'str',
            'key': 'str',
            'time_created': 'datetime',
            'name': 'str',
            'uri': 'str',
            'term_key': 'str',
            'term_path': 'str',
            'term_description': 'str',
            'glossary_key': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'entity_key': 'entityKey',
            'key': 'key',
            'time_created': 'timeCreated',
            'name': 'name',
            'uri': 'uri',
            'term_key': 'termKey',
            'term_path': 'termPath',
            'term_description': 'termDescription',
            'glossary_key': 'glossaryKey',
            'lifecycle_state': 'lifecycleState'
        }

        self._entity_key = None
        self._key = None
        self._time_created = None
        self._name = None
        self._uri = None
        self._term_key = None
        self._term_path = None
        self._term_description = None
        self._glossary_key = None
        self._lifecycle_state = None

    @property
    def entity_key(self):
        """
        Gets the entity_key of this EntityTagSummary.
        The unique key of the parent entity.


        :return: The entity_key of this EntityTagSummary.
        :rtype: str
        """
        return self._entity_key

    @entity_key.setter
    def entity_key(self, entity_key):
        """
        Sets the entity_key of this EntityTagSummary.
        The unique key of the parent entity.


        :param entity_key: The entity_key of this EntityTagSummary.
        :type: str
        """
        self._entity_key = entity_key

    @property
    def key(self):
        """
        **[Required]** Gets the key of this EntityTagSummary.
        Unique tag key that is immutable.


        :return: The key of this EntityTagSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this EntityTagSummary.
        Unique tag key that is immutable.


        :param key: The key of this EntityTagSummary.
        :type: str
        """
        self._key = key

    @property
    def time_created(self):
        """
        Gets the time_created of this EntityTagSummary.
        The date and time the tag was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this EntityTagSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EntityTagSummary.
        The date and time the tag was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this EntityTagSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def name(self):
        """
        Gets the name of this EntityTagSummary.
        Name of the tag that matches the term name.


        :return: The name of this EntityTagSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EntityTagSummary.
        Name of the tag that matches the term name.


        :param name: The name of this EntityTagSummary.
        :type: str
        """
        self._name = name

    @property
    def uri(self):
        """
        Gets the uri of this EntityTagSummary.
        URI to the tag instance in the API.


        :return: The uri of this EntityTagSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this EntityTagSummary.
        URI to the tag instance in the API.


        :param uri: The uri of this EntityTagSummary.
        :type: str
        """
        self._uri = uri

    @property
    def term_key(self):
        """
        Gets the term_key of this EntityTagSummary.
        Unique key of the related term.


        :return: The term_key of this EntityTagSummary.
        :rtype: str
        """
        return self._term_key

    @term_key.setter
    def term_key(self, term_key):
        """
        Sets the term_key of this EntityTagSummary.
        Unique key of the related term.


        :param term_key: The term_key of this EntityTagSummary.
        :type: str
        """
        self._term_key = term_key

    @property
    def term_path(self):
        """
        Gets the term_path of this EntityTagSummary.
        Path of the related term.


        :return: The term_path of this EntityTagSummary.
        :rtype: str
        """
        return self._term_path

    @term_path.setter
    def term_path(self, term_path):
        """
        Sets the term_path of this EntityTagSummary.
        Path of the related term.


        :param term_path: The term_path of this EntityTagSummary.
        :type: str
        """
        self._term_path = term_path

    @property
    def term_description(self):
        """
        Gets the term_description of this EntityTagSummary.
        Description of the related term.


        :return: The term_description of this EntityTagSummary.
        :rtype: str
        """
        return self._term_description

    @term_description.setter
    def term_description(self, term_description):
        """
        Sets the term_description of this EntityTagSummary.
        Description of the related term.


        :param term_description: The term_description of this EntityTagSummary.
        :type: str
        """
        self._term_description = term_description

    @property
    def glossary_key(self):
        """
        Gets the glossary_key of this EntityTagSummary.
        Unique id of the parent glossary of the term.


        :return: The glossary_key of this EntityTagSummary.
        :rtype: str
        """
        return self._glossary_key

    @glossary_key.setter
    def glossary_key(self, glossary_key):
        """
        Sets the glossary_key of this EntityTagSummary.
        Unique id of the parent glossary of the term.


        :param glossary_key: The glossary_key of this EntityTagSummary.
        :type: str
        """
        self._glossary_key = glossary_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this EntityTagSummary.
        State of the Tag.


        :return: The lifecycle_state of this EntityTagSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EntityTagSummary.
        State of the Tag.


        :param lifecycle_state: The lifecycle_state of this EntityTagSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

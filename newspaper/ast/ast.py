import inspect
import logging

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    pass

class Field(object):
    def __init__(self, *args, **kwargs):
        self.options = args

        if 'nested' in kwargs:
            self.nested = kwargs['nested']
        else:
            self.nested = False

        if 'null' in kwargs:
            self.null = kwargs['null']
        else:
            self.null = False

        if 'default' in kwargs:
            self.default = kwargs['default']
        else:
            self.default = None


    def assign(self, value, *args, **kwargs):
        allowed = False

        value = value or self.default

        if value is None:
            allowed = self.null

        if self.nested and 'type' in kwargs:
            if isinstance(value, kwargs['type']):
                allowed = True

        if not allowed:
            for option in self.options:
                if inspect.isclass(option) and isinstance(value, option):
                    allowed = True
                    break
                elif not inspect.isclass(option) and value == option:
                    allowed = True
                    break

        if not allowed:
            allowed = ", ".join([str(opt) for opt in self.options])
            raise ValidationError("Expecting one of ({}) but got {}".
                                  format(allowed, value))

        return value

class List(Field):
    def __init__(self, *args, **kwargs):
        super(List, self).__init__(*args, **kwargs)

    def assign(self, values, *args, **kwargs):
        logger.info(values)
        for value in values:
            super(List, self).assign(value, *args, **kwargs)

        return values

class NodeMeta(type):
    def __init__(cls, name, parents, dct):
        # create a class_id if it's not specified
        if 'class_id' not in dct:
            dct['class_id'] = name.lower()

        if '_name' not in dct:
            cls._name = name


        fields = dict()

        for parent in parents:
            if getattr(parent, '_fields', None) is not None:
                fields.update(dict(parent._fields))

        fields.update({name: field for name, field in dct.iteritems()
                       if isinstance(field, Field)})

        cls._fields = fields.items()

        # we need to call type.__init__ to complete the initialization
        return super(NodeMeta, cls).__init__(name, parents, dct)


class Node(object):
    __metaclass__ = NodeMeta

    def __init__(self, *args, **kwargs):
        fields = self.__class__._fields

        values = list(args)

        for name, field in fields:
            if name in kwargs:
                value = kwargs[name]
            elif len(values) > 0:
                value = values.pop(0)
            else:
                value = None

            setattr(self, name, field.assign(value, type=self.__class__))

    def __str__(self):
        names = [name for name, field in self.__class__._fields]
        values = []
        for name in names:
            value = getattr(self, name, None)
            if isinstance(value, list):
                value = [str(item) for item in value]
            values = values + [value]


        attrs = " ".join(["{}={}".format(name, value) for name, value in
                          zip(names, values)])\
                   .strip()
        desc = "{} {}".format(self.__class__.__name__, attrs)\
                         .strip()
        return "({})".format(desc)

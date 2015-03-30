from nose.tools import *
from unittest import TestCase
import logging

from newspaper.ast.ast import Node, Field, List, ValidationError

logger = logging.getLogger(__name__)

class NodeTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_field(self):
        field = Field("foo", "bar", "baz")

        value = field.assign("foo")
        self.assertEquals(value, "foo")

        with self.assertRaises(ValidationError):
            value = field.assign("qux")

    def test_nested_field(self):
        class NestedFoo(Node):
            foo = Field("foo", nested=True)

        foo = NestedFoo(NestedFoo("foo"))
        self.assertEquals(foo.foo.foo, "foo")


    def test_node_initialization(self):
        class AlignedNode(Node):
            align = Field("left", "right", "none")

        n = AlignedNode("left")
        self.assertEquals(n.align, "left")

    def test_node_str(self):
        class AlignedNode(Node):
            _name = 'AlignedNode'

            align = Field("left", "right", "none")

        n = AlignedNode("left")
        self.assertEquals(str(n), "(AlignedNode align=left)")

    def test_node_invalid_assignment(self):
        class AlignedNode(Node):
            align = Field("left", "right", "none")

        with self.assertRaises(ValidationError):
            n = AlignedNode("fnord")

    def test_node_named_assignment(self):
        class N(Node):
            first = Field(int)
            second = Field(int)

        n1 = N(5, second=3)
        self.assertEquals(n1.first, 5)
        self.assertEquals(n1.second, 3)

        n2 = N(3, first=5)
        self.assertEquals(n1.first, 5)
        self.assertEquals(n1.second, 3)

    def test_null_field(self):
        class N(Node):
            not_null = Field(int, null=False)
            null = Field(int, null=True)

        n1 = N(not_null=5, null=None)
        self.assertEquals(n1.null, None)

        with self.assertRaises(ValidationError):
            n2 = N(not_null=None, null=5)

    def test_list(self):
        class N(Node):
            ints = List(int)

        n = N([1,2,3])
        self.assertEquals(len(n.ints), 3)

    def test_default(self):
        class N(Node):
            i = Field(int, default=5)

        n = N()
        self.assertEquals(n.i, 5)

from utils import *


import Cell
from template import Template

class Templates:
    @classmethod
    def template1(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]
    
    @classmethod
    def template2(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template3(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Floor, Cell.Floor],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Floor, Cell.Floor],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template4(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template5(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template6(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Floor, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template7(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template8(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Floor, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Floor, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template9(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Floor, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Wall, Cell.Null],
        [Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Floor, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template10(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Floor, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Floor],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template11(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template12(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor],
        [Cell.Null, Cell.Floor, Cell.Wall, Cell.Floor, Cell.Floor],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]
    @classmethod
    def template13(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template14(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Floor, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Floor, Cell.Floor, Cell.Null, Cell.Null, Cell.Null],

        ]

    @classmethod
    def template15(cls):
        return [
        [Cell.Null, Cell.Floor, Cell.Null, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Floor, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Null, Cell.Floor, Cell.Null],

        ]

    @classmethod
    def template16(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],

        ]

    @classmethod
    def template17(cls):
        return [
        [Cell.Null, Cell.Null, Cell.Null, Cell.Null, Cell.Null],
        [Cell.Null, Cell.Wall, Cell.Wall, Cell.Wall, Cell.Null],
        [Cell.Floor, Cell.Floor, Cell.Wall, Cell.Floor, Cell.Floor],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Floor, Cell.Null],
        [Cell.Null, Cell.Floor, Cell.Floor, Cell.Null, Cell.Null],

        ]

    @classmethod
    def templates(cls):
        return [
        cls.template1,
        cls.template2,
        cls.template3,
        cls.template4,
        cls.template5,
        cls.template6,
        cls.template7,
        cls.template8,
        cls.template9,
        cls.template10,
        cls.template11,
        cls.template12,
        cls.template13,
        cls.template14,
        cls.template15,
        cls.template16,
        cls.template17,

        ]

    @classmethod
    def getRandom(cls):
      r = Random()
      randTemplate = cls.templates[r.Next(len(cls.templates))]
      return Template(randTemplate)


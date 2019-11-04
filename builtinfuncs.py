class MathFunctions():

    @staticmethod
    def abs_test():
        assert(abs(10) == 10)
        assert(abs(-10) == 10)
        assert(abs(1.5) == 1.5)
        assert(-1.5 - abs(1.5) < 0.00001)

    @staticmethod
    def divmod_test():
        a = 84
        b = 14
        assert divmod(a, b) == (6, 0)

        a = 84
        b = 15
        assert divmod(a, b) == (5, 9)

        a = -4
        b = 15
        assert divmod(a, b) == (-1, 11)

    @staticmethod
    def pow_test():
        assert pow(2, 4) == 16
        assert pow(2, -2) - (1/4) < .0001
        assert pow(2, 5, 14) == 4

    @staticmethod
    def round_test():
        assert round(1.9) == 2
        assert round(1.99, 1) == 2
        assert round(0.5) == 0
        assert round(-0.5) == 0
        assert round(-0.6) == -1

        assert round(-0.5, 1) - -0.5 < .00001

class FxnsOnIterables():
    def all_test():
        all_true = [1, True, 1.5, 'a']
        assert(all(all_true) == True)
        one_true = [1, True, 0, 1.5, 'a']
        assert(all(one_true) == False)
        assert(any(one_true) == True)
        all_false = [0, False, '', None]
        assert(any(all_false) == False)

    def len_test():
        emp_a = []
        assert len(emp_a) == 0
        emp_d = {}
        assert len(emp_d) == 0
        emp_s = ''
        assert len(emp_s) == 0

        a = [2, 3, 5, [2, 3]]
        assert len(a) == 4
        s = 'qewr'
        assert len(s) == 4
        d = {'foo': 'bar', 'ping': 'pong'}
        assert len(d) == 2

    def iter_test():
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        b = [e for e in iter(a)]
        assert len(b) == 9

        ia = iter(a)
        b = [e for e in iter(ia.__next__ , 5)]
        assert len(b) == 4

    def reversed_test():
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        b = [e for e in reversed(a)]
        assert len(b) == 10
        assert b == [10,9,8,7,6,5,4,3,2,1]

        ia = reversed(a)
        b = [e for e in iter(ia.__next__ , 5)]
        assert len(b) == 5

    def max_test():
        a = [1, 5, 7, 32, 76, 8]
        assert max(a) == 76
        assert max(5, 8, -1) == 8

    def min_test():
        a = [1, 5, 7, -6, 32, 76, 8]
        assert min(a) == -6
        assert min(5, 8, -1, 4) == -1

    def sorted_test():
        a = [1, 5, 7, -6, 32, 76, 8]
        assert sorted(a) == [-6, 1, 5, 7, 8, 32, 76]
        assert sorted(a, reverse=True) == [76,32,8,7,5,1,-6]
        assert sorted(a, key=abs) == [1,5,-6,7,8,32,76]

    def sum_test():
        a = [1, 5, 7, -6, 32, 76, 8]
        assert sum(a) == 123
        assert sum(a, -3) == 120

    def filter_test():
        a = [1, 5, 7, -6, 32, 76, 8]
        assert list(filter(lambda x: x > 10, a)) == [32, 76]

    def map_test():
        a = [1, 5, 7, -6, 32, 76, 8]
        assert list(map(lambda x: pow(x, 2), a)) == [1, 25, 49, 36, 1024, 5776, 64]

    def zip_test():
        a = [1, 5, 7, -6, 32, 76, 8]
        b = [43,1,76,230, 54,  1]
        c = [ 9,-3,4,190, 5,   7, 2]
        assert list(zip(a,b,c)) == [(1,43,9), (5,1,-3), (7,76,4), (-6,230,190), (32, 54, 5), (76,1,7)]

        pred = lambda x: x > 60
        assert list(filter(pred, map(sum, zip(a,b,c)))) == [87, 414, 91, 84]

class TypeConversions():
    def bin_test():
        assert(bin(3) == '0b11')
        assert(bin(-3) == '-0b11')

    def hex_test():
        assert(hex(255) == '0xff')
        assert(hex(-255) == '-0xff')

    def oct_test():
        assert(oct(8)) == '0o10'
        assert(oct(-58)) == '-0o72'

    def bool_test():
        class A:
            a = 4

            def a(self):
                return self.a

        assert bool(1) == True
        assert bool(1.5) == True
        assert bool(' ') == True
        assert bool('a') == True
        assert bool([0]) == True
        assert bool({'None': 0}) == True
        assert bool(A()) == True

        assert bool(0) == False
        assert bool('') == False
        assert bool([]) == False
        assert bool({}) == False

    def chr_test():
        pass

    def complex_test():
        pass

    def float_test():
        pass

    def int_test():
        assert int() == 0
        assert int(1.6) == 1
        assert int(-1.6) == -1
        assert int('1') == 1
        # assert int('1.6') == 1 Error
        assert int('-5') == -5
        assert int('FF', base=16) == 255
        assert int(0xFF) == 255
        assert int(0b100) == 4

    def ord_test():
        pass

    def str_test():
        pass

    def type_test():
        pass
    
def ascii_test():
    pass

def bytearray_test():
    pass

def bytes_test():
    pass

MathFunctions.abs_test()
MathFunctions.divmod_test()
MathFunctions.pow_test()
MathFunctions.round_test()

FxnsOnIterables.all_test()
FxnsOnIterables.len_test()
FxnsOnIterables.iter_test()
FxnsOnIterables.max_test()
FxnsOnIterables.min_test()
FxnsOnIterables.reversed_test()
# FxnsOnIterables.slice_test()
FxnsOnIterables.sorted_test()
FxnsOnIterables.sum_test()
FxnsOnIterables.filter_test()
FxnsOnIterables.map_test()
FxnsOnIterables.zip_test()

TypeConversions.bin_test()
TypeConversions.hex_test()
TypeConversions.oct_test()
TypeConversions.bool_test()
TypeConversions.chr_test()
TypeConversions.complex_test()
TypeConversions.float_test()
TypeConversions.int_test()
TypeConversions.ord_test()
TypeConversions.str_test()
TypeConversions.type_test()
'''
callable_test()
hash_test()
id_test()
isinstance_test()
issubclass_test()
super_test()
ascii_test()
repr_test()
vars_test()

bytearray_test()
bytes_test()
dict_test()
frozenset_test()
list_test()
object_test()
range_test()
set_test()
tuple_test()

classmethod_test()
staticmethod_test()

compile_test()

delattr_test()
getattr_test()
hasattr_test()
setattr_test()
property_test()

enumerate_test()
eval_test()
exec_test()
format_test()

globals_test()
locals_test()

input_test()
print_test()

memoryview_test()

dir_test()
open_test()
'''
import sys
import unittest

sys.path.append(".")

from data_printer import p, np
import io
from colored import fore, back, style


class A:
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)


r = [20, (2, 0.01, False, True, None)]
a = A(x=dict(p=10, r=r), f=lambda x: x)
b = A(abc="acc", a=a, s='Строка\n', b=b'binary\n', r=r, rs=r'\n', delegate=a.__init__)
r.append( b )


class DdpTestCase(unittest.TestCase):

    def test_object(self):
        Int = type("Int", (int,), {})
        self.assertEqual(np(Int(3)), "Int(3)\n")

        Float = type("Float", (float,), {})
        self.assertEqual(np(Float(-3.3)), "Float(-3.3)\n")

        Str = type("Str", (str,), {})
        self.assertEqual(np(Str("x")), "Str('x')\n")


    def test_uncolor_string(self):
         
        s=np(b)
        
        self.assertTrue('10' in s, 'Распечатано число 10')
        self.assertTrue("'Строка\\n'" in s, 'Распечатана строка')
        self.assertTrue("b'binary\\n'" in s, 'Распечатано бинари')
        
        f = io.StringIO('')
        p(b, file=f, color=False)
        
        self.assertEqual(f.getvalue(), s, "Cтроки совпадают")
        f.close()
        

    def test_default_colors(self):

        s=np(b, color=True)

        self.assertTrue('10' in s, 'Распечатано число 10')
        self.assertTrue("'Строка\\n'" in s, 'Распечатана строка')
        self.assertTrue("b'binary\\n'" in s, 'Распечатано бинари')
        
        f = io.StringIO('')
        p(b, file=f)
        
        self.assertEqual(f.getvalue(), s, "Колоризированные строки совпадают")
        f.close()
        
    def test_colors(self):
        
        color=dict(
            int=fore.RED,
            float=fore.GREEN
        )
        
        s=np(b, color=True)

        self.assertTrue('10' in s, 'Распечатано число 10')
        self.assertTrue("'Строка\\n'" in s, 'Распечатана строка')
        self.assertTrue("b'binary\\n'" in s, 'Распечатано бинари')
        
        f = io.StringIO('')
        p(b, file=f)
        
        self.assertEqual(f.getvalue(), s, "Колоризированные строки совпадают")
        f.close()
        
        x=False
        try:
            p('', color={'x': 1})
        except KeyError:
            x = True
        self.assertTrue(x, "Нет ключа")
        
    def test_object_without_dict(self):
        from datetime import datetime
        s=np(datetime.strptime('09.07.2006 00:23:23', '%d.%m.%Y %H:%M:%S'))
        self.assertEqual(s, "datetime('2006-07-09 00:23:23')\n", 'Распечатан объект без словаря')


if __name__ == '__main__':
    unittest.main()


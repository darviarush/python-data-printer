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
            


if __name__ == '__main__':
    unittest.main()


from lark import Lark, Transformer
import json

class ToJSON(Transformer):

    def start(self, items):
        return dict(items)
    
    def dict(self, items):
        return dict(items)

    def pair(self, p):
        k, v = p
        return k, v

    def number(self, n):
        (n,) = n
        return float(n)

    def string(self, s):
        (s,) = s
        return s[0:] 
   
    def estring(self, s):
        (s,) = s
        return s[1:-1] 

if __name__ == "__main__":
    with open('input.txt') as f:
        ast = Lark.open('grammar.lark').parse(f.read())
        print(ast.pretty())

    output =ToJSON().transform(ast) 
    print(json.dumps(output))
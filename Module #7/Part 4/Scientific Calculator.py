import math

class Calculator:
    @staticmethod
    def add(a, b): return a + b
    @staticmethod
    def sub(a, b): return a - b
    @staticmethod
    def mul(a, b): return a * b
    @staticmethod
    def div(a, b): return a / b if b != 0 else float('nan')
    
    @staticmethod
    def sin(x): return math.sin(math.radians(x))
    @staticmethod
    def cos(x): return math.cos(math.radians(x))
    @staticmethod
    def tan(x): return math.tan(math.radians(x))
    
    @staticmethod
    def log(x): return math.log10(x)
    @staticmethod
    def ln(x): return math.log(x)
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        conversions = {
            'cm': {'in': 0.393701, 'm': 0.01},
            'in': {'cm': 2.54, 'm': 0.0254},
            'm': {'cm': 100, 'in': 39.3701}
        }
        return value * conversions[from_unit][to_unit]

def main():
    calc = Calculator()
    print("Scientific Calculator\n")
    
    while True:
        print("1. Basic Math\n2. Trig Functions\n3. Conversions\n4. Exit")
        mode = input("Select mode: ")
        
        if mode == '1':
            a = float(input("First number: "))
            op = input("Operation (+-*/): ")
            b = float(input("Second number: "))
            
            if op == '+': res = calc.add(a, b)
            elif op == '-': res = calc.sub(a, b)
            elif op == '*': res = calc.mul(a, b)
            elif op == '/': res = calc.div(a, b)
            print(f"Result: {res}")
            
        elif mode == '2':
            func = input("Function (sin/cos/tan/log/ln): ")
            x = float(input("Value: "))
            if func == 'sin': res = calc.sin(x)
            elif func == 'cos': res = calc.cos(x)
            elif func == 'tan': res = calc.tan(x)
            elif func == 'log': res = calc.log(x)
            elif func == 'ln': res = calc.ln(x)
            print(f"Result: {res}")
            
        elif mode == '3':
            value = float(input("Value: "))
            from_unit = input("From unit (cm/in/m): ")
            to_unit = input("To unit (cm/in/m): ")
            res = calc.convert(value, from_unit, to_unit)
            print(f"Result: {res} {to_unit}")
            
        elif mode == '4':
            break

if __name__ == "__main__":
    main()

import sys
def leng(integer):
    return len(str(integer))

sys.set_int_max_str_digits(10000)

class BigNum():
    def __init__(self, MantiInt = 0, MantiDec = "0", Expo = 0, Prec = 10, negative_flag = 1):
        while abs(MantiInt) >= 10:
            MantiDec = f"{MantiInt%10}{MantiDec}"
            MantiInt //= 10
            Expo += 1

        if not Expo == 0 and MantiInt == 0:
            while MantiInt == 0:
                MantiInt = int(MantiDec[0])
                MantiDec = MantiDec[1:]
                Expo -= 1

        self.Exponent = Expo
        self.Mantissa_Integer = MantiInt * negative_flag
        self.Mantissa_Decimal = MantiDec
        self.Mantissa_Decimal_Len = leng(self.Mantissa_Decimal)
        self.Precision = Prec

        if self.Mantissa_Decimal_Len > self.Precision:
            self.Mantissa_Decimal = self.Mantissa_Decimal[:self.Precision]
            self.Mantissa_Decimal_Len = leng(self.Mantissa_Decimal)

    def Num(string = "0.0E0", Prec = 10):
        negative = 1

        string = str(string)

        if string[0] == "-":
            negative = -1
            string = string[1:]

        string = string.lower()

        if string.find("e") == -1:
            string = f"{string}e0"

        if string.find(".") == -1:
            string = f"{string[:string.find('e')]}.{string[string.find('e'):]}"

        point = string.find(".")
        if string.count(".") > 1:
            string = string.replace(".", "")
            string = string[:point] + "." + string[point:]
        Mantissa_Integer = int(string[:point])
        E = string.find("e")
        if string.count("e") > 1:
            string = string.replace("e", "")
            string = string[:E] + "e" + string[E:]
        Mantissa_Decimal = string[point+1:E]
        Exponent = int(string[E+1:])

        return BigNum(Mantissa_Integer, Mantissa_Decimal, Exponent, Prec, negative)

    def PrintNum(self):
        print(BigNum.CTS(self))

    def CTS(self):
        mantissa_string = ""
        for i in range(self.Mantissa_Decimal_Len - leng(self.Mantissa_Decimal)):
            mantissa_string += "0"
        mantissa_string += str(self.Mantissa_Decimal)
        if not mantissa_string == "":
            return f"{self.Mantissa_Integer}.{mantissa_string}E{self.Exponent}"
        else:
            return f"{self.Mantissa_Integer}E{self.Exponent}"

    def Add(Num1, Num2):
        low_exp = min(Num1.Exponent, Num2.Exponent)

        while Num1.Exponent > low_exp:
            Num1.Exponent -= 1
            if Num1.Mantissa_Decimal == "":
                Num1.Mantissa_Decimal += "0"
            Num1.Mantissa_Integer = int(f"{Num1.Mantissa_Integer}{Num1.Mantissa_Decimal[0]}")
            Num1.Mantissa_Decimal = Num1.Mantissa_Decimal[1:]

        while Num2.Exponent > low_exp:
            Num2.Exponent -= 1
            if Num2.Mantissa_Decimal == "":
                Num2.Mantissa_Decimal += "0"
            Num2.Mantissa_Integer = int(f"{Num2.Mantissa_Integer}{Num2.Mantissa_Decimal[0]}")
            Num2.Mantissa_Decimal = Num2.Mantissa_Decimal[1:]


        ResPrec = min(Num1.Precision, Num2.Precision)
        ResInt = Num1.Mantissa_Integer + Num2.Mantissa_Integer

        return BigNum(ResInt, "0", low_exp, ResPrec)


    def Mult(Num1, Num2):

        match Num1.Mantissa_Integer or Num2.Mantissa_Integer:

            ResIntDec = int(str(Num1.Mantissa_Integer)+str(Num1.Mantissa_Decimal)) * int(str(Num2.Mantissa_Integer)+str(Num2.Mantissa_Decimal))
            print(ResIntDec)
            DecPoint = leng(ResIntDec) - (leng(Num1.Mantissa_Decimal) + leng(Num2.Mantissa_Decimal))
            print(DecPoint)
            ResInt = int(str(ResIntDec)[:DecPoint])
            ResDec=  int(str(ResIntDec)[DecPoint:])
            ResExpo = Num1.Exponent + Num2.Exponent
            print("c ca que tu cherche",ResInt, ResDec, ResExpo, ResIntDec)
            return BigNum(ResInt, ResDec, ResExpo)


def printnum(*num):
    for i in num:
        BigNum.PrintNum(i)

def add(*nums):
    res = BigNum()
    for num in nums:
        res = BigNum.Add(res, num)
    return res

def mult(*nums):
    Res = BigNum.Num("1.0")
    for num in nums:
        Res = BigNum.Mult(Res, num)
    return Res


a = BigNum.Num("1")
b = BigNum.Num("5")

print("Façon chiante:")
printnum(BigNum.Mult(a,b))
print("Façon rapide:")
printnum(mult(a,b))

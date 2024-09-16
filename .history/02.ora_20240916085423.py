import statistics

def median(lista):
    hossz = len(lista)
    rendezett = sorted(lista)
    if (hossz % 2 == 1):
        return rendezett(hossz//2)
    else:
         x1 = rendezett[hossz//2]
         x2 = rendezett(hossz//2+1)
         x3 = (x1 + x2)/2

         return round(x3, 1)

def median(lista):
    return statistics.median(lista)
 
 # --------------------------------------------------------

 def jegykulonbseg(num1, num2):
    
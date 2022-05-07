class Solution:
    def intToRoman(self, num: int) -> str:
    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
        ROM = ''
        SYMBOL={1000:'M',
                500:'D',
                100:'C',
                50:'L',
                10:'X',
                5:'V',
                1:'I'}

        STEP = list(SYMBOL.keys())
        STEP.reverse()
        #separate the digits:
        ones = num%10 # 1<= ones <=9
        tens = (num - ones)%100 #11<=tens<=99
        hnds = (num - ones - tens)%1000 #100<=hnds<=999
        thnds = num - ones - tens -hnds #1000<=thnds<=3999
        SPLIT = {1:ones,
                 10:tens,
                 100:hnds,
                 1000:thnds}
        #print("ones=",ones,"tens=",tens,"hnds=",hnds,"thnds=",thnds)
        r1 = ''
        r2 = ''
        r3 = ''
        r4 = ''
        if ones == 4:
            r1 = 'IV'
        elif ones ==9:
            r1 = 'IX'
        else:
            r1 = (ones//5)*'V'+(ones - 5*(ones//5))*'I'

        if tens == 40:
            r2 = 'XL'
        elif tens ==90:
            r2 = 'XC'
        else:
            r2 = (tens//50)*'L' + ((tens - 50*(tens//50)))//10*'X'

        if hnds == 400:
            r3 = 'CD'
        elif hnds == 900:
            r3 = 'CM'
        else:
            r3 = (hnds//500)*'D'+((hnds - 500*(hnds//500)))//100*'C'

        r4=(thnds//1000)*'M'
        result = r4+r3+r2+r1
        return result 
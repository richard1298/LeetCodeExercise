class Solution:
    def intToRoman(self, num: int) -> str:
        SYMBOL={1000:'M',
                900:'CM',
                500:'D',
                400:'CD',
                100:'C',
                90:'XC',
                50:'L',
                40:'XL',
                10:'X',
                9:'IX',
                5:'V',
                4:'IV',
                1:'I'}
        result = ''
        KEYS = list(SYMBOL.keys())
        for i in KEYS:
            quo = num//i
            rem = num%i
            result = result + quo*SYMBOL[i]
            num = num - quo*i
        return result
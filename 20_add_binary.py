class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry_over = 0
        response = ""
        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord("0") if i < len(a) else 0

            digit_b = ord(b[i]) - ord("0") if i < len(b) else 0

            total_sum = (int(digit_a)+int(digit_b)+carry_over)
            char_sum = str(total_sum % 2)
            response = char_sum + response
            carry_over = (total_sum) // 2
        if carry_over:
            response = "1" + response
        return response
            

if __name__=='__main__':
    self = Solution()
    a = "1010"
    b = "1011"
    print(self.addBinary(a=a, b=b))
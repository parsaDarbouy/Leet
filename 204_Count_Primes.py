class Solution:
    def countPrimes(self, n: int) -> int:
        list_of_numbers = range(2,n)
        length = len(list_of_numbers)
        prime = [0] * length
        count = 0
        for i in range(length):
            if prime[i] == 0:
                count += 1
                change = list_of_numbers[i]
                index = i + change
                while index < length:
                    prime[index] = 1
                    index += change
        return count

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(n):
            number = i + 1
            divisible_3 = number % 3
            divisible_5 = number % 5
            divisible_15 = number% 15
            if divisible_3 == 0 and divisible_5 == 0:
                answer.append("FizzBuzz")
            elif divisible_3 == 0:
                answer.append("Fizz")
            elif divisible_5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(number))
        return answer

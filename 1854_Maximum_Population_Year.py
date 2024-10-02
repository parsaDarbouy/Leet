class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        start = logs[0][0]
        end = logs[0][1]
        for i in logs:
            if i[0] < start:
                start = i[0]
            if i[1] > end:
                end = i[1]

        years = [0] * (end - start + 1)
        offset = start

        for i in logs:
            birth_year_w_offset = i[0] - offset
            death_year_w_offset = i[1] - offset
            years[birth_year_w_offset] += 1
            years[death_year_w_offset] -= 1

        max_population = population = 0
        max_year = 0
        for i, change in enumerate(years):
            population += change
            if population > max_population:
                max_population = population
                max_year = i
                
        return max_year + offset

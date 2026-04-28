class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Iterate through temperatures
        # for each temperature, we want to find how many days until
        # we see a warmer temperature than itself.
        # otherwise we set it to 0

        # for every temp in temperatures, we could just keep counting until we hit a temperature higher
        # than itself, so every day we add one to a count, append that count to the corresponding temp

        res = [0] * len(temperatures)
        stack = []

        # Index Value
        for i, temp in enumerate(temperatures): # want to keep temperatures in bound, we do want to keep track of index
            # Current temperature we are on, iterate through
            while stack and temp > temperatures[stack[-1]]:
                prevIndex = stack.pop()
                res[prevIndex] = i - prevIndex
            stack.append(i)
        return res

# temperatures = [30,38,30,36,35,40,28]

# push 30 to the stack
# see 38 we pop?
# append 38 to stack
# see 30 append, 
# see 36 append
# see 35 append,
# see 40, pop
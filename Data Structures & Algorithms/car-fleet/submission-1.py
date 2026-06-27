class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in cars:
            # Steps (time) needed to reach the target
            steps = (target - pos) / spd

            # Only append if stack is empty or this value is less than the top
            if not stack or steps > stack[-1]:
                stack.append(steps)

        return len(stack)

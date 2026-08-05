class Solution:
    def isValid(self, s: str) -> bool:
        # We want to make a stack with the elemrnts in the list
        # Then we want to pop off the top where is a matching entry below it
        # If there is no match, then we return False
        # If we finish and get a stack size of 0, then we return True

        stack = list()

        ptr = 0

        for i in range(0, len(s)):
            stack.append(s[i])
            ptr = len(stack)-1
            print(stack)
            # We check each char for its matching pair
            if stack[ptr] == ']':
                if stack[ptr-1] == '[':
                    stack.pop()
                    stack.pop()
                    # ptr =- 1
                else:
                    return False
            elif stack[ptr] == '}':
                if stack[ptr-1] == '{':
                    stack.pop()
                    stack.pop()
                    # ptr =- 1
                else:
                    return False
            elif stack[ptr] == ')':
                print("made it here")
                if stack[ptr-1] == '(':
                    stack.pop()
                    stack.pop()
                    # ptr =- 1
                else:
                    return False


        if len(stack) == 0:
            return True
        return False
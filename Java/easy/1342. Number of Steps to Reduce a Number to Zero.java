class Solution {
    public int numberOfSteps (int num) {
        int result = 0;
        while (num != 0) {
            if (num % 2 == 1) {
                num -= 1;
            }
            else {
                num /= 2;
            }
            result += 1;
        }
        return result;
    }
}

// bit manipulation
class Solution {
    public int numberOfSteps (int num) {
        int result = 0;
        while (num != 0) {
            if ((num & ~(num - 1)) == 1) {
                num -= 1;
            }
            else {
                num /= 2;
            }
            result += 1;
        }
        return result;
    }
}

class Solution {
    public int numberOfSteps (int num) {
        if (num == 0) {
            return 0;
        }
        else {
            return Integer.bitCount(num) + (31 - Integer.numberOfLeadingZeros(num));
        }
    }
}
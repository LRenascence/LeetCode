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
        return Integer.bitCount(num) + (31 - Integer.numberOfLeadingZeros(num));
    }
}
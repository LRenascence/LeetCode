class Solution {
    public int xorOperation(int n, int start) {
        int result = 0;
        for (int i = 0; i < n; i ++) {
            result ^= start + 2 * i;
        }
        return result;
    }
}

class Solution {
    public int xorOperation(int n, int start) {
        int result = 0;
        result = (n % 2) * (start % 2);
        
        int a = start;
        int b = start + 2 * n;
        
        a /= 2;
        b /= 2;
        
        a = ((a - 1) * (a % 2)) ^ ((a / 2) % 2);
        b = ((b - 1) * (b % 2)) ^ ((b / 2) % 2);
        
        result += (a ^ b) * 2;
        return result;
    }
}
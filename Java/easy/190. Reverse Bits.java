public class Solution {
    // you need treat n as an unsigned value
    final int precompute[] = {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15};
    
    public int reverseBits(int n) {
        int maskLength = 4;
        int mask = 0xF;
        int result = 0;
        for (int i = 0; i < 8; i++) {
            result |= (precompute[(n >> (i * maskLength)) & mask] << ((8 - i - 1) * maskLength)); 
        }
        return result;
    }
}
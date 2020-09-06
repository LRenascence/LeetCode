class Solution {
    public int[] singleNumber(int[] nums) {
        int mask = 0;
        for (int i = 0; i < nums.length; i++) {
            mask ^= nums[i];
        }
        mask = mask & ~(mask - 1);
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            if ((mask & nums[i]) == 0) {
                result[0] ^= nums[i];
            }
            else {
                result[1] ^= nums[i];
            }
        }
        return result;
    }
}
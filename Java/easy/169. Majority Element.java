class Solution {
    public int majorityElement(int[] nums) {
        int result = 0;
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            if (counter == 0) {
                result = nums[i];
            }
            counter += result == nums[i] ? 1 : -1;
        }
        return result;
    }
}
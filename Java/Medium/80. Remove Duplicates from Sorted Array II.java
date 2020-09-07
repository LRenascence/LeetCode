class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int result = 0;
        int counter = 0;
        int temp = nums[0];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == temp && counter < 2) {
                nums[result++] = nums[i];
                counter++;
            }
            else if (nums[i] != temp) {
                nums[result++] = nums[i];
                counter = 1;
                temp = nums[i];
            }
        }
        return result;
    }
}
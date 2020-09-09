class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int result1 = 0, result2 = 0, counter1 = 0, counter2 = 0;
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (result1 == nums[i]) counter1++;
            else if (result2 == nums[i]) counter2++;
            else if (counter1 == 0) {
                result1 = nums[i];
                counter1 = 1;
            }
            else if (counter2 == 0) {
                result2 = nums[i];
                counter2 = 1;
            }
            else {
                counter1--;
                counter2--;
            }
        }
        counter1 = 0;
        counter2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == result1) counter1++;
            else if(nums[i] == result2) counter2++;
        }
        if (counter1 > nums.length / 3) result.add(result1);
        if (counter2 > nums.length / 3) result.add(result2);
        return result;
    }
}
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> memory = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (memory.containsKey(nums[i])) {
                if (i - memory.get(nums[i]) <= k) return true;
            }
            memory.put(nums[i], i);
        }
        return false;
    }
}
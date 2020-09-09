class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> map = new HashSet<Integer>();
        for (int num : nums) {
            if (map.contains(num)) return true;
            map.add(num);
        }
        return false;
    }
}
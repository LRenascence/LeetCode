class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int curSum = 0;
        int total = 0;
        int result = 0;
        for (int i = 0; i < gas.length; i++) {
            curSum += gas[i] - cost[i];
            if (curSum < 0) {
                total += curSum;
                result = i + 1;
                curSum = 0;
            }
        }
        total += curSum;
        return total < 0 ? -1 : result;
    }
}
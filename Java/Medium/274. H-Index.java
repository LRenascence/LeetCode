class Solution {
    public int hIndex(int[] citations) {
        int[] memory = new int[citations.length + 1];
        for (int i = 0; i < citations.length; i++) {
            if (citations[i] >= citations.length) memory[citations.length]++;
            else memory[citations[i]]++;
        }
        int count = 0;
        for (int i = memory.length - 1; i >= 0; i--) {
            count += memory[i];
            if (count >= i) return i;
        }
        return 0;
    }
}
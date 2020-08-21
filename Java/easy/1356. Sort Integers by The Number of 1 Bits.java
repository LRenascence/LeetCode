class Solution {
    public int[] sortByBits(int[] arr) {
        int result[] = new int[arr.length];
        PriorityQueue<Integer> minheap = new PriorityQueue<>(
            new Comparator<Integer>() {
                public int compare(Integer a, Integer b) {
                    int a1 = count1s(a);
                    int b1 = count1s(b);
                    if (a1 == b1) {
                        return a - b;
                    }
                    else {
                        return a1 - b1;
                    }
                }
            });
        
        for (int i = 0; i < arr.length; i ++) {
            minheap.add(arr[i]);
        }
        int index = 0;
        while (minheap.size() > 0) {
            result[index++] = minheap.poll();
        }
        return result;
    }
    
    private int count1s(int num) {
        int count = 0;
        while (num > 0) {
            count++;
            num = num & (num - 1);
        }
        return count;
    }
}
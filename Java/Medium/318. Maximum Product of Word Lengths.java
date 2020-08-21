class Solution {
    public int maxProduct(String[] words) {
        int bitList[] = new int[words.length];
        int result = 0;
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                bitList[i] |= 1 << (words[i].charAt(j) - 'a');
            }
        }
        for (int i = 0; i < words.length; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if ((bitList[i] & bitList[j]) == 0) {
                    int temp = words[i].length() * words[j].length();
                    if (result < temp) {
                        result = temp;
                    }
                }
            }
        }
        return result;
    }
}
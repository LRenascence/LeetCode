class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack.equals("") && needle.equals("")) return 0;
        for (int i = 0; i < haystack.length(); i++) {
            boolean found = true;
            for (int j = 0; j < needle.length(); j++) {
                if (i + j >= haystack.length()){
                    return -1;
                }
                if (haystack.charAt(i + j) != needle.charAt(j)) {
                    found = false;
                    break;
                }
            }
            if (found) return i;
        }
        return -1;
    }
}
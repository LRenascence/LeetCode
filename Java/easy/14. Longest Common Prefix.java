class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < strs[0].length(); i++) {
            char curChar = strs[0].charAt(i);
            boolean match = true;
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != curChar) {
                    match = false;
                    break;
                }
            }
            if (match) {
                result.append(curChar);
            }
            else {
                break;
            }
        }
        return result.toString();
    }
}
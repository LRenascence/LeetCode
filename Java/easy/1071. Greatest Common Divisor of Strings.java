class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (str1.length() > str2.length()) {
            return gcdOfStrings(str2, str1);
        }
        if (str1.repeat(str2.length() / str1.length()).equals(str2)) {
            return str1;
        }
        for (int i = str1.length() / 2; i > 0; i--) {
            String result = str1.substring(0, i);
            if (result.repeat(str1.length() / i).equals(str1) & result.repeat(str2.length() / i).equals(str2)) {
                return result;
            } 
        }
        return "";
    }
}
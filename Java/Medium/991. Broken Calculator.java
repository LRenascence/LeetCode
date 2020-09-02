class Solution {
    public int brokenCalc(int X, int Y) {
        int result = 0;
        while (Y > X) {
            Y = (Y & 1) == 0 ? Y / 2 : Y + 1;
            result++;
        }
        return result + X - Y;
    }
}
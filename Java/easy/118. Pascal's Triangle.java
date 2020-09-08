class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        ArrayList<Integer> newRow = new ArrayList<Integer>();
        for(int i = 0; i < numRows; i++)
        {
            newRow.add(0, 1);
            for(int j = 1;j < newRow.size() - 1; j++)
                newRow.set(j, newRow.get(j) + newRow.get(j+1));
            result.add(new ArrayList<Integer>(newRow));
        }
        return result;
    }
}
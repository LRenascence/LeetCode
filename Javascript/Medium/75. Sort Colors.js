/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    var red = 0, white = 0, blue = nums.length - 1;
    while(white <= blue){
        if(nums[white] == 0){
            var temp = nums[white];
            nums[white] = nums[red];
            nums[red] = temp;
            white ++;
            red ++;
        }
        else if(nums[white] == 1){
            white ++;
        }
        else{
            var temp = nums[white];
            nums[white] = nums[blue];
            nums[blue] = temp;
            blue --;
        }
    }
    return ;
};
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    var fr = false, fc = false;
    for(var i = 0; i < matrix.length; i++){
        for(var j = 0; j < matrix[0].length; j++){
            if(matrix[i][j] == 0){
                if(i == 0) fr = true;
                if(j == 0) fc = true;
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    for(var i = 1; i < matrix.length; i++){
        for(var j = 1; j < matrix[0].length; j++){
            if(matrix[i][0] == 0 || matrix[0][j] == 0){
                matrix[i][j] = 0;
            }
        }
    }
    if(fr){
        for(var j = 0; j < matrix[0].length; j++){
            matrix[0][j] = 0;
        }
    }
    if(fc){
        for(var i = 0; i < matrix.length; i++){
            matrix[i][0] = 0;
        }
    }
    return ;
};
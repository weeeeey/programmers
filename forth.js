const rotateMatrix = (matrix, rotateNum = 1) => {
    let N = matrix.length;
    let M = matrix[0] && matrix[0].length;

    rotateNum = rotateNum % 4;
    if (rotateNum === 0) {
        return matrix;
    }

    let result = [];
    let rotateCount = rotateNum % 2 === 1 ? [M, N] : [N, M];

    for (let row = 0; row < rotateCount[0]; row++) {
        result[row] = [];
        for (let col = 0; col < rotateCount[1]; col++) {
            if (rotateNum === 1) {
                result[row][col] = matrix[N - col - 1][row];
            } else if (rotateNum === 2) {
                result[row][col] = matrix[N - row - 1][M - col - 1];
            } else result[row][col] = matrix[col][M - row - 1];
        }
    }
    return result;
};
const find_rectri = (gr, topX, topY) => {
    let temp = Object.assign([], gr);
    let width = 2;
    let bool = true;
    // while (true) {
    //     let compareTemp;
    //     if (temp[topX][topY] === 0) {
    //         compareTemp = Array(width).fill(0);
    //     } else {
    //         compareTemp = Array(width).fill(1);
    //     }
    //     if (topY === 0) {
    //         compareTemp.push(0);
    //     } else {
    //         compareTemp.push(0);
    //         compareTemp.unshift(0);
    //     }
    //     if (
    //         Object.is(
    //             temp[topX].substring(topY - 1, topY + compareTemp.length),
    //             compareTemp
    //         )
    //     ) {
    //         console.log('saa');
    //     } else {
    //         bool = false;
    //         break;
    //     }
    // }
    console.log(temp[topX]);

    return temp;
};
const find_mirror = (gr, topX, topY) => {
    return;
};
function solution(graph) {
    let answer = 0;

    for (let k = 0; k < 4; k++) {
        let gr = rotateMatrix(graph, k);
        const n = gr.length;
        const m = gr[0].length;
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                console.log(gr[i][j]);
                // if (gr[i][j] === 1) {
                //     if (gr[i][j + 1] !== 1) {
                //         gr = find_rectri(gr, i, j);
                //         gr = find_mirror(gr, i, j);
                //     }
                // }
            }
        }
    }

    return answer;
}

// 테스트
const graph = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
];

console.log(solution(graph));

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    const n = parseInt(input);

    // 높이가 n인 삼각형 출력
    for (let i = 1; i <= n; i++) {
        let row = '';
        // 공백 추가
        // 별표 추가
        for (let j = 0; j < i * 2 - 1; j++) {
            row += '*';
        }
        console.log(row);
    }
});

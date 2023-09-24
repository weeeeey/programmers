const find_rectri = (gr, x, y) => {
    const n = gr.length;
    const m = gr[0].length;
    const dx = [-1, 0, 1]; // 위, 오른쪽, 왼쪽 방향
    const dy = [0, 1, -1];

    const isInside = (nx, ny) => nx >= 0 && nx < n && ny >= 0 && ny < m;

    const dfs = (nx, ny) => {
        gr[nx][ny] = 0; // 방문한 곳은 0으로 표시
        for (let d = 0; d < 3; d++) {
            const nx2 = nx + dx[d];
            const ny2 = ny + dy[d];
            if (isInside(nx2, ny2) && gr[nx2][ny2] === 1) {
                dfs(nx2, ny2);
            }
        }
    };

    dfs(x, y); // DFS 시작
    return gr; // 변경된 그래프 반환
};

// 테스트
const graph = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
];

console.log(solution(graph));

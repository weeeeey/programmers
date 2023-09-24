function solution(s) {
    let answer = 1_000;
    const n = s.length;

    q = [];
    if (s[0] < s[1]) {
        q.push([-1, 1, 0]);
    } else if (s[0] === 10_000 && s[1] === 10_000) {
        q.push([-1, 1, 2]);
    } else {
        q.push([1, 1, 1]);
        q.push([-1, 0, 1]);
    }
    while (q.length) {
        let [bool, cur, cnt] = q.shift();
        if (cur === n - 1) {
            answer = Math.min(cnt);
            continue;
        }
        if (bool === 1) {
            if (s[cur] < s[cur + 1]) {
                q.push([-1, cur + 1, cnt]);
            } else {
                q.push([1, cur + 1, cnt + 1]);
            }
        }
        if (bool === -1) {
            if (s[cur] > s[cur + 1]) {
                q.push([1, cur + 1, cnt]);
            } else {
                q.push([-1, cur + 1, cnt + 1]);
            }
        }
    }

    return answer;
}

console.log(solution([1, 2, 3]));

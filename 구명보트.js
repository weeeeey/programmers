function solution(people, limit) {
    let answer = 0;
    let cur = 0;
    const n = people.length;
    people.sort();
    while (cur < n) {
        temp = 0;
        answer += 1;
        const tc = cur;
        for (let i = tc; i < n; i++) {
            if (people[i] + temp <= limit) {
                cur += 1;
                temp += people[i];
            } else {
                break;
            }
        }
    }
    return answer;
}
const people = [70, 50, 80, 50];
const limit = 100;
console.log(solution(people, limit));

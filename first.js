function solution(phone) {
    let answer = -1;
    if (phone.length === 13 && phone.substring(0, 4) === '010-') {
        const pattern = /^\d{4}-\d{4}$/;
        if (pattern.test(phone.substring(4))) {
            answer = 1;
        }
    } else if (phone.length === 11 && phone.substring(0, 3) === '010') {
        const pattern = /^\d{8}$/;
        if (pattern.test(phone.substring(3))) {
            answer = 2;
        }
    } else if (phone.length === 16 && phone.substring(0, 7) === '+82-10-') {
        const pattern = /^\d{4}-\d{4}$/;
        if (pattern.test(phone.substring(7))) {
            answer = 3;
        }
    }
    return answer;
}

console.log(solution('010-1234-5678'));

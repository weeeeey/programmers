function findSeats(seats) {
    const seatsArray = seats.split(''); // 문자열을 배열로 변환
    const minSeats = seatsArray.slice(); // 최소한으로 앉을 자리 복사
    const maxSeats = seatsArray.slice(); // 최대한 많이 앉을 자리 복사

    // 최소한으로 앉을 자리 찾기
    for (let i = 0; i < seatsArray.length; i++) {
        if (
            seatsArray[i] === '.' &&
            (i === 0 || seatsArray[i - 1] === '#' || seatsArray[i + 1] === '#')
        ) {
            minSeats[i] = 'A'; // 사람이 앉을 수 있는 자리
        }
    }

    // 최대한 많이 앉을 자리 찾기
    for (let i = 0; i < seatsArray.length; i++) {
        if (seatsArray[i] === '.') {
            maxSeats[i] = 'A'; // 사람이 앉을 수 있는 자리
        }
    }

    return [minSeats.join(''), maxSeats.join('')];
}

const seats = '...#.....';
const [minSeatArrangement, maxSeatArrangement] = findSeats(seats);

console.log('최소한으로 앉는 자리:', minSeatArrangement);
console.log('최대한 많이 앉는 자리:', maxSeatArrangement);

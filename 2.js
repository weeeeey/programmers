function countPossiblePasswords(phoneNumber, birthday) {
    var phoneDigits = phoneNumber.replace(/\D/g, ''); // 전화번호에서 숫자만 추출
    var birthdayDigits = birthday.replace(/\D/g, ''); // 생년월일에서 숫자만 추출

    var count = 0;
    var generatedPasswords = {};

    while (true) {
        var password = generatePassword(phoneDigits, birthdayDigits);
        if (!generatedPasswords[password]) {
            generatedPasswords[password] = true;
            count++;
        }
        // 모든 가능한 비밀번호를 생성했을 때 루프 종료
        if (count === 10000) {
            break;
        }
    }

    return count;
}
function generatePassword(phoneNumber, birthday) {
    var phoneDigits = phoneNumber.replace(/\D/g, ''); // 전화번호에서 숫자만 추출
    var birthdayDigits = birthday.replace(/\D/g, ''); // 생년월일에서 숫자만 추출

    // 무작위로 4개의 숫자를 선택하여 비밀번호 생성
    var password = getRandomDigits(phoneDigits, 4);

    // 전화번호와 생년월일로부터 선택한 숫자가 비밀번호와 다를 때까지 재시도
    while (
        password == getRandomDigits(phoneDigits, 4) ||
        password == getRandomDigits(birthdayDigits, 4)
    ) {
        password = getRandomDigits(phoneDigits, 4);
    }

    return password;
}

function getRandomDigits(inputDigits, count) {
    if (inputDigits.length < count) {
        throw new Error('Not enough digits in the input.');
    }

    var startIndex = Math.floor(
        Math.random() * (inputDigits.length - count + 1)
    );
    return inputDigits.substr(startIndex, count);
}

// 예제 사용법

var phoneNumber = '54662345';
var birthday = '20010923';
var totalPossiblePasswords = countPossiblePasswords(phoneNumber, birthday);
console.log('조건을 만족하는 비밀번호의 총 개수: ' + totalPossiblePasswords);

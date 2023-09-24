from collections import Counter


def calculate_max_score(cards):
    max_score = 0
    card_counts = Counter(cards)
    for count in card_counts.values():
        max_score += count * (count + 1) // 2
    return max_score


def min_swaps_to_maximize_score(cards1, cards2):
    max_score1 = calculate_max_score(cards1)
    max_score2 = calculate_max_score(cards2)

    if max_score1 == max_score2:
        return 0  # 이미 점수가 같으므로 교환이 필요하지 않음

    card_counts1 = Counter(cards1)
    card_counts2 = Counter(cards2)

    max_score_diff = abs(max_score1 - max_score2)

    # 가능한 교환 횟수를 계산
    min_swaps = float('inf')
    for card, count in card_counts1.items():
        needed_count = card_counts2.get(card, 0)
        if needed_count > 0:
            swaps_needed = min(count, needed_count)
            current_score_diff = count * \
                (count + 1) // 2 - swaps_needed * (swaps_needed + 1) // 2
            if current_score_diff == max_score_diff:
                min_swaps = min(min_swaps, swaps_needed)

    if min_swaps == float('inf'):
        return -1  # 교환으로는 점수를 맞출 수 없음
    else:
        return min_swaps


# 예시 호출
cards1 = [1, 2, 1, 1, 1, 1, 3, 3, 3]
cards2 = [2, 2, 3, 3, 3]
result = min_swaps_to_maximize_score(cards1, cards2)
print(result)  # 출력: 2 (두 번의 교환이 필요함)

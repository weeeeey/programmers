# 그 프로젝트는 검색어에 가장 잘 맞는 웹페이지를
# 보여주기 위해 아래와 같은 규칙으로 검색어에 대한
# 웹페이지의 매칭점수를 계산 하는 것이었다.

# 한 웹페이지에 대해서 기본점수, 외부 링크 수, 링크점수, 그리고 매칭점수를 구할 수 있다.

#기본점수: 해당 웹페이지의 텍스트중, 검색어가 등장하는 횟수이다. (대소문자 무시)한

# 외부 링크 수: 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수이다.한

# 링크점수: 해당 웹페이지로 링크가 걸린 다른 기본점수 ÷ 외부 링크 수의 총합이다.한

# 매칭점수: 기본점수와 링크점수의 합으로 계산한다.

# print(a.lower())

def solution(word, pages):
    word = word.lower()
    answer = "answer"
    n = len(pages)
    gr = dict()  # [기본 점수, 외부 링크 갯수, 들어오는 딕셔너리 키 저장]
    result = dict()
    a = len("<meta property=\"og:url\" content=\"https://")
    for i in range(n):
        pages[i] = pages[i].lower()
        
        sss = pages[i].find("<meta property=\"og:url\" content=\"https://" )
        w = pages[i].count(word,)
        gr[pages[i][sss+a]]

        
    return answer

print(solution("blind",	['<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://a.com"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href="https://b.com"> Link to b </a>\n</body>\n</html>', '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://b.com"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href="https://a.com"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href="https://c.com"> Link to c </a>\n</body>\n</html>', '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://c.com"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href="https://a.com"> Link to a </a>\n</body>\n</html>']))



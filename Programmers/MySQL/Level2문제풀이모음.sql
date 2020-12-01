-- 최솟값 구하기
-- https://programmers.co.kr/learn/courses/30/lessons/59038
SELECT DATETIME AS '시간' FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1

-- 동물 수 구하기
-- https://programmers.co.kr/learn/courses/30/lessons/59406
SELECT COUNT(*) AS COUNT FROM ANIMAL_INS
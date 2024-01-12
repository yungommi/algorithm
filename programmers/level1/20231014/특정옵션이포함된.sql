-- 예상 시간복잡도 (NlogN)

SELECT car_id, car_type, daily_fee, options FROM car_rental_company_car
WHERE options REGEXP '네비게이션'
ORDER BY car_id DESC;

;; sussman anomaly https://en.wikipedia.org/wiki/Sussman_anomaly

(define (problem psussman)
  (:domain bw)
  (:objects A B C)
  (:init (arm-empty)
  	  (on-table A)
	  (on C A)
	  (clear C)
	  (on-table B)
	  (clear B))
  (:goal (and (on A B) (on B C))))




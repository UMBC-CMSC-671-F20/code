;; The arm is empty and there are two blocks on the table: A and B.
;; Put A on top of B.

(define (problem p02)
  (:domain bw)
  (:objects A B)
  (:init (arm-empty)
  	  (on-table A)
	  (clear A)
    	  (on-table B)
	  (clear B))
  (:goal (on A B)))
  




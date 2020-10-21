;; The arm is empty and there is a stack of three blocks: C is on B
;; which is on A which is on the table.  The goal is to reverse the
;; stack, i.e., have A on B and B on C.  We don't need to mention that
;; C is on the table, since the domain constraints will enforce it.

(define (problem p03)
  (:domain bw)
  (:objects A B C)
  (:init (arm-empty)
  	  (on-table A)
	  (on B A) 
	  (on C B)
	  (clear C))
  (:goal (and (on A B) (on B C))))




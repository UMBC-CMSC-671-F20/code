(define (domain jug-pouring)

  (:requirements :typing :fluents)

  (:types jug)

  (:functions
    (amount ?j - jug) - number
    (capacity ?j - jug) - number)

  (:action pour
    :parameters (?jug1 ?jug2 - jug)
    :precondition (> (- (capacity ?jug2) (amount ?jug2)) 0)
    :effect (and
     ; if the available space in jug2 is larger or equal to the amount in
    ; jug1, we pour everything in and jug1 is empty.
                (when (>= (- (capacity ?jug2) (amount ?jug2)) (amount ?jug1))
                  (and
		     (increase (amount ?jug2) (amount ?jug1))
                     (assign (amount ?jug1) 0)
                  ))
    ; if jug2 can only be partially filled, we subtract the amount from jug1
    ; and add it to jug2 until jug2 is full.
      	     	(when (< (- (capacity ?jug2) (amount ?jug2)) (amount ?jug1))
                  (and
                     (decrease (amount ?jug1) (- (capacity ?jug2) (amount ?jug2)))
		     (assign (amount ?jug2) (capacity ?jug2))
		  ))
           ))
)

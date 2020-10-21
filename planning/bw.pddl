;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Blocks world 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain bw)
  (:requirements :strips)
  (:predicates
      (on ?x ?y)         ; object ?x is on ?object ?y
      (on-table ?x)   ; ?x is directly on the table
      (clear ?x)         ; ?x has nothing on it
      (arm-empty)   ; robot isn't holding anything
      (holding ?x))   ; robot is holding ?x

  ;; the four classic actions for manipulating objects

  (:action pick-up
     :parameters (?ob1)
     :precondition (and (clear ?ob1) (on-table ?ob1) (arm-empty))
     :effect
     (and (not (on-table ?ob1))
  	     (not (clear ?ob1))
	     (not (arm-empty))
	     (holding ?ob1)))

  (:action put-down
     :parameters (?ob)
     :precondition (holding ?ob)
     :effect
     (and (not (holding ?ob))
	   (clear ?ob)
	   (arm-empty)
	   (on-table ?ob)))

  (:action stack
     :parameters (?sob ?sunderob)
     :precondition (and (holding ?sob) (clear ?sunderob))
     :effect
     (and (not (holding ?sob))
	   (not (clear ?sunderob))
	   (clear ?sob)
	   (arm-empty)
	   (on ?sob ?sunderob)))

  (:action unstack
     :parameters (?sob ?sunderob)
     :precondition (and (on ?sob ?sunderob) (clear ?sob) (arm-empty))
     :effect
     (and (holding ?sob)
	   (clear ?sunderob)
	   (not (clear ?sob))
	   (not (arm-empty))
	   (not (on ?sob ?sunderob))))
)

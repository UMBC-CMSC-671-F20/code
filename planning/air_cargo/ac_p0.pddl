;; PDDL instance problem for the Air cargo transport

(define (problem pb1)
  (:domain air-cargo)
  (:objects C1 C2
        P1 P2
        SFO JFK)
  (:init
   ;; types
   (Cargo C1) (Cargo C2)
   (Plane P1) (Plane P2)
   (Airport SFO) (Airport JFK)

   ;; locations
   (At C1 SFO) (At C2 JFK) (At P1 SFO) (At P2 JFK))

  (:goal (and (At C1 JFK) (At C2 SFO))))

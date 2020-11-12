;; PDDL instance problem for the Air cargo transport

;;  Plane P1 is at SFO and plane P2 is at JFK.
;;  We need to move cargo C1 from SFO to JFK and cargo C2 from JFK to SFO.

(define (problem ac_p0)

  (:domain air-cargo)
  
  (:objects
        C1 C2      ;;cargo objects
        P1 P2       ; plane objects
        SFO JFK)   ; airports
	
  (:init
   ;; types
   (Cargo C1) (Cargo C2)
   (Plane P1) (Plane P2)
   (Airport SFO) (Airport JFK)

   ;; locations
   (At C1 SFO) (At C2 JFK) (At P1 SFO) (At P2 JFK))

  (:goal (and (At C1 JFK) (At C2 SFO))))

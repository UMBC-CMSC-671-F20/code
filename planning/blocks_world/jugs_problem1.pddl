(define (problem jug-pouring-problem)

  (:domain jug-pouring)

  (:objects jug3 jug5 jug8 - jug)

  (:init (= (amount jug3) 0)
         (= (capacity jug3) 3)
         (= (amount jug5) 0)
         (= (capacity jug5) 5)
         (= (amount jug8) 8)
         (= (capacity jug8) 8))

  (:goal (= (amount jug8) 4))
)

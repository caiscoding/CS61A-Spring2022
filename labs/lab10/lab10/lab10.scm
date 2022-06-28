(define (over-or-under num1 num2)
  (cond
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    ((> num1 num2) 1))
)

(define (make-adder num)
    (lambda (inc) (+ num inc))
)

(define (composed f g)
    (lambda (x) (f (g x)))
)

(define (square n) (* n n))

(define (pow base exp)
    (cond
        ((zero? exp) 1)
        ((even? exp) (square (pow base (/ exp 2))))
        ((odd? exp) (* base (pow base (- exp 1)))))
)

(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
(cond
    ((null? items) nil)
    (else (cons (proc (car items))
                  (map proc
(cdr items))))))

(define (cons-all first rests)
  'replace-this-line)

(define (zip pairs)
(cond
    ((null? pairs) (list '() '()))
    ((null? (car pairs)) nil)
    (else (append (list (map car
                             pairs))
                    (zip (map cdr
pairs))))))

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  (define (helper s i)
        (cond ((eq? s nil) nil)
              (else (cons (list i (car s)) (helper (cdr s) (+ i 1))))
      )
    )
   (helper s 0)
  )
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  'replace-this-line
  )
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         expr
         )
        ((quoted? expr)
         expr
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; (define evaluated-body (map let-to-lambda body))
           (cons form (cons params (map let-to-lambda body)))
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           (append (list (cons 'lambda (cons (car (zip values))
                                (append (map let-to-lambda body) nil))))
                    (map let-to-lambda (cadr (zip values))))
           ))
        (else
         (map let-to-lambda expr)
         )))

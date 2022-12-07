package utils

type Set[T comparable] map[T]struct{}

func (s Set[T]) Add(m T) {
    s[m] = struct{}{}
}

func (s Set[T]) Remove(m T) {
    delete(map[T]struct{}(s), m)
}

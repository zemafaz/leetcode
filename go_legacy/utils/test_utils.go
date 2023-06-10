package utils

import "testing"

func GenTestErrorMessage(t *testing.T, n int, expected interface{}, returned interface{}) {
	t.Errorf("Failed test %d:\n\tExpected: %v\n\tReturned: %v\n", n, expected, returned)
}

package udmx

import (
	"fmt"

	"github.com/creasty/defaults"
)

/*
Genera un Step, si no puso algun campo se inicializa en su valor default.
*/
func NewStep(duration, fadetime uint16) (*Step, error) {
	step := Step{
		Values:   [512]uint8{},
		Duration: duration,
		FadeTime: fadetime,
	}
	if err := defaults.Set(step); err != nil {
		return &Step{}, fmt.Errorf("error NewStep: %w", err)
	}
	return &step, nil
}

/*
Agrega a un canal un valor
*/
func (s *Step) AddValue(ch uint16, val uint8) {
	s.Values[ch] = val
}

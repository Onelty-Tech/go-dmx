package udmx

import (
	"errors"
	"fmt"
	"time"

	"github.com/google/gousb"
)

// Perfil principal del controlador uDMX
type Device struct {
	Dev *gousb.Device
}

// Crea una nueva instancia uDMX
func NewUDMXDevice(ctx *gousb.Context) (*Device, error) {

	dev, err := ctx.OpenDeviceWithVIDPID(0x16c0, 0x5dc)
	if err != nil {
		return nil, err
	}
	if dev == nil {
		return nil, errors.New("could not find uDMX device")
	}
	// m, err := dev.Manufacturer()
	// if err != nil {
	// 	return nil, err
	// }
	// if m != "www.anyma.ch" {
	// 	return nil, errors.New("found possible uDMX device but wrong manufacturer string found")
	// }

	return &Device{
		Dev: dev,
	}, nil
}

/*
Set, funcion estandar para enviar bytes al puerto.
*/
func (d *Device) Set(address, value uint16) error {
	if _, err := d.Dev.Control(gousb.ControlOut|gousb.ControlVendor|gousb.ControlDevice, 1, value, address-1, []byte{}); err != nil {
		return fmt.Errorf("error Set: %w", err)
	}
	return nil
}

func (d *Device) Clear() error {
	for ch := uint16(1); ch <= 255; ch++ {
		if err := d.Set(ch, 0); err != nil {
			return fmt.Errorf("error Clear: %w", err)
		}
	}
	return nil
}



func (d *Device) PlayChase(chase Chase) error {
	for _, step := range chase {
		for ch, value := range step.Values {
			if err := d.Set(uint16(ch), uint16(value)); err != nil {
				return fmt.Errorf("error PlayChase:%w", err)
			}
		}
		time.Sleep(time.Duration(step.Duration) * time.Millisecond)
	}
	return nil
}


package main

import (
	"fmt"

	"main/udmx"

	"github.com/google/gousb"
)

func main() {
	// Crea el contexto para mantenerlo como servicio
	ctx := gousb.NewContext()
	defer ctx.Close()

	fmt.Println("Buscando adaptador uDMX...")

	/*
		Esto abre el dispositivo, retornando la estructura.
	*/
	device, err := udmx.NewUDMXDevice(ctx)
	if err != nil {
		panic(fmt.Sprintf("Error abriendo dispositivo: %v", err))
	}
	// No hay un método .Close() oficial en esa librería udmx,
	// pero el ctx.Close() de arriba se encargará de liberar el USB.

	fmt.Println("Adaptador encontrado. Enviando datos...")

	/*
		Hace una iteracion para encender cada canal
	*/
	// for i := uint16(1); i <= 6; i++ {
	// 	if err := device.Set(i, 0); err != nil {
	// 		fmt.Println("Error:", err.Error())
	// 		return
	// 	}
	// }

	var sceneTwo = udmx.Chase{
		udmx.Step{
			Values:   [512]uint8{255, 255, 255, 255, 255},
			Duration: 300,
			FadeTime: 40,
		},
		udmx.Step{
			Values:   [512]uint8{255, 255, 144, 255, 255},
			Duration: 300,
			FadeTime: 40,
		},
		udmx.Step{
			Values:   [512]uint8{255, 255, 255, 122, 200},
			Duration: 300,
			FadeTime: 40,
		},
	}
	device.Clear()
	for {
		if err := device.PlayChase(sceneTwo); err != nil {
			fmt.Println(err.Error())
			return
		}
	}
	// for {
	// 	for ch, steps := range sceneOne {
	// 		for _, step := range steps {
	// 			if err := device.Set(ch, step); err != nil {
	// 				fmt.Println(err)
	// 				return
	// 			}
	// 			time.Sleep(40 * time.Millisecond)
	// 		}
	// 	}
	// }
	// if err := device.Set(uint16(1), uint16(0)); err != nil {
	// 	fmt.Println(err)
	// 	return
	// }
	// if err := device.Set(uint16(2), uint16(0)); err != nil {
	// 	fmt.Println(err)
	// 	return
	// }
}

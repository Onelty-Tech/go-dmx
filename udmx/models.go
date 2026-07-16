package udmx

type Chase []Step

type Step struct {
	/*
		El indice representa el canal y el valor el movimiento, en cada canal de cada step solo puede
		haber un movimiento por canal, pero todos juntos haran un show.
	*/
	Values   [512]uint8
	Duration uint16 `default:"40"` //tiempo que se mantendra esta luz
	FadeTime uint16 `default:"40"` // cuanto tiempo para pasarse suavemente al otro paso
}

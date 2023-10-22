Algoritmo primo
	//definimos variables
    definir n1, divisor, contador como entero
	//colocamos valores
    divisor = 1
    contador = 0
    
    //se le pide al usuario ingresar el número
    Escribir("Por favor, ingrese el número:")
    Leer n1
    //empezamos  con la selectiva si, para descartar las excepciones que son el 2 y numeros negativos
    Si n1 == 2 Entonces
        Escribir("2 es el único número par que es primo")
	Sino Si n1 <= 1 Entonces;
			Escribir(" Al no ser mayor a 1, no es primo.")
		Sino
			Mientras divisor <= n1 Hacer
				Si n1 % divisor == 0 Entonces;
					contador = contador + 1
				Fin Si
				divisor = divisor + 1
				Si contador > 3 Entonces;
				Fin Si
				Si divisor >= 101 
					Escribir "El número ", n1, " SI es primo"
				FinSi

			Fin Mientras
			
			Si contador == 2 Entonces;
				Escribir "El número ", n1, " SI es primo";
			Fin Si
			Si contador >= 3 Entonces;
				Escribir "El número ", n1, " NO es primo "
			Fin Si
		Fin Si
	FinSi
	
FinAlgoritmo
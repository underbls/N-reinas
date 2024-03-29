#include <stdlib.h>
#include <time.h>
#include<iostream>
#include <math.h>

using namespace std;

//funcion que genera un numero randomico entre 1 -0
int randomhasta1(){
int num, c;
    srand(time(NULL));

    num = rand() % 2;
    cout << num<< " ";

    return 0;
}

//funcion que genera numero randomico entre 1 - N
int randomhastaN(int N){
	int num=0;
    srand(time(NULL));
 
    num = rand() % (N-1);

    return num;
}

//shuffle es la funcion de revuelve el vector
void shuffle(int vectortabla[], int largo){	
	int temp = 0;
	int randomIndex = 0;
	
	for (int i = 0; i < largo; i++){
		randomIndex = rand() % largo;
		temp = vectortabla[i];
		vectortabla[i] = vectortabla[randomIndex];	
		vectortabla[randomIndex] = temp;
	}	
}

int EvaluarFitnes(int vectortabla[], int length){
    int j, countchoques=0;
    
    for(int i=0; i < length ;i++)
    {
        j=i+1;
        
        for(int k=i; k < length ;k++)
        {
        	int posvector = abs(j-k+2);
        	int valorvector = abs(vectortabla[i]-vectortabla[k+1]);
            if ( posvector =  valorvector)
            {
                countchoques=countchoques+1;
            }
        }
    }
    
    return countchoques;
}


//funcion que inicia la poblacion
int inicializarPoblacion(){
	//N = tama�o tablero y M=poblacion
	int N=8,M=1;
	int vectortabla[N];
	
	//hay que inicializar esto para utilizar el metodo rand() RANDOM
	srand(time(NULL));
	   
	//se inicializa el vector con valores de 1 hasta N
	for (int i = 0; i < N; i++){
		vectortabla[i] = i+1;	
	}
	
	//se llama la funcion shuffle para revolver los valores dentro del vector.
	shuffle(vectortabla,N);
	
	//imprime ne pantalla el vector desordenado
	for (int i = 0; i < N; i++){
		cout << vectortabla[i]<< " ";
	}
	
	return 0;
}
 
int main()
{
	inicializarPoblacion();
}

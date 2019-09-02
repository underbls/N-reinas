#include <stdlib.h>
#include <time.h>
#include<iostream>
using namespace std;

int randomhasta1(){
int num, c;
    srand(time(NULL));

    num = rand() % 2;
    cout << num<< " ";

    return 0;
}

int randomhastaN(int N){
int num;
    srand(time(NULL));

    num = rand() % (N-1);

    return num;
}

int inicializarPoblacion(){
//N = tamaño tablero y M=poblacion
int N=8,M=1;
int vectortabla[N];
srand(time(NULL));

for (int i = 0; i < N; i++){
        vectortabla[i] = randomhastaN(N);
        cout <<  vectortabla[i]<< "=" << i <<"-";
    }
    return 0;
}

int main()
{
inicializarPoblacion();
}

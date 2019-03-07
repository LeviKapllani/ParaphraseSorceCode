#include <iostream>
#include <iomanip>

using namespace std;

void bubbleSort(int *, const int);
void swap(int * const, int * const);

int main(int argc, const char * argv[]) {
    
    const int sizeArray = 10;
    
    int a[sizeArray] = { 2, 6, 4, 8, 10, 12, 89, 68, 45, 37 };
    
    cout<<"Elements in the array: "<<endl;
    
    for(int i=0; i<sizeArray; i++){
        cout<< setw(4)<<a[i];
    }
    cout<<endl;
    
    bubbleSort(a, sizeArray);
    
    cout<<"Elements sorted in the array: "<<endl;
    
    for(int i=0; i<sizeArray; i++){
        cout<< setw(4)<<a[i];
    }
    
    return 0;
}

void bubbleSort(int *a, const int size){
    for(int i=0; i<size-1;i++){
        for(int j=0; j<size-1;j++){
            if(a[j]>a[j+1]){
                swap(&a[j], &a[j+1]);
            }
        }
    }
}

void swap(int * const a, int * const b){
    int aux = *a;
    *a = *b;
    *b = aux;
}
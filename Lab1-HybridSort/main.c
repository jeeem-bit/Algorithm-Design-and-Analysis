#include <stdio.h>
#include <stdlib.h>

void main(){
    static int arr[100]; // arr1[1000], arr2[100000], arr3[10000000];
    int n = 100; // n1 = 1000, n2 = 100000, n3 = 10000000;
    populate(arr, n);
    // populate(arr1, n1);
    // populate(arr2, n2);
    // populate(arr3, n3);
    int s = 75;

    //sort(arr1, n1, s);
    // sort(arr2, n2, s);
    // sort(arr3, n3, s);
    sort(arr, n, s);
}

// To generate integers 1-10 mil (i cant generate to 10 mil, max is 32768)
void populate(int arr[], int n){
    srand((unsigned int)time(NULL));

    for (int i=0; i<n; i++){
        arr[i] = rand() % 32768 + 1; // would be 10 mil if could generate 10 mil in rand()
    }
}

// To show results
void sort(int arr[], int n, int s){
    printf("Unsorted array: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    hybridSort(arr, 0, n-1, s);

    printf("Sorted array: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* void hybridSort(int arr[], int left, int right, int s) {
    // If subarray of size s is reached, use insertion
    if (right - left + 1 <= s) {
        insertionSort(arr + left, right - left + 1);
    // else split the array and call recursively
    } else {
        int mid = left + (right - left) / 2;
        hybridSort(arr, left, mid, s);
        hybridSort(arr, mid + 1, right, s);

        // merge sorted sides
        int left_size = mid - left + 1;
        int right_size = right - mid;
        int left_half[left_size];
        int right_half[right_size];

        for (int i = 0; i < left_size; i++) {
            left_half[i] = arr[left + i];
        }
        for (int i = 0; i < right_size; i++) {
            right_half[i] = arr[mid + 1 + i];
        }

        merge(arr + left, left_half, right_half, left_size, right_size);
    }
}


void merge(int arr[], int left[], int right[], int left_size, int right_size) {
    int i = 0, j = 0, k = 0;

    while (i < left_size && j < right_size) {
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        } else {
            arr[k++] = right[j++];
        }
    }

    while (i < left_size) {
        arr[k++] = left[i++];
    }

    while (j < right_size) {
        arr[k++] = right[j++];
    }
}


void insertionSort(int arr[], int n) {
    int i, j, curr;

    for (i = 1; i < n; i++) {
        curr = arr[i];
        j = i - 1; // begin comparisons from element before curr

        // while element infront is larger than curr, swap
        while (j >= 0 && arr[j] > curr) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = curr; // insert curr in sorted position
    }
} */


int comparision = 0;
void insertion_sort(int arr[], int size, int left){
  for(int i = 1; i < size; i++){
    for(int j = i; j > 0; j--){
      if(arr[left + j] < arr[left + j - 1]){
        int temp = arr[left + j - 1];
        arr[left + j - 1] = arr[left + j];
        arr[left + j] = temp;
        comparision++;
      }
      else{
        break;
      }
    }
  }
}
void merge(int arr[], int left_arr1, int right_arr1, int left_arr2, int right_arr2){
  int res[right_arr2 - left_arr1 + 1]; // array store elements after merge
  int pointer1, pointer2;
  pointer1 = left_arr1;
  pointer2 = left_arr2;
  int index = 0;
  while(pointer1 <= right_arr1 && pointer2 <= right_arr2 ){
    if(arr[pointer1] <= arr[pointer2]){
      res[index] = arr[pointer1];
      pointer1++;
    }
    else{
      res[index] = arr[pointer2];
      pointer2++;
    }
    index++;
    comparision++;
  }
  if(pointer1 > right_arr1){
    while(pointer2 <= right_arr2){
      res[index] = arr[pointer2];
      pointer2++;
      index++;
    }
  }
  else{
    while(pointer1 <= right_arr1){
      res[index] = arr[pointer1];
      pointer1++;
      index++;
    }
  }
  for(int i = left_arr1; i <= right_arr2; i++){
    arr[i] = res[i-left_arr1];
  }
}
void hybridSort(int arr[], int left, int right, int threshold){
  int mid = (left + right)/2;
  int size = right-left+1;
  if((right-left) <= 0){
    return;
  }
  if(size <= threshold ){
    insertion_sort(arr, size, left);
  }
  else{
    //recursively call to divide the array into subarray
    hybridSort(arr, left, mid, threshold);
    hybridSort(arr, mid+1, right, threshold);
    merge(arr, left, mid, mid+1, right);
  }
}

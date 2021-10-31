import java.util.*;

// selection sort
// runtime: O(n^2)
public class selection {
  public static void main(String[] args){

    int n = 10;
    int[] arr = {4,5,3,2,7,6,9,8,0,1};

    for (int i = 0; i < n; i++) {
      int min_index = i;
      for (int j = i + 1; j < n; j++) {
        if (arr[min_index] > arr[j]) {
          min_index = j;
        }
      }
      int temp = arr[i];
      arr[i] = arr[min_index];
      arr[min_index] = temp;
    }
    for (int i = 0; i < n; i++){
      System.out.print(arr[i] + " ");
    }
  }
}

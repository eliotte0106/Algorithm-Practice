import java.util.*;

// insertion sort: works well if the elements in the array are almost sorted.
// Runtime: worst case: O(n^2), best case: O(n)
public class insertion {
  public static void main(String[] args) {
    int n = 10;
    int[] arr = {4,5,3,2,7,6,9,8,0,1};
    //going from right to left starting from second index
    for (int i = 1; i < n; i++) {
      for (int j = i; j > 0; j--) {
        if (arr[j] < arr[j - 1]){
          int temp = arr[j];
          arr[j] = arr[j - 1];
          arr[j - 1] = temp;
        } else {
          break;
        }
      }
    }
  for (int i = 0; i < n; i++){
    System.out.print(arr[i] + " ");
    }
  }
}

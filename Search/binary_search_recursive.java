import java.util.*;

//In order to use binary search, we should assume the array is sorted.
// binary search (recursive)
// runtime: O(log n)
public class binary_search_recursive {
  public static int binary_search_recursive(int[] arr, int target, int start, int end) {
    if (start > end) {
      return -1;
    }
    int mid = (start + end) / 2;
    if (arr[mid] == target) {
      return mid;
    }
    //if the target is less than the value of mid
    else if (arr[mid] > target) {
      return binary_search_recursive(arr,target,start, mid - 1);
    }
    //if the target is greater than the value of mid
    else {
      return binary_search_recursive(arr, target, mid + 1, end);
    }
  }
}

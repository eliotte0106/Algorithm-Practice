import java.util.*;

//In order to use binary search, we should assume the array is sorted.
// binary search (recursive)
// runtime: O(log n)
public class binary_search_iterative {
  public static int binarySearch(int[] arr, int target, int start, int end) {
    while (start <= end) {
      int mid = (start + end) / 2;
      if (arr[mid] == target) {
        return mid;
      }
      else if (arr[mid] > target) {
        end = mid - 1;
      }
      else {
        start = mid + 1;
      }
    }
    return -1;
  }
}

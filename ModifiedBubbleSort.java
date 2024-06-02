import java.util.Arrays;

class ModifiedBubbleSort {
  public static void main(String[] args) {
    int[] data = { 45, 81, 21, 12, 7 };
    int size = data.length;

    for (int i = 0; i < (size - 1); i++) {
      boolean swapped = false;

      for (int j = 0; j < (size - i - 1); j++) {
        if (data[j] > data[j + 1]) {
          int temp = data[j];
          data[j] = data[j + 1];
          data[j + 1] = temp;
          
          swapped = true;
        }
      }

      if (!swapped)
        break;
    }

    System.out.println("Sorted Array:");
    System.out.println(Arrays.toString(data));
  }
}

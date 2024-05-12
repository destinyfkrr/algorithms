public class InsertionSort {
    public static void main(String[] args) {
        int[] array = {31, 42, 13, 63, 52, 69};
        insertionSort(array);
        System.out.println("Sorted array in ascending order:");
        for (int num : array) { 
            System.out.print(num + " ");
        }
    }

    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
}

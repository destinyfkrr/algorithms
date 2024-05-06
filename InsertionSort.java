public class InsertionSort {
    public static void main(String[] args) {
        int[] array = {31, 42, 13, 63, 52, 69};
        int x = 25;
        int position = 0;
        for (int i = 0; i < 6; i++) {
            if (array[i] > x) {
                position = i;
                break;
            }
        }
        for (int i = 6; i > position; i--) {
            array[i] = array[i - 1];
        }
        array[position] = x;
        System.out.println("Example :");
        printArray(array);

    }

}

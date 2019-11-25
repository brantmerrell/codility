import java.util.Stack;
import java.util.Iterator;
class Solution {
    public static void main(String args[]) {

        // build stack of test data
        Stack<Integer> test_array = new Stack<>();
        test_array.push(1041);
        test_array.push(15);
        test_array.push(32);

        // add args to test data (if numeric)
        for(int i = 0; i < args.length; i++) {
            if(isNumeric(args[i]))
            {
                var new_test = Integer.parseInt(args[i]);
                test_array.push(new_test);
            }
        }

        // print the output of each arg for binary_gap
        var iter = test_array.iterator();
        while (iter.hasNext())
        {
            var my_int = iter.next();
            System.out.println("binary_gap(" + my_int + "): " + binary_gap(my_int));
        }
    }
    static int binary_gap (int N) {
        // convert to binary string
        String bin = Integer.toBinaryString(N);
        // remove trailing/leading zeros; split by 1s
        bin = bin.replaceAll("^0+|0+$","");

        // split by 1s
        String[] binArray = bin.split("1");

        // convert each binary gap to a character count
        int gaps[] = new int[binArray.length];
        for(int i = 0; i < binArray.length; i++) {
            gaps[i] = binArray[i].length();
        }

        // obtain maximum number from character counts
        int result = 0;
        for(int i = 0; i < gaps.length; i++) {
            if (gaps[i] > result) {
                result = gaps[i];
            }
        }
        return result;
    }
    public static boolean isNumeric(String strNum) {
        if (strNum == null) {
            return false;
        }
        try {
            double d = Double.parseDouble(strNum);
        } catch (NumberFormatException nfe) {
            return false;
        }
        return true;
    }
}

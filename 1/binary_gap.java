import java.util.Arrays;
import java.util.Collections;
class Solution {
    public static void main(String args[]) {
        if(args.length==0) {
            System.out.println("input: 1041; output: " + solution(1041));
            System.out.println("input: 15; output: " + solution(15));
            System.out.println("input: 32; output: " + solution(32));
        }
        else
        {
            for(int i = 0; i < args.length; i++) {
                System.out.println("input: " + args[i] + "; output: " + solution(Integer.parseInt(args[i])));
            }
        }
    }
    static int solution (int N) {
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
}

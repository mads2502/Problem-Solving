// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class HelloWorld {
    public static void main(String[] args) {
        System.out.println(ceilingNumber());
        
    }
    public static int ceilingNumber(){
        int[] arr={1,2,4,5,6,67,89};
        int target=65;
        int start=0;
        int mid=0;
        int end=arr.length-1;
        while(start<=end){
            mid=start+(end-start)/2;
            if(arr[mid]<target){
                start=mid+1;
                
            }
            if(arr[mid]>target){
                end=mid-1;
            }
            if(arr[mid]==target){
                return mid;
            }
            
        }
        return arr[start];
    }
}
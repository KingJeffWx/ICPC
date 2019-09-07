import java.util.*;

public class knapsack {

    public static int[][] K;
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner s = new Scanner(System.in);
        while(s.hasNextInt()) {
            String items_chosen = "";
            int items_chosen_len = 0;
            
            int max_weight = s.nextInt();
            int num_items = s.nextInt();
            Item[] items = new Item[num_items];
            K = new int[num_items+1][max_weight+1];
            for(int i=0; i<num_items; i++) {
                int value = s.nextInt();
                int weight = s.nextInt();
                items[i] = new Item(weight,value);   
            }
            int max_value = solve(max_weight, items);
            
            if(max_value == 0) {
                System.out.println(0);
            }
            else {
                int current_weight = max_weight;
                int current_value = max_value;
                int n = items.length;
                while(current_value != 0) {
                    if(current_weight >= items[n-1].getWeight()) {
                        if(K[n-1][current_weight - items[n-1].getWeight()] == current_value - items[n-1].getValue()) {
                            items_chosen = (n-1) +" " + items_chosen;
                            items_chosen_len += 1;
                            current_weight -= items[n-1].getWeight();
                            current_value -= items[n-1].getValue();
                            n -= 1;
                        }
                        else if(K[n-1][current_weight] == current_value) {
                            n = n-1;
                        }
                    }
                    else {
                        n -= 1;
                    }
                }
            }
            System.out.println(items_chosen_len);
            System.out.println(items_chosen);
        }
        /*
        try {
            
        }
        catch(Exception e) {
            System.out.println("????");
        }
        */
        
    }

    public static int solve(int W, Item[] items) {
        int n = items.length;
        for(int i=0; i<n+1; i++) {
            for(int w=0; w<W+1; w++) {
                if(i==0 || w==0) {
                    K[i][w] = 0;
                }
                else if(items[i-1].getWeight() <= w) {
                    K[i][w] = Math.max(items[i-1].getValue() + K[i-1][w-items[i-1].getWeight()], K[i-1][w]);
                }
                else {
                    K[i][w] = K[i-1][w];
                }
            }
        }
        return K[n][W];
    }
}
class Item {
    
    private int weight;
    private int value;
    
    public Item(int w, int v) {
        this.weight = w;
        this.value = v;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}
